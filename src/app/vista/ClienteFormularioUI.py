import gi

from src.app.modelo.Cliente import Cliente

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClienteFormularioUI(Gtk.Window):
    """clase que genera y controla el formulario de clientes
    """

    def __init__(self, parent, cliente: Cliente = None):
        Gtk.Window.__init__(self)
        self.parent = parent
        self.creating: bool = cliente is None
        if self.creating:
            self.cliente = Cliente('', '', '', '', 0, '')
        else:
            self.cliente = cliente

        builder = Gtk.Builder()
        builder.add_from_file("/home/emilio/PycharmProjects/DI_Proyecto_Emilio/res/ClienteNuevoUi.glade")
        signals = {
            "btn_volver_act": self.on_btn_volver,
            "btn_limpiar_act": self.on_btn_limpiar,
            "btn_guardar_act": self.on_btn_guardar
        }
        builder.connect_signals(signals)
        self.box_ui = builder.get_object("box_ui")
        self.add(self.box_ui)

        self.cliente_nombre_entry: Gtk.Entry = builder.get_object("cliente_nombre_entry")
        self.cliente_apellido_1_entry: Gtk.Entry = builder.get_object("cliente_apellido_1_entry")
        self.cliente_apellido_2_entry: Gtk.Entry = builder.get_object("cliente_apellido_2_entry")
        self.cliente_documento_entry: Gtk.Entry = builder.get_object("cliente_documento_entry")
        self.cliente_edad_entry: Gtk.Entry = builder.get_object("cliente_edad_entry")
        self.cliente_provincia_entry: Gtk.Entry = builder.get_object("cliente_provincia_entry")


        self.cliente_nombre_entry.set_text(self.cliente.cliente_nombre)
        self.cliente_apellido_1_entry.set_text(self.cliente.cliente_apellido_1)
        self.cliente_apellido_2_entry.set_text(self.cliente.cliente_apellido_2)
        self.cliente_documento_entry.set_text(self.cliente.cliente_documento)
        self.cliente_edad_entry.set_text(str(self.cliente.cliente_edad))
        self.cliente_provincia_entry.set_text(self.cliente.cliente_provincia)

        self.show_all()

    def on_btn_volver(self, button):
        """volver a la lista de clientes

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

        self.cliente.cliente_nombre = self.cliente_nombre_entry.get_text()
        self.cliente.cliente_apellido_1 = self.cliente_apellido_1_entry.get_text()
        self.cliente.cliente_apellido_2 = self.cliente_apellido_2_entry.get_text()
        self.cliente.cliente_documento = self.cliente_documento_entry.get_text()
        self.cliente.cliente_edad = int(self.cliente_edad_entry.get_text())
        self.cliente.cliente_provincia = self.cliente_provincia_entry.get_text()
        if self.creating:
            self.cliente.insert()
        else:
            self.cliente.update()
        self.parent.return_from_child()

    def on_btn_limpiar(self, button):
        pass
