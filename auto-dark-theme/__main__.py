import os

from .dbus import DbusListener
from .config import AppConfig


def is_de_valid():
    # https://unix.stackexchange.com/a/366055
    desktop_env = os.environ.get(
        'XDG_CURRENT_DESKTOP') or os.environ.get('AUTO_DARK_THEME_DE')
    if not desktop_env:
        raise Exception("Unable to determine Desktop environment.")
    desktop_env = desktop_env.lower()
    if not desktop_env == 'kde':
        raise Exception("Unsupported Desktop Environment.")

    return True


def main():
    # quit if not running in KDE
    assert (is_de_valid())

    # app config
    AppConfig()

    # init dbus listener
    DbusListener()


if __name__ == '__main__':
    main()
