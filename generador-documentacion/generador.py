# Barto 25 de febrero de 2018
# Este programa convierte las tablas exportadas de Access en bonitas páginas Web

# Nota: Al poner la fecha de modificaciones y novedades hay que poner el día siguiente
# de la última recopilación, para que no salga un programa incluido el último día.

# COSAS POR HACER

import json, pathlib, shutil, imagesize


PAGINAS = "paginas.json"
ELEMENTOS = "elementos.json"
ORIGEN = "sitio-plantilla"
DESTINO = "sitio"
REMOTO_ARCHIVOS = "http://www.mclibre.org/descargar/docs/"
LOCAL_ARCHIVOS = (
    "D:\\Barto\\Documentación software libre\\revistas\\__revistas_en_mclibre\\"
)
LOCAL_MINIATURAS = (
    "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\documentacion\\img\\"
)
MES = [
    "",
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


def nombre_plantilla_a_nombre_revista(plantilla):
    for i in paginas_json["paginas"]:
        # print(f"{plantilla} - {i['nombre']}")
        if plantilla == i["nombre"]:
            return i
    return "ERROR"


def ordena(lista, clave, reverse=False):
    # Ordena una lista de diccionarios por valores crecientes de una clave
    cambios = True
    while cambios:
        cambios = False
        for i in range(len(lista) - 1):
            if reverse:
                if lista[i][clave] < lista[i + 1][clave]:
                    cambios = True
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
            else:
                if lista[i][clave] > lista[i + 1][clave]:
                    cambios = True
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def crea_bloque_revista_anyos(plantilla):
    ejemplares = []
    anyos = []
    # Obtiene ejemplares
    r = nombre_plantilla_a_nombre_revista(plantilla)
    for i in elementos_json["revistas"]:
        if i["nombre"] == r["revista"]:
            ejemplares += [i]
            if i["año"] not in anyos:
                anyos += [i["año"]]
    anyos.sort(reverse=True)

    # Genera html
    t = ''
    t += '<!DOCTYPE html>\n'
    t += '<html lang="es">\n'
    t += '<head>\n'
    t += '  <meta charset="utf-8" />\n'
    t += f'  <title>Revista {r["revista"]}. Documentación sobre software libre. Bartolomé Sintes Marco. www.mclibre.org</title>'
    t += '\n'
    t += '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
    t += '  <link rel="stylesheet" type="text/css" href="../varios/documentos.css" title="mclibre" />\n'
    t += '  <link rel="icon" href="../varios/favicon.ico" />\n'
    t += '</head>\n'
    t += '\n'
    t += '<body>\n'
    t += f'  <h1>Revista {r["revista"]}</h1>'
    t += '\n'
    t += '\n'
    t += '  <nav>\n'
    t += '    <p>\n'
    t += '      <a href="../index.html"><img src="../varios/cc.png" alt="Volver a la página principal" title="Volver a la página principal" height="64" width="64" /></a>\n'
    t += '      <a href="#"><img src="../varios/iconos/icono_arrow_circle_up.svg" alt="Principio de la página" title="Principio de la página" width="36" height="36" /></a>\n'
    t += '    </p>\n'
    t += '\n'
    t += f'    <h2>{r["revista"]}</h2>'
    t += '\n'
    t += '\n'
    t += '    <div class="toc">\n'
    t += '      <ul>\n'
    for i in anyos:
        t += f'        <li><a href="#y{i}">{i}</a></li>'
        t += '\n'
    t += '      </ul>\n'
    t += '    </div>\n'
    t += '  </nav>\n'
    t += '\n'
    t += f'  <p>Esta página contiene enlaces a los números publicados de la revista <strong>{r["revista"]}</strong> en '
    for i in range(len(anyos)-1):
        t += f'<a href="#y{anyos[i]}">{anyos[i]}</a> - '
    t += f'<a href="#y{anyos[-1]}">{anyos[-1]}</a>.</p>'
    t += '\n'
    t += '\n'
    t += f'  <p>Página web: <a href="{r["web"]}">{r["revista"]}</a></p>'
    t += '\n'
    t += '\n'
    for a in anyos:
        ejemplares_year = []
        for i in ejemplares:
            if i["año"] == a:
                ejemplares_year += [i]
        ejemplares_year = ordena(ejemplares_year, "número", reverse=True)

        t += f'  <section id="y{a}">'
        t += '\n'
        t += f"    <h2>{a}</h2>"
        t += '\n'
        t += '\n'
        t += '    <div class="miniaturas">\n'
        for i in ejemplares_year:
            width, height = imagesize.get(
                LOCAL_MINIATURAS + r["miniaturas"] + i["portada"]
            )
            fichero = pathlib.Path(LOCAL_ARCHIVOS + r["archivos"] + i["fichero"])
            weight = str(round(fichero.stat().st_size / 1024 / 1024, 1)) + " MB"
            formato = fichero.suffix[1:].upper()
            t += '      <div>\n'
            t += f'        <p><img alt="Revista {i["nombre"]} nº {i["número"]} - {i["año"]}-{i["mes"]:02d}" src="{r["miniaturas"]}{i["portada"]}" width="{width}" height="{height}" /></p>'
            t += '\n'
            t += f'        <p>Número {i["número"]} - {i["año"]} {MES[i["mes"]]}</p>'
            t += '\n'
            t += f'        <p><a href="{REMOTO_ARCHIVOS +r["archivos"]+i["fichero"]}">Descarga</a> ({formato} {weight} {i["idioma"]})</p>'
            t += '\n'
            t += '      </div>\n'
        t += '    </div>\n'
        t += '  </section>\n'
        t += '\n'
    t += '  <address id="ultmod">\n'
    t += '    Autor: Bartolomé Sintes Marco<br /> Última modificación de esta página: 1 de mayo de 2019\n'
    t += '  </address>\n'
    t += '</body>\n'
    t += '</html>\n'
    return t


print("GENERADOR DE SITIO WEB")

# Comprueba que DESTINO no existe y lo borra si existe
p = pathlib.Path(DESTINO)
if p.exists():
    print()
    print("El directorio de destino ya existe.")
    print("El directorio de destino se borrará completamente.")
    respuesta = input("Confirme que desea crearlo de nuevo (S): ")
    if respuesta != "S":
        print("El sitio no se ha creado.")
        exit(0)
    else:
        shutil.rmtree(p)

# Carga elementos y páginas
with open(ELEMENTOS, encoding="utf-8") as json_file:
    elementos_json = json.load(json_file)

with open(PAGINAS, encoding="utf-8") as json_file:
    paginas_json = json.load(json_file)

# Crea directorios de DESTINO
print("Creando directorios de destino")
for i in pathlib.Path(ORIGEN).rglob(f"*"):
    directorio = str(i.parent)
    directorio = directorio.replace(ORIGEN, DESTINO)
    p = pathlib.Path(directorio)
    if not p.exists():
        print(f"  {directorio}")
        p.mkdir(parents=True, exist_ok=True)
print("Directorios creados.")
print()

paginas = []
for i in paginas_json["paginas"]:
    paginas += [i["nombre"]]
# print(paginas)

# Crea ficheros
print("Creando ficheros de destino")
for i in pathlib.Path(ORIGEN).rglob(f"*/*"):
    fichero_origen = str(i)
    if i.name not in paginas:
        print(f"El fichero no existe en la plantilla del sitio: {fichero_origen}")
    else:
        fichero_destino = fichero_origen.replace(ORIGEN, DESTINO)
        print(fichero_destino)
        with open(fichero_destino, "w", encoding="utf-8") as fichero:
            fichero.write(crea_bloque_revista_anyos(i.name))