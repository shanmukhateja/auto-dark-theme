import dbus

# Main loop
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib  # type: ignore

from .switcher import ThemeSwitcher

# Create mainloop
DBusGMainLoop(set_as_default=True)
loop = GLib.MainLoop()
GLib.MainLoop()


class DbusListener:

    def handle_lock_unlock(listener, *args):  # type: ignore
        if args[0] == dbus.Boolean(False):
            ThemeSwitcher().run()

    def __init__(self):
        print("Initializing...")
        self.session_bus = dbus.SessionBus()
        self.system_bus = dbus.SystemBus()

        self.iface_screen_lock = self.session_bus.get_object(
            'org.freedesktop.ScreenSaver', '/org/freedesktop/ScreenSaver')
        self.iface_screen_lock.connect_to_signal(
            'ActiveChanged', handler_function=self.handle_lock_unlock)

        self.iface_suspend = self.system_bus.get_object(
            'org.freedesktop.login1', '/org/freedesktop/login1')
        self.iface_suspend.connect_to_signal(
            'PrepareForSleep', handler_function=self.handle_lock_unlock)

        try:
            # Apply theme on init
            self.handle_lock_unlock(dbus.Boolean(False))
            # Start event loop
            loop.run()
        except:
            print("Shutting down..")
            self.session_bus.close()
            self.system_bus.close()
            loop.quit()
