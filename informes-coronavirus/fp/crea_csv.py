# Barto 28 d emayo de 2020

# COSAS QUE FALTAN:

from os import listdir, mkdir, remove, removedirs, rmdir

# from string import replace, find, rfind
from shutil import copy2
import glob, sys, zipfile, os, os.path, time
import xml.etree.ElementTree as ET


def borra_directorio(path):
    files = os.listdir(path)
    for x in files:
        fullpath = path + "/" + x
        if os.path.isfile(fullpath):
            os.remove(fullpath)
        elif os.path.isdir(fullpath):
            borra_directorio(fullpath)
    if os.path.isdir(path):
        os.rmdir(path)


def descomprime(ruta, fichero):

    file_path = ruta + fichero
    directorio = ruta + "/tmp"

    print("Descomprimo ", fichero)

    # borra directorio temporal si existe
    if os.path.isdir(directorio):
        borra_directorio(directorio)

    # descomprime plantilla sxd en directorio temporal
    os.mkdir(directorio, 0o777)
    zfobj = zipfile.ZipFile(file_path)
    for name in zfobj.namelist():
        rd = zfobj.getinfo(name)
        time_list = list(rd.date_time) + [0, 0, -1]
        time_value = time.mktime(tuple(time_list))
        pathname = os.path.join(directorio, name)
        if name.endswith("/"):
            os.makedirs(os.path.join(directorio, name))
        else:
            try:
                (path, nombre) = os.path.split(os.path.join(directorio, name))
                os.makedirs(path)
            except:
                pass
            name2 = name
            # print(name2)
            #            name2 = replace (name2, "ú", "\xb7")
            #            pathname2 = replace (pathname, "ú", "\xb7")
            pathname2 = pathname
            outfile = open(os.path.join(directorio, name2), "wb")
            outfile.write(zfobj.read(name))
            os.utime(pathname2, (time_value, time_value))
            outfile.close()
    zfobj.close()


def sustituye(ruta, fichero):
    archivo_a_sustituir = ruta + fichero
    entrada = open(archivo_a_sustituir, encoding="utf8")
    pagina = entrada.read()
    entrada.close()

    pagina = pagina.replace("<text:s/>", "")
    salida = open(archivo_a_sustituir, "w", encoding="utf8")
    salida.write(pagina)
    salida.close()


def muestra_valores(ruta, fichero):
    file_path = ruta + fichero
    tree = ET.parse(file_path)
    root = tree.getroot()

    # print(root[0])
    for child in root[3][0][1]:
        # print(child.tag, child.attrib)
        for child2 in child:
            # print("  ", child2)
            for child3 in child2:
                print(child3.text, end=",")
        print()


def escribe_csv(ruta, fichero_xml, fichero_csv):
    file_path = ruta + fichero_xml

    salida = open(fichero_csv, "w", encoding="utf-8")
    tree = ET.parse(file_path)
    root = tree.getroot()

    # print(root[0])
    for child in root[3][0][1]:
        # print(child.tag, child.attrib)
        datos = False
        for child2 in child:
            # print("  ", child2)
            for child3 in child2:
                salida.write(f"{child3.text},")
                datos = True
        if datos:
            salida.write("\n")
    salida.close()


# AQUí EMPIEZA EL PROGRAMA

ruta_hoja = "D:/_Carpetas_frecuentes/Documentos/Clase/19-20 Abastos/19-20 Coronavirus/informes/fp/"
ruta_xml = ruta_hoja + "tmp/"

hoja = "datos.ods"
content_xml = "content.xml"
csv = "datos.csv"

descomprime(ruta_hoja, hoja)
sustituye(ruta_xml, content_xml)
muestra_valores(ruta_xml, content_xml)
escribe_csv(ruta_xml, content_xml, csv)
print("Programa terminado. Pulsa una tecla")
