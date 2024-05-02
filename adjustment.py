import globalPluginHandler
import ctypes
from scriptHandler import script
from logHandler import log
import ui
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    def __init__(self):
        super(GlobalPlugin, self).__init__()

    @script(
        description=_("Allows manual entry of content type to adjust speech rate"),
        gesture="kb:NVDA+leftArrow"
    )
    def script_manualContentTypeEntry(self, gesture):
        # Prompt user to enter the content type
        content_type = ui.inputDialog(
            title="Enter Content Type",
            message="Please enter the content type (e.g., Article, Movies, Podcast, etc.):"
        )
        if content_type:
            content_type = content_type.strip()
            if content_type in ['Article', 'Movies', 'Podcast', 'Research Paper', 'e-commerce', 'Journal', 'Newspaper', 'Magazine']:
                log.info(f"Entered content type: {content_type}")
                ui.message(f"Content type entered as {content_type}. Adjusting speech rate.")
                self.set_speech_rate(content_type)
            else:
                ui.message("Invalid content type entered.")
        else:
            ui.message("No content type entered.")

    def set_speech_rate(self, content_type):
        rate_mapping = {
            'Article': 50,
            'Movies': 55,
            'Podcast': 60,
            'Research Paper': 65,
            'e-commerce': 50,
            'Journal': 55,
            'Newspaper': 60,
            'Magazine': 65
        }
        speech_rate = rate_mapping.get(content_type, 50)  # Default rate if not matched
        nvdaControllerClient.speechSetRate(ctypes.c_int(speech_rate))

# Assuming nvdaControllerClient is properly loaded and initialized elsewhere in your plugin