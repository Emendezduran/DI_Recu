import sqlite3

"""
variable para determinar si se imprimen las sentencias sql (debugging)
"""
debug: bool = False


def connect() -> sqlite3.Connection:
    """
    inicia la conexion a la base de datos con las restricciones de foreign keys activadas
    :return: la conexion hecha a la base de datos
    :rtype: sqlite3.Connection
    """
    conn = sqlite3.connect("/home/emilio/PycharmProjects/DI_Proyecto_Emilio/res/sqlite.db")
    conn.execute('PRAGMA foreign_keys=1;')
    return conn
