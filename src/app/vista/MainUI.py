import gi

from app.reportes import Reportes_script
from src.app.vista.ClientesUI import ClientesUI
from src.app.vista.ProductosUI import ProductosUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainUI(Gtk.Window):
    """
    clase que genera y controla la el menu principal de la applicacion
    """

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)

        self.active_pane = None

        builder = Gtk.Builder()
        builder.add_from_file("/home/emilio/PycharmProjects/DI_Proyecto_Emilio/res/MainUi.glade")
        self.box_ui = builder.get_object("box_ui")
        self.show_main_menu()

        signals = {
            "btn_clientes_act": self.on_btn_clientes,
            "btn_productos_act": self.on_btn_productos,
            "btn_reportes_act_1": self.on_btn_reportes_1,
            "btn_reportes_act_2": self.on_btn_reportes_2,
        }
        builder.connect_signals(signals)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_btn_reportes_1(self, button):

        """
        genera el reporte de productos con stock inferior a 12
        :param button:
        :type button:
        :return:
        :rtype:
        """
        Reportes_script.reporte_stock_minimo()

    def on_btn_reportes_2(self, button):

        """
        genera el reporte del numero de clientes por provincia
        :param button:
        :type button:
        :return:
        :rtype:
        """
        Reportes_script.reporte_provincias()

    def on_btn_clientes(self, button):
        """
        abre el editor de clientes
        :param button:
        :type button:
        :return:
        :rtype:
        """
        clientes_ui = ClientesUI(self)
        self.set_active_pane(clientes_ui)

    def on_btn_productos(self, button):
        """
        abre el editor de productos
        :param button:
        :type button:
        :return:
        :rtype:
        """
        productos_ui = ProductosUI(self)
        self.set_active_pane(productos_ui)


    def set_active_pane(self, pane):
        """
        metodo que amuestra en la ventana principal un Gtk.Widget recibido como parametro
        :param pane:
        :type pane:
        :return:
        :rtype:
        """
        if self.active_pane is not None:
            self.remove(self.active_pane)
        self.active_pane = pane
        if self.active_pane is not None:
            self.add(self.active_pane)

    def show_main_menu(self):
        """
        muestra el menu principal

        este metodo sera llamado por todos los hijos de esta ventana para volver al menu principal
        :return:
        :rtype:
        """
        self.set_active_pane(self.box_ui)
