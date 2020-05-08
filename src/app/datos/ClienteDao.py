from src.app.modelo.Cliente import Cliente
from src.app.datos import GenericDao

debug: bool = GenericDao.debug


def get_all() -> list:
    """
    Obtiene una lista con todos los clientes existentes en la base de datos
    :return: lista de Clientes
    :rtype: list
    """
    clientes = []
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
        clientes.append(cliente)
        if debug:
            print(str(cliente))

    conn.close()
    return clientes


def get_id(idd: int) -> Cliente:
    """
    Busca 1 cliente en la base de datos proporcionando el id
    :param idd: id del cliente
    :type idd: int
    :return: Cliente, si existe
    :rtype: Cliente
    """
    conn = GenericDao.connect()
    cursor = conn.execute("SELECT * FROM clientes where cliente_id = ?", (str(idd),))
    row = cursor.fetchone()
    cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
    if debug:
        print(str(cliente))

    conn.close()
    return cliente


def insert(cliente: Cliente) -> int:
    """
    Inserta un nuevo cliente en la base de datos
    :param cliente: el cliente a insertar
    :type cliente: Cliente
    :return: el id generado para el cliente insertado
    :rtype: int
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()

    sql = 'INSERT INTO clientes(cliente_id) VALUES (?)'
    values = (int(cliente.cliente_id),
              cliente.cliente_nombre,
              cliente.cliente_apellido_1,
              cliente.cliente_apellido_2,
              cliente.cliente_documento,
              cliente.cliente_edad,
              cliente.cliente_provincia)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    cliente.idd = cursor.lastrowid
    if debug:
        print("Cliente insertado: " + str(cliente))
    return cliente.idd


def remove_id(idd: int) -> bool:
    """
    Elimina un cliente de la base de datos en por su id
    :param idd: id del cliente a eliminar
    :type idd: int
    :return: True si fue eliminado
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.execute("DELETE FROM clientes where cliente_id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Cliente eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(cliente: Cliente) -> bool:
    """
    Elimina un cliente de la base de datos por su objeto
    :param cliente: cliente a eliminar
    :type cliente: Cliente
    :return: True si fue eliminado
    :rtype: bool
    """
    return remove_id(cliente.idd)


def update(cliente: Cliente) -> bool:
    """
    Actualiza los datos de un objeto Cliente a la representación en base de datos
    :param cliente: cliente a actualizar
    :type cliente: Cliente
    :return: True si hubo modificaciones
    :rtype: bool
    """
    conn = GenericDao.connect()
    cursor = conn.cursor()
    sql = 'UPDATE clientes SET cliente_id=?, cliente_nombre=?, cliente_apellido_1=?, cliente_apellido_2=?, cliente_documento=?, cliente_edad=?, cliente_provincia=?  WHERE id = ?'
    values = (cliente.cliente_id,
              cliente.cliente_nombre,
              cliente.cliente_apellido_1,
              cliente.cliente_apellido_2,
              cliente.cliente_documento,
              cliente.cliente_edad,
              cliente.cliente_provincia,
              cliente.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Cliente actualizado: " + str(cliente))
    return cursor.rowcount > 0


def get_clientes_provincia(provincia: str) -> list:
    """
    Genera una lista con todos los clientes de la provincia seleccionado
    :param provincia: provincia
    :type provincia: str
    :return: lista de Clientes filtrados por provincia
    :rtype: list<Cliente>
    """
    clientes = []
    conn = GenericDao.connect()
    sql = "SELECT * FROM clientes where cliente_provincia = ?"
    cursor = conn.execute(sql, provincia)
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[6], row[0])
        clientes.append(cliente)
        if debug:
            print(str(cliente))
    conn.close()
    return clientes


