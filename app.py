from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
from google.cloud import secretmanager
from flask.views import MethodView
from spoonacular_api import get_recipes, get_recipe_details
from google_calendar import create_calendar_event
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load API Keys
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

# Routes
class Index(MethodView):
    def get(self):
        return render_template('index.html')

class Recipes(MethodView):
    def post(self):
        ingredients = request.form.get('ingredients', '').strip()
        recipes = get_recipes(ingredients, SPOONACULAR_API_KEY)
        return render_template('recipes.html', recipes=recipes)

class RecipeDetails(MethodView):
    def get(self, recipe_id):
        recipe = get_recipe_details(recipe_id, SPOONACULAR_API_KEY)

        # Ensure the recipe description is safely rendered as HTML
        if 'description' in recipe:
            recipe['description'] = Markup(recipe['description'])

        return render_template('recipe_details.html', recipe=recipe)

class AddToCalendar(MethodView):
    def get_service_account_key(self, secret_name):
        """Fetch service account key from Secret Manager."""
        try:
            # Initialize the Secret Manager client
            client = secretmanager.SecretManagerServiceClient()

            # Build the secret resource name
            project_id = os.getenv("GOOGLE_CLOUD_PROJECT")  
            secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

            # Access the secret
            response = client.access_secret_version(request={"name": secret_path})
            secret_payload = response.payload.data.decode("UTF-8")

            # Return the secret as a dictionary
            return json.loads(secret_payload)
        except Exception as e:
            raise RuntimeError(f"Failed to fetch service account key from Secret Manager: {str(e)}")

    def post(self):
        # Get event details from the form data
        event_details = {
            'summary': request.form['title'],
            'description': request.form['description'],
            'start': {
                'dateTime': f"{request.form['start_datetime']}:00",
                'timeZone': 'America/Los_Angeles'  # Explicitly set to Los Angeles time
            },
            'end': {
                'dateTime': f"{request.form['end_datetime']}:00",
                'timeZone': 'America/Los_Angeles'  # Explicitly set to Los Angeles time
            }
        }

        # Get the user's email from the form data
        user_email = request.form['user_email']

        # Fetch the service account key from Secret Manager
        try:
            secret_name = "service-account-key" 
            service_account_info = self.get_service_account_key(secret_name)
        except RuntimeError as e:
            return {'message': str(e)}, 500

        # Create calendar event
        event = create_calendar_event(event_details, service_account_info, user_email)

        # Check if the event was created successfully
        if event and 'htmlLink' in event:
            return redirect(event['htmlLink'])
        else:
            return {'message': 'Unable to add event. Please go to Google Calendar > Settings > Share with Specific People and add calendar-service-account@cloud-bojedla-jbojedla-439000.iam.gserviceaccount.com email to make changes to events'}, 400

# Register routes
app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/recipes', view_func=Recipes.as_view('recipes'))
app.add_url_rule('/recipe/<int:recipe_id>', view_func=RecipeDetails.as_view('recipe_details'))
app.add_url_rule('/add_to_calendar', view_func=AddToCalendar.as_view('add_to_calendar'))

if __name__ == '__main__':
    app.run(debug=True)

