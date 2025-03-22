from datetime import datetime, timezone
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from plugins.base_plugin.base_plugin import BasePlugin

# Google Calendar API Setup
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials/google_credentials.json")
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "fvanzee@gmail.com"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)

class Calendar(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()
        return template_params

    def generate_image(self, settings, device_config):
        events = self.get_upcoming_events(settings.get("account"))
        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        template_params = {
            "events": events, 
            "plugin_settings": settings
        }
        image = self.render_image(dimensions, "calendar.html", "calendar.css", template_params)
        return image

    def get_upcoming_events(self, account):
        """Fetch upcoming Google Calendar events"""
        now = datetime.now(timezone.utc).isoformat()
        events_result = service.events().list(
            calendarId=account,
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime"
        ).execute()
        return events_result.get("items", [])
