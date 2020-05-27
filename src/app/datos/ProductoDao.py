from src.app.datos import GenericDao
from src.app.modelo.Producto import Producto

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los productos existentes en la base de datos
    :return: lista de Productos
    :rtype: list
    """
    productos = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM productos")
    for row in cursor:
        producto = Producto(row[1], row[2], row[3], row[4], row[0])
        productos.append(producto)
        if debug:
            print(str(producto))

    conn.close()
    return productos


def get_id(idd: int) -> Producto:
    """
    Busca 1 producto en la base de datos proporcionando el id
    :param idd: id del cliente
    :type idd: int
    :return: Producto, si existe
    :rtype: Producto
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM productos where producto_id = ?", (str(idd),))
    row = cursor.fetchone()
    producto = Producto(row[1], row[2], row[3], row[4], row[0])
    if debug:
        print(str(producto))

    conn.close()
    return producto


def insert(producto: Producto) -> int:
    """
    Inserta un nuevo producto en la base de datos
    :param producto: el producto a insertar
    :type producto: Producto
    :return: el id generado para el producto insertado
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()

    sql = 'INSERT INTO productos(producto_id) VALUES (?)'
    values = (int(producto.producto_id),
              producto.producto_nombre,
              producto.producto_precio,
              producto.producto_stock,
              producto.producto_categoria)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    producto.idd = cursor.lastrowid
    if debug:
        print("Producto insertado: " + str(producto))
    return producto.idd


def remove_id(idd: int) -> bool:
    """
    Elimina un producto de la base de datos en por su id
    :param idd: id del producto a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM productos where producto_id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Producto eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(producto: Producto) -> bool:
    """
    Elimina un producto de la base de datos por su objeto
    :param producto: producto a eliminar
    :type producto: Producto
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(producto.idd)


def update(producto: Producto) -> bool:
    """
    Actualiza los datos de un objeto Producto a la representación en base de datos
    :param producto: producto a actualizar
    :type producto: Producto
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE productos SET producto_id=?, producto_nombre=?, producto_precio=?, producto_stock=?, categoria_id=?  WHERE producto_id = ?'
    values = (producto.producto_id,
              producto.producto_nombre,
              producto.producto_precio,
              producto.producto_stock,
              producto.producto_categoria,
              producto.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Producto actualizado: " + str(producto))
    return cursor.rowcount > 0


def get_productos_stock(stock: int) -> list:
    """
    Genera una lista con todos los poductos con stock inferior o igual a lo indicado
    :param stock: stock
    :type stock: int
    :return: lista de Productos filtrados por stock
    :rtype: list<Producto>
    """
    productos = []
    conn = GenericDao.connect()
    sql = "SELECT * FROM productos where producto_stock <= ?"
    cursor = conn.execute(sql, stock)
    for row in cursor:
        producto = Producto(row[1], row[2], row[3], row[4], row[0])
        productos.append(producto)
        if debug:
            print(str(producto))
    conn.close()
    return productos
