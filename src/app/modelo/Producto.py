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

    def __str__(self) -> str:
        return str(self.idd) + ' ' + self.producto_nombre + ' ' + str(self.producto_precio) + ' ' + str(
            self.producto_stock) + ' ' + str(self.producto_categoria)
