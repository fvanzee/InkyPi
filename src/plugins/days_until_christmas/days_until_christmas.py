from plugins.base_plugin.base_plugin import BasePlugin
from openai import OpenAI
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DaysUntilChristmas(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()

        return template_params


    def generate_image(self, settings, device_config):

        image_template_params = {
            "title": "Days Until Christmas",
            "content": self.get_days_until_christmas(),
            "plugin_settings": settings
        }

        dimensions = device_config.get_resolution()
        if device_config.get_config("orientation") == "vertical":
            dimensions = dimensions[::-1]
        
        image = self.render_image(dimensions, "days_until_christmas.html", "days_until_christmas.css", image_template_params)

        return image
    
    @staticmethod
    def get_days_until_christmas():
        logger.info(f"Getting days until christmas")

        today = datetime.now()
        christmas = datetime(today.year, 12, 25)

        days_until_christmas = (christmas - today).days

        return days_until_christmas
