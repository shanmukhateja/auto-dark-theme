from time import localtime, strftime
from .config import AppConfig
from .spawn import Spawner


class ThemeSwitcher:
    def __init__(self):
        self.hour = int(strftime("%H", localtime()))
        self.config = AppConfig()
        self.spawner = Spawner()

    def run(self):
        print("Switching theme...")
        if self.hour >= self.config.start_time:
            print('Dark theme selected.')
            self.switch_to_dark()
        else:
            print('Light theme selected.')
            self.switch_to_light()

    def switch_to_light(self):
        self.spawner.spawn_tool(self.config.light_theme)

    def switch_to_dark(self):
        self.spawner.spawn_tool(self.config.dark_theme)
