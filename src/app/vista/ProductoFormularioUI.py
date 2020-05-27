import gi

from src.app.modelo.Producto import Producto

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProductoFormularioUI(Gtk.Window):
    """clase que genera y controla el formulario de productos
    """

    def __init__(self, parent, producto: Producto = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = producto is None
        if self.creating:
            self.producto = Producto('', '', '', '', '')
        else:
            self.producto = producto

        builder = Gtk.Builder()
        builder.add_from_file("/home/emilio/PycharmProjects/DI_Proyecto_Emilio/res/ProductoNuevoUi.glade")
        signals = {
            "btn_volver_act": self.on_btn_volver,
            "btn_limpiar_act": self.on_btn_limpiar,
            "btn_guardar_act": self.on_btn_guardar
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.producto_nombre_entry: Gtk.Entry = builder.get_object("producto_nombre_entry")
        self.producto_precio_entry: Gtk.Entry = builder.get_object("producto_precio_entry")
        self.producto_stock_entry: Gtk.Entry = builder.get_object("producto_stock_entry")
        #self.producto_categoria_combo: Gtk.Entry = builder.get_object("producto_categoria_combo")

        self.producto_nombre_entry.set_text(self.producto.producto_nombre)
        self.producto_precio_entry.set_text(str(self.producto.producto_precio))
        self.producto_stock_entry.set_text(str(self.producto.producto_stock))
        #self.producto_categoria_combo.set_text(self.producto.producto_categoria)

        self.show_all()

    def on_btn_volver(self, button):
        """volver a la lista de productos

        :param button:
        :type button:
        :return:
        """
        self.parent.return_from_child()

    def on_btn_guardar(self, button):
        """guarda los datos ingresados inicializando e insertando un nuevo objeto

        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.producto.producto_nombre = self.producto_nombre_entry.get_text()
        self.producto.producto_precio = int(self.producto_precio_entry.get_text())
        self.producto.producto_stock = int(self.producto_stock_entry.get_text())
        # self.producto.producto_categoria = self.producto_categoria_combo.get_text()
        if self.creating:
            self.producto.insert()
        else:
            self.producto.update()
        self.parent.return_from_child()

    def on_btn_limpiar(self, button):
        pass
