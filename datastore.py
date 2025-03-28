from google.cloud import datastore

# Initialize Datastore client
datastore_client = datastore.Client()

def save_search_results(ingredients, results):
    """
    Save entered ingredients and results into Google Cloud Datastore.
    """
    entity_key = datastore_client.key("RecipeSearch")
    entity = datastore.Entity(key=entity_key)
    entity.update({
        "ingredients": ingredients,
        "results": results,
    })
    datastore_client.put(entity)
    print("Data successfully saved to Datastore.")

