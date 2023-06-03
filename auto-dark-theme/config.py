import configparser
from pathlib import Path
import platformdirs
import os
import time


class AppConfig:

    CONFIG_DIR_PATH = Path(
        platformdirs.user_config_dir('auto-dark-theme')
    ).resolve()

    CONFIG_FILE_PATH = Path(CONFIG_DIR_PATH, 'config.ini')

    def __init__(self):
        # create config dir if not exist
        os.makedirs(self.CONFIG_DIR_PATH, exist_ok=True)

        # read config
        self.read_file()

        # populate results from config
        self.fillup()

    def read_file(self):
        try:
            ini_path = self.CONFIG_FILE_PATH.resolve()
            self.ini = configparser.ConfigParser()
            self.ini.read_file(open(ini_path))
        except FileNotFoundError:
            raise FileNotFoundError(
                f'Unable to locate config file at "{self.CONFIG_FILE_PATH}"')

    def fillup(self):
        self.start_time_raw = self.ini.get('Timer', 'start_time')
        self.end_time_raw = self.ini.get('Timer', 'end_time')
        # str->struct_time->int conversion
        self.start_time = int(time.strftime(
            '%H', time.strptime(self.start_time_raw, '%H:%M')))
        self.end_time = int(time.strftime(
            '%H', time.strptime(self.end_time_raw, '%H:%M')))

        self.light_theme = self.ini.get('Theme', 'light_theme')
        self.dark_theme = self.ini.get('Theme', 'dark_theme')

    def list_config(self):
        return [
            ['Light Theme', self.light_theme],
            ['Dark Theme', self.dark_theme],
            ['Switch to light theme at', self.end_time_raw],
            ['Switch to  dark theme at', self.start_time_raw],
        ]
