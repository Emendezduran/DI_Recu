from src.app.modelo.Categoria import Categoria
from src.app.datos import GenericDao

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos las categorias existentes en la base de datos
    :return: lista de categorias
    :rtype: list
    """
    categorias = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM categorias")
    for row in cursor:
        categoria = Categoria(row[1], row[0])
        categorias.append(categoria)
        if debug:
            print(str(categoria))

    conn.close()
    return categorias


def get_id(idd: int) -> Categoria:
    """
    Busca 1 categoria en la base de datos proporcionando el id
    :param idd: id de categoria
    :type idd: int
    :return: Categoria, si existe en la base de datos
    :rtype: Categoria
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM categorias where categoria_id = ?", (str(idd),))
    row = cursor.fetchone()
    categoria = Categoria(row[1], row[0])
    if debug:
        print(str(categoria))

    conn.close()
    return categoria


def insert(categoria: Categoria) -> int:
    """
    Inserta una nueva categoria en la base de datos
    :param categoria: categoria a insertar
    :type categoria: Categoria
    :return: el id generado para la categoria insertada
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()

    sql = 'INSERT INTO categorias(categoria_id) VALUES (?)'
    values = (int(categoria.categoria_id),
              categoria.categoria_nombre)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    categoria.idd = cursor.lastrowid
    if debug:
        print("Categoria insertada: " + str(categoria))
    return categoria.idd


def remove_id(idd: int) -> bool:
    """
    Elimina una categoria de la base de datos por su id
    :param idd: id de la categoria a eliminar
    :type idd: int
    :return: True si fue eliminada
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM categorias where categoria_id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Categoria eliminada: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(categoria: Categoria) -> bool:
    """
    Elimina una categoria de la base de datos por su objeto
    :param categoria: categoria a eliminar
    :type categoria: Categoria
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(categoria.idd)


def update(categoria: Categoria) -> bool:
    """
    Actualiza los datos de un objeto Categoria a la representación en base de datos
    :param categoria: categoria a actualizar
    :type categoria: Categoria
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE categorias SET categoria_id=?, categoria_nombre=?  WHERE id = ?'
    values = (categoria.categoria_id, categoria.categoria_nombre, categoria.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Categoria actualizada: " + str(categoria))
    return cursor.rowcount > 0

