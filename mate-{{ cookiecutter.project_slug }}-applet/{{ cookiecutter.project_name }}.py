#!/usr/bin/python3
import logging
import signal
import time
import os
import sys
import threading
import socket
signal.signal(signal.SIGINT, signal.SIG_DFL)
# --------------------------------------------------------
import gi

gi.require_version("Gtk", "3.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gio", "2.0")
gi.require_version('MatePanelApplet', '4.0')
from gi.repository import Gtk, GLib, Gio
from gi.repository import MatePanelApplet


current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_path)

def exception_handler(type, value, traceback):
    logging.exception(f"Uncaught exception occurred: {value}")
    logging.debug(f"{value}")
    sys.__excepthook__(type, value, traceback)  # calls default excepthook


logger = logging.getLogger("{{ cookiecutter.project_name }}Log")
logger.setLevel(logging.ERROR)

sys.excepthook = exception_handler

file_handler = logging.FileHandler(os.path.expanduser("/tmp/{{ cookiecutter.project_name }}.log"))
file_handler.setFormatter(
    logging.Formatter('[%(levelname)s] %(asctime)s: %(message)s', "%Y-%m-%d %H:%M:%S")
)
logger.addHandler(file_handler)

def applet_fill(applet):

    label = Gtk.Label(label="{{ cookiecutter.project_name }}")
    applet.add(label)
    applet.show_all()

def applet_factory(applet, iid, data):
    if iid != "{{ cookiecutter.project_name }}":
       return False
 
    applet_fill(applet)
 
    return True


MatePanelApplet.Applet.factory_main("{{ cookiecutter.project_name }}", True,
                                    MatePanelApplet.Applet.__gtype__,
                                    applet_factory, None)


def main():
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    applet_factory(win, "{{ cookiecutter.project_name }}", None)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
