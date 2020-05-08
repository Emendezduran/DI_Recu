import gi


from src.app.datos import ClienteDao
from src.app.vista import PyDialogs
from src.app.vista.ClienteFormularioUI import ClienteFormularioUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ClientesUI(Gtk.Box):
    """
    clase que genera y controla la vista de navegacion de clientes
    """

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.formulario_ui: ClienteFormularioUI = None
        builder = Gtk.Builder()
        builder.add_from_file("/home/emilio/PycharmProjects/DI_Proyecto_Emilio/res/VistaUi.glade")
        signals = {
            "btn_agregar_act": self.on_btn_agregar,
            "btn_eliminar_act": self.on_btn_eliminar,
            "btn_volver_act": self.on_btn_volver,
            "btn_refrescar_act": self.on_btn_refrescar,
        }
        builder.connect_signals(signals)

        '''
        self.elementos_box = builder.get_object("elementos_box")
        self.add(self.elementos_box)
        self.treeview_container = builder.get_object("tree_view_container")

        # Creating the ListStore model
        self.clientes_liststore = Gtk.ListStore(int, str, str, str, str, int, str)
        self.refrescar_tabla()

        self.treeview = Gtk.TreeView(model=self.clientes_liststore)
        for i, column_title in enumerate(["ID", "Nombre", "1er Apellido", "2do Apellido", "Documento", "Edad", "Provincia"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(True)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.treeview_container.add(self.scrollable_treelist)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()
        '''
    def refrescar_tabla(self):
        '''
        """Refresca la tabla de clientes buscando en la base de datos"""
        self.clientes_liststore.clear()
        clientes = ClienteDao.get_all()
        for cliente in clientes:
            cliente_datos = [cliente.idd,
                             cliente.cliente_nombre,
                             cliente.cliente_apellido_1,
                             cliente.cliente_apellido_2,
                             cliente.cliente_documento ,
                             cliente.cliente_edad,
                             cliente.cliente_provincia]
            self.clientes_liststore.append(cliente_datos)
            '''

    def on_btn_volver(self, button):
        """vuelve a la vista de menu principal

        :param button:
        :type button:
        :return:
        """
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        """abre el formulario para agregar un cliente al programa

        :param button:
        :type button:
        :return:
        """
        self.set_sensitive(False)
        self.formulario_ui = ClienteFormularioUI(self)
        self.formulario_ui.show()


    def on_btn_eliminar(self, button):
        """solicita confirmacion al usuario antes de eliminar el cliente seleccionado

        :param button:
        :type button:
        :return:
        """
        selected_id = self.get_selected_id()
        if selected_id > 0:
            confirm = PyDialogs.show_warn_confirm_dialog(self.parent, "Eliminacion del cliente",
                                                         "Seguro que deseas eliminar el cliente con id: "
                                                         + str(selected_id))
            if confirm:
                print("Eliminando el cliente con id: " + str(selected_id))
                eliminado = ClienteDao.remove_id(selected_id)
                info = " " if eliminado else " no "
                PyDialogs.show_info_dialog(self.parent, "Eliminando", "El Cliente" + info + "fue eliminado.")
                self.refrescar_tabla()


    def on_btn_refrescar(self, button):
        """refresca la tabla de clientes

        :param button:
        :return:
        """
        self.refrescar_tabla()

    def return_from_child(self):
        """reactiva una ventana al cerrar una de sus ventanas secundarias
        """
        self.set_sensitive(True)
        self.refrescar_tabla()
        self.editor_ui.destroy()
        self.editor_ui = None

    def get_selected_id(self) -> int:
        """retorna el id del objeto seleccionado

        :return: id del objeto
        :rtype: int
        """
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter is not None:
            selected_id = model[treeiter][0]
            return selected_id
        return 0