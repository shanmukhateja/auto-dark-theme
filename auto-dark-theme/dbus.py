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
        self.bus = dbus.SessionBus()
        self.bus_name = 'org.freedesktop.ScreenSaver'
        self.object_path = '/org/freedesktop/ScreenSaver'
        self.signal_name = 'ActiveChanged'

        self.iface = self.bus.get_object(self.bus_name, self.object_path)

        print("Listening for screen lock/unlock signal...")
        self.iface.connect_to_signal(
            self.signal_name, handler_function=self.handle_lock_unlock)

        try:
            loop.run()
        except:
            print("Shutting down..")
            self.bus.close()
            loop.quit()
