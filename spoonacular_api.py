import requests
from datastore import save_search_results

BASE_URL = "https://api.spoonacular.com/recipes"

def get_recipes(ingredients, api_key):
    """Fetch recipes based on ingredients."""
    url = f"{BASE_URL}/complexSearch"
    params = {
        'query': ingredients,
        'number': 20,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    results =  response.json().get("results", [])

    # Save ingredients and results to Google Cloud Datastore
    save_search_results(ingredients, results)

    return results

def get_recipe_details(recipe_id, api_key):
    """Fetch detailed recipe information."""
    url = f"{BASE_URL}/{recipe_id}/information"
    params = {'apiKey': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

