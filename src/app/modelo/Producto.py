from src.app.datos import ProductoDao


class Producto:
    """
    Clase modelo Producto
    """

    def __init__(self, producto_nombre, producto_precio, producto_stock, producto_categoria, idd=0):
        """Constructor unico con parametros, un objeto de este tipo se inicializara
        con el id 0 y al ser insertado en sqlite se le asigna un id

        :param producto_id:
        :param producto_nombre:
        :param producto_precio:
        :param producto_stock:
        :param producto_categoria:
        :param idd:
        """

        self.idd: int = idd
        self.producto_nombre: str = producto_nombre
        self.producto_precio: int = producto_precio
        self.producto_stock: str = producto_stock
        self.producto_categoria: str = producto_categoria

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return ProductoDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return ProductoDao.remove(self)

    def update(self):
        """
        actualizar la base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return ProductoDao.update(self)

    def __str__(self) -> str:
        return super().__str__()