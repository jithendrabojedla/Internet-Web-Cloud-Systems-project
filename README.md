**Recipe Planner Web Application**

**Overview**

This is a Flask-based web application that helps users discover recipes based on their input ingredients and allows them to schedule selected recipes in Google Calendar. The application integrates with the Spoonacular API to fetch recipe details and the Google Calendar API for scheduling meals. The app is designed to be containerized using Docker and deployed on cloud platforms.

**Features**

1. Recipe Search
   
   Users enter ingredients in a search form (e.g., "chicken, rice, carrots").

   The app queries the Spoonacular API and fetches recipes based on the input.

   The results are displayed with recipe titles, images, and links to view detailed information.

2. Recipe Details

   Clicking on a recipe displays:

   Recipe title

   Image

   Instructions

   List of ingredients

   Users can schedule the recipe in their Google Calendar by entering event details (title, description, date, time, and email).

3. Google Calendar Integration
   
   The app securely authenticates using a Google service account stored in Google Cloud Secret Manager.

   Users can add a selected recipe as an event to their Google Calendar.

4. Data Storage in Google Cloud Datastore

   The application saves search results (ingredients and recipe data) as entities in Google Cloud Datastore for future retrieval.

5. Docker Support

   The project includes a Dockerfile for containerizing the application.

   The containerized app can be deployed on cloud platforms such as Google Cloud Run.

**Project Structure**

📂 final/

│-- 📂 static/ (Contains CSS styles) 

│-- 📂 templates/ (HTML Templates) 

│   │-- index.html (Homepage with search form)  

│   │-- recipes.html (Displays list of recipes)  

│   │-- recipe_details.html (Detailed recipe view + Calendar form)  

│-- .gitignore  

│-- app.py (Main Flask application) 

│-- datastore.py (Interacts with Google Cloud Datastore)  

│-- google_calendar.py (Google Calendar API integration)  

│-- spoonacular_api.py (Handles Spoonacular API calls) 

│-- requirements.txt (Project dependencies)  

│-- Dockerfile (Containerizes the application)

│-- project_url.txt (Project deployment URL) 

│-- screencast_url.txt (Demo video link)  

**Installation & Setup**

1. Clone the Repository:

   git clone https://github.com/jithendrabojedla/Internet-Web-Cloud-Systems-project.git

   cd Internet-Web-Cloud-Systems-project

2. Create a Virtual Environment & Install Dependencies:

   python -m venv env

   source env/bin/activate  # On Windows use: env\Scripts\activate

   pip install -r requirements.txt


3. Set Up Environment Variables:

   Configure API keys for Spoonacular and Google Cloud Secret Manager.

4. Run the Flask Application:

   python app.py

5. Access the Application:

   Open http://127.0.0.1:5000/ in your browser.


**Deployment with Docker**

1. Build the Docker Image

   docker build -t recipe-planner .

2. Run the Container

   docker run -p 5000:5000 recipe-planner

**Technologies Used**

> Flask (Backend Framework)

> HTML, CSS (Frontend)

> Spoonacular API (Recipe Data)

> Google Calendar API (Event Scheduling)

> Google Cloud Datastore (Data Storage)

> Docker (Containerization)

**Author**

Developed by Jithendra Bojedla as part of the Internet, Web, and Cloud Systems Course Project.
