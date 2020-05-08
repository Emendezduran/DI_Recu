import gi

from src.app.vista.MainUI import MainUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

"""
Main de la app
"""

if __name__ == "__main__":
    MainUI()
    Gtk.main()
