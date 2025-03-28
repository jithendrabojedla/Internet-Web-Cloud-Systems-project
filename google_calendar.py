from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def create_calendar_event(event_details, service_account_info, user_email):
    # Define the required scope for calendar access
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    # Authenticate using the service account and the specified scope
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)
    
    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)
    
    try:
        # Insert the event into the specified calendar (user_email)
        event = service.events().insert(
            calendarId=user_email, body=event_details).execute()
        return event
    except HttpError as error:
        print(f"Google Calendar API error: {error}")
        return None

