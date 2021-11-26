# 01/06/2020
# A partir de datos.csv genera los pdfs
# En vez de canvas podría usar esto http://reportlab4.rssing.com/chan-13611823/all_p1.html
# El apartado Going with the Flow
# Otra cosa para averiguar sería si es posible quitar los campo de formulario. No he encontrado nada
# igual aquí dicen algo https://stackoverflow.com/questions/27023043/generate-flattened-pdf-with-python
# otra biblioteca para mirar https://github.com/pymupdf/PyMuPDF-Utilities

import csv
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth

CAMPOS_REPETIDOS = 10
FUENTE_TIPO = "Helvetica"
FUENTE_SIZE = 8

campos_a_agrupar = [
    "Cualificación",
    "Valoración del grupo",
    "Valoración individual",
    "Otros",
]

campos_a_eliminar = [
    "A. Datos del centro",
    "B. Datos grupo",
    "G. Fecha y firma",
    "E1. Valoración del grupo",
    "B. Datos del alumno",
    "C. Datos académicos",
    "D. Cualificaciones",
    "E. Módulos de primer curso",
    "F. Otros datos de interés",
]

pos_fp = {
    "Código de centro": [0, 65, 582],
    "Nombre de centro": [0, 190, 582],
    "Titularidad pública": [0, 462, 585],
    "Localidad": [0, 65, 562],
    "Provincia": [0, 190, 562],
    "Teléfono": [0, 400, 562],
    "Dirección": [0, 65, 541],
    "CP": [0, 400, 541],
    "NIA": [0, 65, 497],
    "Curso": [0, 150, 497],
    "Apellidos y Nombre": [0, 205, 497],
    "Ciclo Formativo": [0, 65, 466],
    "Grado": [0, 65, 435],
    "Desarrollo general satisfactorio": [0, 500, 320],
    "Desarrollo general suficiente": [0, 500, 299],
    "Desarrollo general posible": [0, 500, 278],
    "Desarrollo general no conseguido": [0, 500, 257],
    "Competencia avanzada": [0, 121, 217],
    "Competencia media": [0, 230, 217],
    "Competencia básica": [0, 339, 217],
    "Competencia ausente": [0, 448, 217],
    "Cualificación": [0, 70, 135, 450],
    "Valoración del grupo": [1, 70, 695, 450],
    "Valoración individual": [1, 70, 580, 450],
    "Otros": [1, 70, 450, 450],
    "Lugar": [1, 205, 219],
    "Día": [1, 281, 219],
    "Mes": [1, 310, 219],
    "Tutor": [1, 130, 172],
}


def devuelve_elemento(lista, posicion, valor):
    for elemento in lista:
        if elemento[posicion] == valor:
            return elemento
    return []


def elimina_elemento(lista, posicion, valor):
    for indice in range(len(lista) - 1, -1, -1):
        if lista[indice][posicion] == valor:
            del lista[indice]
    return lista


def divide_cadena(origen, maximo):
    t = origen.split(" ")
    check = True
    for palabra in t:
        if len(palabra) > maximo:
            raise Exception(
                f'Problema: "{palabra}" es demasiado larga para ancho de línea {maximo}'
            )
    if check:
        t2 = []
        while len(t) > 0:
            u = ""
            while (
                len(t) > 0
                and stringWidth(u, FUENTE_TIPO, FUENTE_SIZE)
                + stringWidth(t[0], FUENTE_TIPO, FUENTE_SIZE)
                <= maximo
            ):
                u += t[0] + " "
                del t[0]
            t2 += [u]
        return t2


with open("datos.csv", encoding="utf-8", newline="") as csvfile:
    data = list(csv.reader(csvfile, delimiter=",", quotechar='"'))

for i in campos_a_eliminar:
    data = elimina_elemento(data, 0, i)

alumnos = len(devuelve_elemento(data, 0, "NIA")) - 1

for campo in campos_a_agrupar:
    campos_unidos = [campo]
    for i in range(CAMPOS_REPETIDOS):
        nombre_campo = campo + f" {i+1}"
        campo_a_unir = devuelve_elemento(data, 0, nombre_campo)
        for j in range(1, len(campo_a_unir)):
            if campo_a_unir[j] != "":
                if j > len(campos_unidos) - 1:
                    campos_unidos += [campo_a_unir[j]]
                else:
                    campos_unidos[j] += f". {campo_a_unir[j]}"

    while len(campos_unidos) < alumnos + 1:
        campos_unidos += [""]
    data += [campos_unidos]

    for i in range(CAMPOS_REPETIDOS):
        nombre_campo = campo + f" {i+1}"
        data = elimina_elemento(data, 0, nombre_campo)

alumnos = devuelve_elemento(data, 0, "NIA")
for alumno in range(1, len(alumnos)):
    # read your existing PDF
    existing_pdf = PdfFileReader(open("fp_informe_original.pdf", "rb"))
    output = PdfFileWriter()
    outputStream = open(f"{alumnos[alumno]}.pdf", "wb")
    # add the "watermark" (which is the new pdf) on the existing page
    for page_num in range(existing_pdf.getNumPages()):
        page = existing_pdf.getPage(page_num)

        # create a new PDF with Reportlab
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont(FUENTE_TIPO, FUENTE_SIZE)  # choose your font type and font size
        # can.drawString(100, 100, "____")
        # can.drawString(200, 500, "____")
        for i in data:
            if i[0] in pos_fp and pos_fp[i[0]][0] == page_num:
                if i[alumno] == "":
                    can.drawString(pos_fp[i[0]][1], pos_fp[i[0]][2], i[1])
                elif len(pos_fp[i[0]]) > 3:
                    s = i[alumno]
                    # print(stringWidth(i[alumno], FUENTE_TIPO, FUENTE_SIZE))
                    s2 = divide_cadena(s, pos_fp[i[0]][3])
                    for trozo in range(len(s2)):
                        can.drawString(
                            pos_fp[i[0]][1],
                            pos_fp[i[0]][2] - trozo * FUENTE_SIZE * 1.25,
                            s2[trozo],
                        )
                else:
                    can.drawString(pos_fp[i[0]][1], pos_fp[i[0]][2], i[alumno])
        can.save()
        # move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)

        page2 = new_pdf.getPage(0)
        page.mergePage(page2)
        output.addPage(page)
        # finally, write "output" to a real file
        output.write(outputStream)
    outputStream.close()
