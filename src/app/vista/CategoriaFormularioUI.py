import gi


from src.app.modelo.Categoria import Categoria

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProductoFormularioUI(Gtk.Window):
    """clase que genera y controla el formulario de categoria
    """

    def __init__(self, parent, categoria: Categoria = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = categoria is None
        if self.creating:
            self.categoria = Categoria('', '')
        else:
            self.categoria = categoria

        builder = Gtk.Builder()
        builder.add_from_file(Globals.path_res + "/CategoriaNuevoUI.glade")
        signals = {
            "btn_volver_act": self.on_btn_cancelar,
            "btn_guardar_act": self.on_btn_guardar
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("categoria_formulario_box")
        self.add(self.box_ui)

        self.categoria_nombre_entry: Gtk.Entry = builder.get_object("categoria_nombre_entry")
        self.producto_nombre_entry.set_text(self.producto.producto_nombre)
        self.show_all()

    def on_btn_volver(self, button):
        """volver al menu principal

        :param button:
        :type button:
        :return:
        """
        self.parent.return_from_child()

    def on_btn_guardar_act(self, button):
        """guarda los datos ingresados inicializando e insertando un nuevo objeto

        :param button:
        :type button:
        :return:
        :rtype:
        """
        self.categoria.categoria_nombre = self.categoria_nombre_entry.get_text()
        if self.creating:
            self.producto.insert()
        else:
            self.producto.update()
        self.parent.return_from_child()