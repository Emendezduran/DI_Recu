from src.app.datos import CategoriaDao


class Categoria:
    """
    Clase modelo Categoria
    """

    def __init__(self, categoria_nombre, idd=0):
        """Constructor unico con parametros, un objeto de este tipo se inicializara
        con el id 0 y al ser insertado en sqlite se le asigna un id

        :param categoria_id:
        :param categoria_nombre:
        :param idd:
        """

        self.idd: int = idd
        self.categoria_nombre: str = categoria_nombre

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return CategoriaDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return CategoriaDao.remove(self)

    def update(self):
        """
        actualizar la base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return CategoriaDao.update(self)

    def __str__(self) -> str:
        return super().__str__()