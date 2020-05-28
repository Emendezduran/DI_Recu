from app.datos import CategoriaDao, ClienteDao, ProductoDao

def testCategorias():
    list = CategoriaDao.get_all()
    for cat in list:
        print(cat)


def testClientes():
    list = ClienteDao.get_all()
    for cli in list:
        print(cli)


def testProductos():
    list = ProductoDao.get_all()
    for pro in list:
        print(pro)


# testClientes()
# testCategorias()
testProductos()
