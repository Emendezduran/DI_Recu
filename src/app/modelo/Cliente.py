from src.app.datos import ClienteDao


class Cliente:
    """
    Clase modelo Cliente
    """

    def __init__(self, cliente_nombre, cliente_apellido_1, cliente_apellido_2, cliente_documento, cliente_edad, cliente_provincia, idd=0):
        """ Constructor unico con parametros, un objeto de este tipo se inicializara
        con el id 0 y al ser insertado en sqlite se le asigna un id

        :param cliente_id:
        :param cliente_nombre:
        :param cliente_apellido_1:
        :param cliente_apellido_2:
        :param cliente_documento:
        :param cliente_edad:
        :param cliente_provincia:
        :param idd:
        """

        self.idd: int = idd
        self.cliente_nombre: str = cliente_nombre
        self.cliente_apellido_1: str = cliente_apellido_1
        self.cliente_apellido_2: str = cliente_apellido_2
        self.cliente_documento: str = cliente_documento
        self.cliente_edad: int = cliente_edad
        self.cliente_provincia: str = cliente_provincia


    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return ClienteDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return ClienteDao.remove(self)

    def update(self):
        """
        actualizar la base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return ClienteDao.update(self)

    def __str__(self) -> str:
        return super().__str__()
"""
    def __str__(self) -> str:
        return 'Cliente { ' + \
               str(self.idd) + ', ' + \
               str(self.cliente_id) + ', ' + \
               str(self.cliente_nombre) + ' };'
"""