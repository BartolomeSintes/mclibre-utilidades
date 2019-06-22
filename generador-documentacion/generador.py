# Barto 25 de febrero de 2018
# Este programa convierte las tablas exportadas de Access en bonitas páginas Web

# Nota: Al poner la fecha de modificaciones y novedades hay que poner el día siguiente
# de la última recopilación, para que no salga un programa incluido el último día.

# COSAS POR HACER

import json, pathlib, shutil, imagesize, operator


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
# LOCAL_ARCHIVOS = (
#     "C:\\Users\\ASIR 7L\\Documents\\IAW\\apuntes\\__revistas_en_mclibre\\"
# )

# LOCAL_MINIATURAS = (
#     "C:\\Users\\ASIR 7L\\Documents\\IAW\\apuntes\\documentacion\\img\\"
# )
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
        if plantilla == i["pagina"]:
            return i
    return "ERROR"


def ordena(lista, reverse=False):
    # Ordena una lista de diccionarios por año > mes > nombre revista > número
    # La comparación es complicada porque meses y números pueden ser int o str
    cambios = True
    while cambios:
        cambios = False
        for i in range(len(lista) - 1):
            if reverse:
                if (
                    # si el año es menor
                    lista[i]["año"] < lista[i + 1]["año"]
                    # si los meses son números compara como números
                    or (lista[i]["año"] == lista[i + 1]["año"]
                    and (
                        isinstance(lista[i]["mes"], int)
                        and isinstance(lista[i+1]["mes"], int)
                    )
                    and lista[i]["mes"] < lista[i + 1]["mes"])
                    # si los meses no son números compara como cadenas
                    or (lista[i]["año"] == lista[i + 1]["año"]
                    and (
                        not isinstance(lista[i]["mes"], int)
                        or not isinstance(lista[i+1]["mes"], int)
                    )
                    and str(lista[i]["mes"]) < str(lista[i + 1]["mes"]))
                    # si el nombre de la revista es menor (para recopilaciones)
                    or (lista[i]["año"] == lista[i + 1]["año"]
                    and str(lista[i]["mes"]) == str(lista[i + 1]["mes"])
                    and lista[i]["nombre"] < lista[i + 1]["nombre"])
                    # si los números de revista son números compara como números
                    or (lista[i]["año"] == lista[i + 1]["año"]
                    and str(lista[i]["mes"]) == str(lista[i + 1]["mes"])
                    and lista[i]["nombre"] == lista[i + 1]["nombre"]and (
                        isinstance(lista[i]["número"], int)
                        and isinstance(lista[i+1]["número"], int)
                    )
                    and lista[i]["número"] < lista[i + 1]["número"])
                    # si los números de revista no son números compara como cadenas
                    or (lista[i]["año"] == lista[i + 1]["año"]
                    and str(lista[i]["mes"]) == str(lista[i + 1]["mes"])
                    and lista[i]["nombre"] == lista[i + 1]["nombre"]and (
                        not isinstance(lista[i]["número"], int)
                        or not isinstance(lista[i+1]["número"], int)
                    )
                    and str(lista[i]["número"]) < str(lista[i + 1]["número"]))
                ):
                    cambios = True
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    # print("cambiados")
            else:
                if (
                    lista[i]["año"] > lista[i + 1]["año"]
                    or lista[i]["año"] == lista[i + 1]["año"]
                    and str(lista[i]["número"]) > str(lista[i + 1]["número"])
                ):
                    cambios = True
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


def meses(numero):
    if numero == "":
        return ""
    elif str(numero).isnumeric() and 1 <= numero and numero <= 12:
        return MES[numero]
    elif numero == "S1":
        return "Primer semestre"
    elif numero == "S2":
        return "Segundo semestre"
    else:
        return "ERROR"


def crea_bloque_revista_anyos(plantilla):
    ejemplares = []
    anyos = []
    # Obtiene ejemplares
    r = nombre_plantilla_a_nombre_revista(plantilla)
    for i in elementos_json["revistas"]:
        if i["nombre"] == r["nombre-corto"] or ("serie" in i and i["serie"] == r["nombre-corto"]):
            ejemplares += [i]
            if i["año"] not in anyos:
                anyos += [i["año"]]
    anyos.sort(reverse=True)
    # Genera html
    t = ""
    t += "<!DOCTYPE html>\n"
    t += '<html lang="es">\n'
    t += "<head>\n"
    t += '  <meta charset="utf-8">\n'
    t += f'  <title>Revista {r["nombre"]}. Documentación sobre software libre. Bartolomé Sintes Marco. www.mclibre.org</title>'
    t += "\n"
    t += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    t += '  <link rel="stylesheet" type="text/css" href="../varios/documentos.css" title="mclibre">\n'
    t += '  <link rel="icon" href="../varios/favicon.ico">\n'
    t += "</head>\n"
    t += "\n"
    t += "<body>\n"
    t += f'  <h1>Revista {r["nombre"]}</h1>'
    t += "\n"
    t += "\n"
    t += "  <nav>\n"
    t += "    <p>\n"
    t += '      <a href="../index.html"><img src="../varios/cc.png" alt="Volver a la página principal" title="Volver a la página principal" height="64" width="64"></a>\n'
    t += '      <a href="#"><img src="../varios/iconos/icono-arrow-circle-up.svg" alt="Principio de la página" title="Principio de la página" width="36" height="36"></a>\n'
    t += "    </p>\n"
    t += "\n"
    t += f'    <h2>{r["nombre-corto"]}</h2>'
    t += "\n"
    t += "\n"
    t += '    <div class="toc">\n'
    t += "      <ul>\n"
    for i in anyos:
        t += f'        <li><a href="#y{i}">{i}</a></li>'
        t += "\n"
    t += "      </ul>\n"
    t += "    </div>\n"
    t += "  </nav>\n"
    t += "\n"
    t += f'  <p>Esta página contiene enlaces a los números publicados de la revista <strong>{r["nombre"]}</strong> en '
    for i in range(len(anyos) - 1):
        t += f'<a href="#y{anyos[i]}">{anyos[i]}</a> - '
    t += f'<a href="#y{anyos[-1]}">{anyos[-1]}</a>.</p>'
    t += "\n"
    t += "\n"
    t += f'    <h2>{r["nombre"]}</h2>'
    t += "\n"
    t += "\n"
    t += f'  <p>Página web: '
    t += f'<a href="{r["web"][0][0]}">{r["web"][0][1]}</a>'
    for i in range(len(r["web"]) - 1):
        t += f' - <a href="{r["web"][i+1][0]}">{r["web"][i+1][1]}</a>'
    t += f'</p>'
    t += "\n"
    t += "\n"
    for a in anyos:
        ejemplares_year = []
        for i in ejemplares:
            if i["año"] == a:
                ejemplares_year += [i]
        ejemplares_year = ordena(ejemplares_year, reverse=True)
        # ejemplares_year = sorted(ejemplares_year, key=operator.attrgetter('año', 'mes'), reverse=True)
        # no me aclaro con sorted, dice que no hay atributo año

        t += f'  <section id="y{a}">'
        t += "\n"
        t += f"    <h2>{a}</h2>"
        t += "\n"
        t += "\n"
        t += '    <div class="miniaturas">\n'
        for i in ejemplares_year:
            width, height = imagesize.get(
                LOCAL_MINIATURAS + r["miniaturas"] + i["portada"]
            )
            fichero = pathlib.Path(LOCAL_ARCHIVOS + r["archivos"] + i["fichero"])
            weight = str(round(fichero.stat().st_size / 1024 / 1024, 1)) + " MB"
            formato = fichero.suffix[1:].upper()
            t += "      <div>\n"
            if isinstance(i["mes"], int):
                t += f'        <p><img alt="Revista {i["nombre"]} nº {i["número"]} - {i["año"]}-{i["mes"]:02d}" src="{r["miniaturas"]}{i["portada"]}" width="{width}" height="{height}"></p>'
            else:
                t += f'        <p><img alt="Revista {i["nombre"]} nº {i["número"]} - {i["año"]}-{i["mes"]}" src="{r["miniaturas"]}{i["portada"]}" width="{width}" height="{height}"></p>'
            t += "\n"
            t += f'        <p>Número {i["número"]} - {i["año"]} {meses(i["mes"])}</p>'
            t += "\n"
            t += f'        <p><a href="{REMOTO_ARCHIVOS +r["archivos"]+i["fichero"]}">Descarga</a> ({formato} {weight} {i["idioma"]})</p>'
            t += "\n"
            t += "      </div>\n"
        t += "    </div>\n"
        t += "  </section>\n"
        t += "\n"
    t += '  <address id="ultmod">\n'
    t += "    Autor: Bartolomé Sintes Marco<br>\n"
    t += "    Última modificación de esta página: 1 de mayo de 2019\n"
    t += "  </address>\n"
    t += "</body>\n"
    t += "</html>\n"
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
    paginas += [i["pagina"]]
# print(paginas)

# Crea ficheros
print("Creando ficheros de destino")
for i in pathlib.Path(ORIGEN).rglob(f"*/*"):
    fichero_origen = str(i)
    if i.name not in paginas:
        print(
            f"El fichero no existe en la plantilla del sitio: {fichero_origen} {i.name}"
        )
    else:
        fichero_destino = fichero_origen.replace(ORIGEN, DESTINO)
        print(fichero_destino)
        with open(fichero_destino, "w", encoding="utf-8") as fichero:
            fichero.write(crea_bloque_revista_anyos(i.name))
