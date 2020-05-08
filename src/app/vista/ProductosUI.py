import gi


from src.app.datos import ProductoDao
from src.app.vista import PyDialogs
from src.app.vista.ProductoFormularioUI import ProductoFormularioUI

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ProductosUI(Gtk.Box):
    """
    clase que genera y controla la vista de navegacion de productos
    """

    def __init__(self, parent=None):
        Gtk.Box.__init__(self)
        self.parent = parent
        self.editor_ui: ProductoFormularioUI = None
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
        self.productos_liststore = Gtk.ListStore(int, str, int, int, str)
        # self.refrescar_tabla()

        self.treeview = Gtk.TreeView(model=self.productos_liststore)
        for i, column_title in enumerate(["ID", "Nombre", "Precio", "Stock", "Categoria"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_resizable(True)
            self.treeview.append_column(column)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        #self.treeview_container.add(self.scrollable_treelist)
        #self.scrollable_treelist.add(self.treeview)

        self.show_all()
        '''
    def refrescar_tabla(self):
        '''
        """Refresca la tabla de productos buscando en la base de datos"""
        self.productos_liststore.clear()
        productos = ProductoDao.get_all()
        for producto in productos:
            producto_datos = [producto.producto.idd,
                              producto.producto_nombre,
                              producto.producto_precio,
                              producto.producto_stock,
                              producto.producto_categoria]
            self.productos_liststore.append(producto_datos)
        '''

    def on_btn_volver(self, button):
        """vuelve a la vista de menu principal

        :param button:
        :type button:
        :return:
        """
        self.parent.show_main_menu()

    def on_btn_agregar(self, button):
        """abre el formulario para agregar un producto al programa

        :param button:
        :type button:
        :return:
        """
        self.set_sensitive(False)
        self.editor_ui = ProductoFormularioUI(self)
        self.editor_ui.show()

    def on_btn_eliminar(self, button):
        """solicita confirmacion al usuario antes de eliminar el cliente seleccionado

        :param button:
        :type button:
        :return:
        """
        selected_id = self.get_selected_id()
        if selected_id > 0:
            confirm = PyDialogs.show_warn_confirm_dialog(self.parent, "Eliminacion del producto",
                                                         "Seguro que deseas eliminar el producto con id: "
                                                         + str(selected_id))
            if confirm:
                print("Eliminando producto con id: " + str(selected_id))
                eliminado = ProductoDao.remove_id(selected_id)
                info = " " if eliminado else " no "
                PyDialogs.show_info_dialog(self.parent, "Eliminando", "El Producto" + info + "fue eliminado.")
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