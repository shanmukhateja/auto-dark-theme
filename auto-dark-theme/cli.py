import argparse
from tabulate import tabulate

from .switcher import ThemeSwitcher
from .config import AppConfig

parser = argparse.ArgumentParser(
    prog='auto-dark-theme', description='Switch your DE theme between light/dark themes acc. to specified time for KDE Plasma')

# Add args

# -t || --theme
parser.add_argument(
    '-t', '--theme', choices=['light', 'dark'], required=False, help='Forcefully switch between light/dark theme.')
# List config
parser.add_argument(
    '-l', '--list-config', action='store_true', help='List current config.')

# Parse & process
result = parser.parse_args()

# Trigger theme change if provided
if result.theme == 'light':
    ThemeSwitcher().switch_to_light()
if result.theme == 'dark':
    ThemeSwitcher().switch_to_dark()

if (result.list_config):
    app_config = AppConfig().list_config()
    print(tabulate(app_config, headers=['Option', 'Value'], tablefmt="outline"))