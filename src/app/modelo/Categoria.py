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

    def __str__(self) -> str:
        return str(self.idd) + ' ' + self.categoria_nombre
