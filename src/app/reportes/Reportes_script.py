from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate

from app.datos import ProductoDao
from src.app.datos import ClienteDao

"""
Scripts de generacion de reportes
"""


def reporte_provincias():
    """
    genera un reporte en pdf con una lista de las provincias donde hay clientes y el numero de clientes por provincia
    :return:
    :rtype:
    """
    provincias = ClienteDao.get_clientes_provincia()
    hoja_estilo = getSampleStyleSheet()
    guia = []
    heading = hoja_estilo['Heading4']
    guia.append(Paragraph("LISTADO DE CLIENTES POR PROVINCIA: ", heading))
    guia.append(Spacer(0, 20))

    div_listado = hoja_estilo['BodyText']
    it = iter(provincias)
    for x in it:
        guia.append(Paragraph(x, div_listado))
        guia.append(Spacer(0, 10))

    doc = SimpleDocTemplate("ClientesPorProvincia.pdf", pagesize=A4, showBoundary=0)
    doc.build(guia)


def reporte_stock_minimo():
    """
    genera un reporte en pdf con una lista de productos que tienen menos de 12 unidades en stock
    :return:
    :rtype:
    """
    productos = ProductoDao.get_productos_stock(12)
    hoja_estilo = getSampleStyleSheet()
    guia = []
    heading = hoja_estilo['Heading3']
    guia.append(Paragraph("PRODUCTOS CON STOCK INFERIOR A 12: ", heading))
    guia.append(Spacer(0, 20))

    div_productos = hoja_estilo['BodyText']
    for producto in productos:
        guia.append(Paragraph(producto.producto_nombre + " - Nº ID : " + str(producto.idd) + " - Solo quedan: " + str(
            producto.producto_stock), div_productos))
        guia.append(Spacer(0, 10))
    doc = SimpleDocTemplate("StockBajo.pdf", pagesize=A4, showBoundary=0)
    doc.build(guia)
