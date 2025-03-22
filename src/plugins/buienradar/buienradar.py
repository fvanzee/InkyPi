from plugins.base_plugin.base_plugin import BasePlugin
import logging

logger = logging.getLogger(__name__)

class Buienradar(BasePlugin):
    def generate_settings_template(self):
        template_params = super().generate_settings_template()

        return template_params

    def generate_image(self, settings, device_config):

        image = self.render_image([500, 512], "buienradar.html", "buienradar.css", {})
        return image
