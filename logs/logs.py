import json, math, pathlib, re
from collections import defaultdict
from datetime import date, datetime
from calendar import monthrange

# para ejecutar esta aplicación,
# escriba en MCL_0 la raíz de los ficheros a analizar
# y ejecute la orden py diccionario.py

MCL_0 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-0"
MCL_1 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-1"
MCL_2 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-2"
# usar \\ en vez de / porque pathlib usa \ y no funciona replace

FICHERO_ESTADISTICAS = "estadisticas.html"
FICHERO_VISITAS = "json/visitas.json"
FICHERO_VISITAS_TODAS = "json/visitas-todas.json"

PROFES = [
    "amaliaalbero",
    "antoniojosefernandez",
    "cristinasanfrancisco",
    "daniel_tomas",
]
EJEMPLOS = ["css/ejemplos", "html/ejemplos", "/python/python/"]
LIMPIA = [
    "/ HTTP",
    "/primaria",
    ".html",
    ".xhtml",
    ".pdf",
    ".php",
    ".xml",
    ".xsl",
    ".py",
    ".txt",
    ".rtf",
    ".odt",
    ".odp",
    ".ods",
    ".sxi",
    ".swf",
    ".mp3",
    ".mp4",
    ".exe",
    ".zip",
    ".rar",
    ".7z",
    ".gz",
    ".tgz",
    ".iso",
    ".ova",
]
IMG = [".jpg", ".png", ".svg", ".gif", ".webp", ".ico", ".cur"]
OTROS = [".css", ".js", ".woff", ".otf", ".ttf", ".po", ".eot"]
APUNTES = [
    "consultar/amaya",
    "consultar/documentacion",
    "consultar/google",
    "consultar/htmlcss",
    "consultar/informatica",
    "consultar/legislacion",
    "consultar/linux",
    "consultar/php",
    "consultar/primaria",
    "consultar/python",
    "consultar/webapps",
    "consultar/xml",
]
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


def fecha_a_texto(numero):
    return (
        str(int(numero[8:10]))
        + " de "
        + MES[int(numero[5:7])]
        + " de "
        + str(numero[0:4])
    )


def mclibre_limpia_logs():
    print("Limpia logs")
    # Se queda con las líneas 200 GET que contienen las cadenas que hay en LIMPIA[]
    for source_file in pathlib.Path(MCL_0).rglob(f"**/transfer*"):
        print(source_file)

        file_ataques = str(source_file).replace(MCL_0, MCL_1 + "\\ataques") + ".ataques"
        file_profes = str(source_file).replace(MCL_0, MCL_1 + "\\profes") + ".profes"
        file_ejemplos = (
            str(source_file).replace(MCL_0, MCL_1 + "\\clean-ejemplos")
            + ".clean-ejemplos"
        )
        file_clean = str(source_file).replace(MCL_0, MCL_1 + "\\clean") + ".clean"
        file_img = str(source_file).replace(MCL_0, MCL_1 + "\\img") + ".img"
        file_ok = str(source_file).replace(MCL_0, MCL_1 + "\\ok") + ".ok"
        file_otros = str(source_file).replace(MCL_0, MCL_1 + "\\otros") + ".otros"
        file_dirty = str(source_file).replace(MCL_0, MCL_1 + "\\dirty") + ".dirty"

        ataques = open(file_ataques, "w", encoding="utf-8")
        profes = open(file_profes, "w", encoding="utf-8")
        ejemplos = open(file_ejemplos, "w", encoding="utf-8")
        clean = open(file_clean, "w", encoding="utf-8")
        img = open(file_img, "w", encoding="utf-8")
        ok = open(file_ok, "w", encoding="utf-8")
        otros = open(file_otros, "w", encoding="utf-8")
        dirty = open(file_dirty, "w", encoding="utf-8")

        with open(source_file, "r", encoding="utf-8") as source:
            texto = source.readline()
            while texto:
                texto = source.readline()
                # print(texto)
                guardado = False
                if "GET /?" in texto or "GET //?" in texto:
                    print(texto, end="", file=ataques)
                    guardado = True
                if not (guardado):
                    if (
                        (" /otros/" in texto or " //otros/" in texto)
                        and " 200 " in texto
                        and "GET" in texto
                    ):
                        print(texto, end="", file=profes)
                        guardado = True
                if not (guardado):
                    for i in PROFES:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=profes)
                            guardado = True
                if not (guardado):
                    for i in EJEMPLOS:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=ejemplos)
                            guardado = True
                if not (guardado):
                    for i in IMG:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=img)
                            guardado = True
                if not (guardado):
                    for i in OTROS:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=otros)
                            guardado = True
                if not (guardado):
                    for i in LIMPIA:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=clean)
                            guardado = True
                if not (guardado):
                    if " 200 " in texto and "GET" in texto:
                        print(texto, end="", file=ok)
                        guardado = True
                if not (guardado):
                    print(texto, end="", file=dirty)

        ataques.close()
        profes.close()
        ejemplos.close()
        img.close()
        ok.close()
        otros.close()
        dirty.close()


def mclibre_divide_logs_apuntes():
    print("Divide logs de cada grupo de apuntes")
    for source_file in pathlib.Path(MCL_0).rglob(f"**/*"):
        print(source_file)

        file_apicv = (
            str(source_file).replace(MCL_0, MCL_2 + "\\apicv-recursos")
            + ".apicv-recursos"
        )
        file_basura = str(source_file).replace(MCL_0, MCL_2 + "\\basura") + ".basura"
        file_charlas = str(source_file).replace(MCL_0, MCL_2 + "\\charlas") + ".charlas"
        file_descargas = (
            str(source_file).replace(MCL_0, MCL_2 + "\\descargas") + ".descargas"
        )
        file_docs = str(source_file).replace(MCL_0, MCL_2 + "\\docs") + ".docs"
        file_edubuntu = (
            str(source_file).replace(MCL_0, MCL_2 + "\\edubuntu") + ".edubuntu"
        )
        file_especiales = (
            str(source_file).replace(MCL_0, MCL_2 + "\\especiales") + ".especiales"
        )
        file_examenes = (
            str(source_file).replace(MCL_0, MCL_2 + "\\examenes") + ".examenes"
        )
        file_google = str(source_file).replace(MCL_0, MCL_2 + "\\google") + ".google"
        file_homepage = (
            str(source_file).replace(MCL_0, MCL_2 + "\\homepage") + ".homepage"
        )
        file_htmlcss = str(source_file).replace(MCL_0, MCL_2 + "\\htmlcss") + ".htmlcss"
        file_iaig = (
            str(source_file).replace(MCL_0, MCL_2 + "\\iaig-pendientes")
            + ".iaig-pendientes"
        )
        file_informatica = (
            str(source_file).replace(MCL_0, MCL_2 + "\\informatica") + ".informatica"
        )
        file_instalar = (
            str(source_file).replace(MCL_0, MCL_2 + "\\instalar-software")
            + ".instalar-software"
        )
        file_internet = (
            str(source_file).replace(MCL_0, MCL_2 + "\\internet") + ".internet"
        )
        file_legislacion = (
            str(source_file).replace(MCL_0, MCL_2 + "\\legislacion") + ".legislacion"
        )
        file_linux = str(source_file).replace(MCL_0, MCL_2 + "\\linux") + ".linux"
        file_musica = str(source_file).replace(MCL_0, MCL_2 + "\\musica") + ".musica"
        file_pau = str(source_file).replace(MCL_0, MCL_2 + "\\pau") + ".pau"
        file_php = str(source_file).replace(MCL_0, MCL_2 + "\\php") + ".php"
        file_php2 = str(source_file).replace(MCL_0, MCL_2 + "\\php-php") + ".php-php"
        file_primaria = (
            str(source_file).replace(MCL_0, MCL_2 + "\\primaria") + ".primaria"
        )
        file_python = str(source_file).replace(MCL_0, MCL_2 + "\\python") + ".python"
        file_sqlite = str(source_file).replace(MCL_0, MCL_2 + "\\sqlite") + ".sqlite"
        file_tests = str(source_file).replace(MCL_0, MCL_2 + "\\tests") + ".tests"
        file_videos = str(source_file).replace(MCL_0, MCL_2 + "\\videos") + ".videos"
        file_webapps = str(source_file).replace(MCL_0, MCL_2 + "\\webapps") + ".webapps"
        file_xml = str(source_file).replace(MCL_0, MCL_2 + "\\xml") + ".xml"
        file_restos = str(source_file).replace(MCL_0, MCL_2 + "\\restos") + ".restos"

        apicv = open(file_apicv, "w", encoding="utf-8")
        basura = open(file_basura, "w", encoding="utf-8")
        charlas = open(file_charlas, "w", encoding="utf-8")
        docs = open(file_docs, "w", encoding="utf-8")
        descargas = open(file_descargas, "w", encoding="utf-8")
        edubuntu = open(file_edubuntu, "w", encoding="utf-8")
        especiales = open(file_especiales, "w", encoding="utf-8")
        examenes = open(file_examenes, "w", encoding="utf-8")
        google = open(file_google, "w", encoding="utf-8")
        homepage = open(file_homepage, "w", encoding="utf-8")
        htmlcss = open(file_htmlcss, "w", encoding="utf-8")
        iaig = open(file_iaig, "w", encoding="utf-8")
        informatica = open(file_informatica, "w", encoding="utf-8")
        internet = open(file_internet, "w", encoding="utf-8")
        instalar = open(file_instalar, "w", encoding="utf-8")
        legislacion = open(file_legislacion, "w", encoding="utf-8")
        linux = open(file_linux, "w", encoding="utf-8")
        musica = open(file_musica, "w", encoding="utf-8")
        pau = open(file_pau, "w", encoding="utf-8")
        php = open(file_php, "w", encoding="utf-8")
        php2 = open(file_php2, "w", encoding="utf-8")
        primaria = open(file_primaria, "w", encoding="utf-8")
        python = open(file_python, "w", encoding="utf-8")
        sqlite = open(file_sqlite, "w", encoding="utf-8")
        tests = open(file_tests, "w", encoding="utf-8")
        videos = open(file_videos, "w", encoding="utf-8")
        webapps = open(file_webapps, "w", encoding="utf-8")
        xml = open(file_xml, "w", encoding="utf-8")
        restos = open(file_restos, "w", encoding="utf-8")
        with open(source_file, "r", encoding="utf-8") as source:
            texto = source.readline()
            while texto:
                texto = source.readline()
                # print(texto)
                if (
                    "GET / " in texto
                    or "GET // " in texto
                    or " /index.html" in texto
                    or " /consultar.html " in texto
                    or " /descargar.html " in texto
                    or " /novedades.html " in texto
                    or " /participar.html " in texto
                    or "http://www.mclibre.org/ " in texto
                    or "http://mclibre.org/ " in texto
                ):
                    print(texto, end="", file=homepage)
                elif "consultar/amaya" in texto or "consultar//amaya" in texto:
                    print(texto, end="", file=htmlcss)
                elif "consultar/apicv" in texto or "consultar//apicv" in texto:
                    print(texto, end="", file=apicv)
                elif "consultar/charlas" in texto or "consultar//charlas" in texto:
                    print(texto, end="", file=charlas)
                elif "descargar/" in texto:
                    print(texto, end="", file=descargas)
                elif (
                    "consultar/documentacion" in texto
                    or "consultar//documentacion" in texto
                ):
                    print(texto, end="", file=docs)
                elif "consultar/edubuntu" in texto or "consultar//edubuntu" in texto:
                    print(texto, end="", file=edubuntu)
                elif (
                    "consultar/especiales" in texto or "consultar//especiales" in texto
                ):
                    print(texto, end="", file=especiales)
                elif "consultar/examenes" in texto or "consultar//examenes" in texto:
                    print(texto, end="", file=examenes)
                elif "consultar/google" in texto or "consultar//google" in texto:
                    print(texto, end="", file=google)
                elif "consultar/htmlcss" in texto or "consultar//htmlcss" in texto:
                    print(texto, end="", file=htmlcss)
                elif "consultar/iaig" in texto or "consultar//iaig" in texto:
                    print(texto, end="", file=iaig)
                elif (
                    "consultar/informatica" in texto
                    or "consultar//informatica" in texto
                ):
                    print(texto, end="", file=informatica)
                elif "consultar/instalar" in texto or "consultar//instalar" in texto:
                    print(texto, end="", file=instalar)
                elif "consultar/internet" in texto or "consultar//internet" in texto:
                    print(texto, end="", file=internet)
                elif (
                    "consultar/legislacion" in texto
                    or "consultar//legislacion" in texto
                ):
                    print(texto, end="", file=legislacion)
                elif "consultar/linux" in texto or "consultar//linux" in texto:
                    print(texto, end="", file=linux)
                elif "consultar/musica" in texto or "consultar//musica" in texto:
                    print(texto, end="", file=musica)
                elif "/pau" in texto:
                    print(texto, end="", file=pau)
                elif "consultar/php" in texto or "consultar//php" in texto:
                    if ".php" in texto:
                        print(texto, end="", file=php2)
                    else:
                        print(texto, end="", file=php)
                elif "consultar/primaria" in texto or "consultar//primaria" in texto:
                    print(texto, end="", file=primaria)
                elif "consultar/python" in texto or "consultar//python" in texto:
                    print(texto, end="", file=python)
                elif " /sqlite" in texto or " //sqlite" in texto:
                    print(texto, end="", file=sqlite)
                elif "consultar/tests" in texto or "consultar//tests" in texto:
                    print(texto, end="", file=tests)
                elif "consultar/videos" in texto or "consultar//videos" in texto:
                    print(texto, end="", file=videos)
                elif "consultar/webapps" in texto or "consultar//webapps" in texto:
                    print(texto, end="", file=webapps)
                elif "consultar/xml" in texto or "consultar//xml" in texto:
                    print(texto, end="", file=xml)
                elif (
                    " /tmp" in texto
                    or " /prueba" in texto
                    or " /mozillabug_232951" in texto
                    or "/imagenes_grandes_para_clase" in texto
                    or "/google6" in texto
                    or "/google7" in texto
                ):
                    print(texto, end="", file=basura)
                else:
                    print(texto, end="", file=restos)
        apicv.close()
        basura.close()
        charlas.close()
        descargas.close()
        docs.close()
        edubuntu.close()
        especiales.close()
        examenes.close()
        google.close()
        homepage.close()
        htmlcss.close()
        iaig.close()
        informatica.close()
        instalar.close()
        internet.close()
        legislacion.close()
        linux.close()
        musica.close()
        pau.close()
        php.close()
        php2.close()
        primaria.close()
        python.close()
        sqlite.close()
        tests.close()
        videos.close()
        webapps.close()
        xml.close()
        restos.close()


def cuenta_revistas():
    print("Cuenta revistas")
    BUSCA_REVISTAS = [
        "solo-linux-01-es-201902.pdf",
        "solo-linux-02-es-201903.pdf",
        "solo-linux-03-es-201904.pdf",
        "solo-linux-04-es-201905.pdf",
        "solo-linux-05-es-201906.pdf",
        "solo-linux-06-es-201907.pdf",
        "solo-linux-07-es-201908.pdf",
    ]
    contadores = []
    for i in range(len(BUSCA_REVISTAS)):
        contadores += [0]

    for source_file in pathlib.Path(MCL_0).rglob(f"**/transfer*.clean"):
        print(source_file)
        with open(source_file, "r", encoding="utf-8") as file:
            texto = file.readline()
            while texto:
                texto = file.readline()
                for i in range(len(BUSCA_REVISTAS)):
                    if BUSCA_REVISTAS[i] in texto:
                        contadores[i] += 1

    for i in range(len(BUSCA_REVISTAS)):
        print(f"{BUSCA_REVISTAS[i]}: {contadores[i]}")


APUNTES = [
    # "prueba",
    "charlas",
    "docs",
    "htmlcss",
    "informatica",
    "legislacion",
    "php",
    "php-php",
    "primaria",
    "python",
    "webapps",
    "xml",
]
APUNTES_ESTADISTICAS = [
    # ["prueba", "Datos inventados"],
    ["htmlcss", "Páginas web HTML y hojas de estilo CSS"],
    ["python", "Introducción a la programación con Python"],
    ["php", "Programación web en PHP"],
    ["webapps", "Aplicaciones web"],
    ["informatica", "Temas de Informática"],
    ["xml", "XML: Lenguaje de Marcas Extensible"],
    # ["php-php", "Programación web en PHP [páginas PHP]"],
    ["primaria", "Ejercicios de Primaria y Secundaria"],
    ["docs", "Documentación de software libre"],
    ["legislacion", "Legislación informática"],
    ["charlas", "Charlas"],
]
ACUMULADAS = [
    # ["prueba", "Datos inventados"],
    ["informatica", "Temas de Informática"],
    ["htmlcss", "Páginas web HTML y hojas de estilo CSS"],
    ["python", "Introducción a la programación con Python"],
    ["xml", "XML: Lenguaje de Marcas Extensible"],
    ["php", "Programación web en PHP"],
    ["webapps", "Aplicaciones web"],
    # ["php-php", "Programación web en PHP [páginas PHP]"],
    # ["primaria", "Ejercicios de Primaria y Secundaria"],
    # ["docs", "Documentación de software libre"],
    # ["charlas", "Charlas"],
]
YEARS = ["2015", "2016", "2017", "2018", "2019", "2020"]
MONTHS = "EFMAMJJASOND"


def cuenta_paginas():
    print("Cuenta páginas")
    contadores = []
    for i in APUNTES:
        contadores += [0]

        for source_file in pathlib.Path(MCL_2 + "/" + i).rglob(f"**/*.*"):
            print(source_file)
            with open(source_file, "r", encoding="utf-8") as file:
                texto = file.readline()
                contadores[i] += 1
                while texto:
                    texto = file.readline()
                    contadores[i] += 1

    for i in APUNTES:
        print(f"{i}: {contadores[i]:,}")


def une_visitas_json():
    print("Une los json visitas de cada año en uno solo")
    current_year = datetime.now().year
    current_month = datetime.now().month
    visitas = defaultdict(lambda: 0)
    with open("json/visitas-vacio.json", encoding="utf-8") as json_file:
        visitas = json.load(json_file)
    for i in YEARS:
        with open("json/visitas-" + str(i) + ".json", encoding="utf-8") as json_file:
            visitas_json = json.load(json_file)
            for j in APUNTES:
                for key in list(visitas_json[j][i].keys()):
                    if i == str(current_year) and int(key) >= current_month:
                        del visitas_json[j][i][key]
                visitas[j].update(visitas_json[j])
    with open(FICHERO_VISITAS_TODAS, "w", encoding="utf-8") as json_file:
        json.dump(visitas, json_file)


def cuenta_paginas_meses(year):
    print("Cuenta páginas por meses")

    visitas = defaultdict(lambda: 0)
    for i in APUNTES:
        visitas[i] = {}
        visitas[i][str(year)] = {}
        for j in range(1, 13):
            visitas[i][str(year)][str(j)] = 0

    for i in APUNTES:
        for source_file in pathlib.Path(MCL_2 + "/" + i).rglob(f"**/*.*"):
            print(source_file)
            with open(source_file, "r", encoding="utf-8") as file:
                texto = file.readline()
                if "Jan/" + str(year) in texto:
                    visitas[i][str(year)]["1"] += 1
                elif "Feb/" + str(year) in texto:
                    visitas[i][str(year)]["2"] += 1
                elif "Mar/" + str(year) in texto:
                    visitas[i][str(year)]["3"] += 1
                elif "Apr/" + str(year) in texto:
                    visitas[i][str(year)]["4"] += 1
                elif "May/" + str(year) in texto:
                    visitas[i][str(year)]["5"] += 1
                elif "Jun/" + str(year) in texto:
                    visitas[i][str(year)]["6"] += 1
                elif "Jul/" + str(year) in texto:
                    visitas[i][str(year)]["7"] += 1
                elif "Aug/" + str(year) in texto:
                    visitas[i][str(year)]["8"] += 1
                elif "Sep/" + str(year) in texto:
                    visitas[i][str(year)]["9"] += 1
                elif "Oct/" + str(year) in texto:
                    visitas[i][str(year)]["10"] += 1
                elif "Nov/" + str(year) in texto:
                    visitas[i][str(year)]["11"] += 1
                elif "Dec/" + str(year) in texto:
                    visitas[i][str(year)]["12"] += 1
                while texto:
                    texto = file.readline()
                    if "Jan/" + str(year) in texto:
                        visitas[i][str(year)]["1"] += 1
                    elif "Feb/" + str(year) in texto:
                        visitas[i][str(year)]["2"] += 1
                    elif "Mar/" + str(year) in texto:
                        visitas[i][str(year)]["3"] += 1
                    elif "Apr/" + str(year) in texto:
                        visitas[i][str(year)]["4"] += 1
                    elif "May/" + str(year) in texto:
                        visitas[i][str(year)]["5"] += 1
                    elif "Jun/" + str(year) in texto:
                        visitas[i][str(year)]["6"] += 1
                    elif "Jul/" + str(year) in texto:
                        visitas[i][str(year)]["7"] += 1
                    elif "Aug/" + str(year) in texto:
                        visitas[i][str(year)]["8"] += 1
                    elif "Sep/" + str(year) in texto:
                        visitas[i][str(year)]["9"] += 1
                    elif "Oct/" + str(year) in texto:
                        visitas[i][str(year)]["10"] += 1
                    elif "Nov/" + str(year) in texto:
                        visitas[i][str(year)]["11"] += 1
                    elif "Dec/" + str(year) in texto:
                        visitas[i][str(year)]["12"] += 1
    print(visitas)

    with open(FICHERO_VISITAS, "w", encoding="utf-8") as json_file:
        json.dump(visitas, json_file)


def genera_estadisticas():
    with open(FICHERO_VISITAS_TODAS, encoding="utf-8") as json_file:
        estadisticas_json = json.load(json_file)
    with open(FICHERO_VISITAS_TODAS, encoding="utf-8") as json_file:
        acumuladas_json = json.load(json_file)
    # print(estadisticas_json)
    estadisticas = defaultdict(lambda: 0)

    # Genera html
    t = ""
    t += "<!DOCTYPE html>\n"
    t += '<html lang="es">\n'
    t += "<head>\n"
    t += '  <meta charset="utf-8">\n'
    t += f"  <title>Estadísticas. Bartolomé Sintes Marco. www.mclibre.org</title>\n"
    t += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    # t += '  <link rel="stylesheet" type="text/css" href="../varios/documentos.css" title="mclibre">\n'
    # t += '  <link rel="icon" href="../varios/favicon.ico">\n'
    t += "</head>\n"
    t += "\n"
    t += "<body>\n"
    t += f"  <h1>Estadísticas mclibre</h1>\n"
    t += "\n"
    t += "  <nav>\n"
    t += "    <p>\n"
    t += '      <a href="http://www.mclibre.org/"><img src="../varios/cc.png" alt="Volver a la página principal" title="Volver a la página principal" height="64" width="64"></a>\n'
    # t += '      <a href="#"><img src="../varios/iconos/icono-arrow-circle-up.svg" alt="Principio de la página" title="Principio de la página" width="36" height="36"></a>\n'
    t += "    </p>\n"
    t += "  </nav>\n"
    t += "\n"

    t += "<p>En estas estadísticas sólo se contabilizan las páginas webs. No se contabilizan "
    t += "las páginas de ejemplos o de ejercicios incluidas en otras páginas.</p>\n"
    t += " \n"
    t += "<p>La gráfica de estadísticas acumuladas sólo contabiliza las páginas de apuntes "
    t += "de ASIR.</p>\n"
    t += " \n"

    # Dibuja la gráfica acumulada
    t += f"  <h2>Todos los apuntes acumulados</h2>\n"
    t += "\n"
    t += "  <p>\n"

    # print(acumuladas_json)
    for i in range(1, len(ACUMULADAS)):
        for j in YEARS:
            for k in range(1, len(acumuladas_json[ACUMULADAS[i][0]][j]) + 1):
                # print(acumuladas_json[ACUMULADAS[i][0]][j][str(k)], acumuladas_json[ACUMULADAS[i - 1][0]
                # ][j][str(k)], end=" ")
                acumuladas_json[ACUMULADAS[i][0]][j][str(k)] += acumuladas_json[
                    ACUMULADAS[i - 1][0]
                ][j][str(k)]
                # print(acumuladas_json[ACUMULADAS[i][0]][j][str(k)])
    # print(acumuladas_json)

    ind = ACUMULADAS[-1][0]
    pasito = 24
    tamX = pasito * 12 * len(YEARS)
    tamY = 300
    px = pasito / 2

    t += '    <svg version="1.1" xmlns="http://www.w3.org/2000/svg"\n'
    t += f'      width="{pasito * (12 * len(YEARS) + 4)}" height="{tamY + 110}" viewBox="-30 {-2 * pasito} {pasito * (12 * len(YEARS) + 4)} {tamY + 110}" font-family="sans-serif" font-size="18">\n'

    # dibuja los ejes principales
    t += f'      <polyline points="{pasito},{-pasito / 2} {pasito},{tamY} {tamX + pasito * 1.5},{tamY}" \n'
    t += '        stroke-width="3" stroke="black" fill="none" />\n'

    # divide el número de páginas por los días del mes
    for i in range(len(ACUMULADAS)):
        for j in YEARS:
            for k in range(1, len(acumuladas_json[ACUMULADAS[i][0]][j]) + 1):
                acumuladas_json[ACUMULADAS[i][0]][j][str(k)] = round(
                    acumuladas_json[ACUMULADAS[i][0]][j][str(k)]
                    / monthrange(int(j), k)[1]
                )

    estadisticas[ind] = {}
    minimo = acumuladas_json[ind][YEARS[0]]["1"]
    maximo = acumuladas_json[ind][YEARS[0]]["1"]
    for j in YEARS:
        for k in range(1, len(acumuladas_json[ind][j]) + 1):
            if acumuladas_json[ind][j][str(k)] < minimo:
                minimo = acumuladas_json[ind][j][str(k)]
            if acumuladas_json[ind][j][str(k)] > maximo:
                maximo = acumuladas_json[ind][j][str(k)]
    estadisticas[ind]["minimo"] = minimo
    estadisticas[ind]["maximo"] = maximo

    uniY = 10 ** (math.floor(math.log(estadisticas[ind]["maximo"], 10)) - 1)
    pYmaximo = round(math.ceil(estadisticas[ind]["maximo"] / uniY) * uniY)
    # Este if es para que el número de rayas horizontales no sea mayor que 10
    if pYmaximo / uniY <= 10:
        factor = 1
    elif pYmaximo / uniY <= 20:
        factor = 2
    elif pYmaximo / uniY <= 50:
        factor = 5
    else:
        uniY = uniY * 10
        factor = 1
    # Este if es para que si la escala del eje Y es 10 o 100 los números no superen el 10 (para que sea fácil interpretar los números)
    if uniY == 10 and math.floor(pYmaximo / uniY / factor) * factor > 10:
        uniY = 1
        factor = factor * 10
    elif uniY == 100 and math.floor(pYmaximo / uniY / factor) * factor > 10:
        uniY = 1
        factor = factor * 100

    # print(f'{estadisticas[ind]["maximo"]} {pYmaximo} => {pYmaximo/uniY} {uniY} => {math.floor(pYmaximo / uniY / factor)} {factor}\n')

    # leyenda eje Y
    t += f'      <text x="0" y="{-pasito}" text-anchor="start">x{"{:,}".format(uniY).replace(",",".")} al día</text>\n'

    # dibuja las líneas horizontales
    for i in range(1, math.floor(pYmaximo / uniY / factor) + 1):
        uniYpos = round(tamY - uniY * factor * i / pYmaximo * tamY)
        t += f'      <line x1="{pasito}" y1="{uniYpos}" x2="{tamX + pasito + pasito / 2}" y2="{uniYpos}" \n'
        t += '        stroke-width="1" stroke="black" stroke-dasharray="5 5" />\n'
        t += f'      <text x="{pasito - 10}" y="{uniYpos + 5}" text-anchor="end">{"{:,}".format(i * factor).replace(",",".")}</text>\n'

    # dibuja las líneas verticales de los meses
    for j in range(len(YEARS)):
        for k in range(12):
            t += f'      <line x1="{(12 * j + k + 2) * pasito}" y1="{-pasito / 2}" x2="{(12 * j + k + 2) * pasito}" y2="{tamY}" \n'
            t += '        stroke-width="1" stroke="red" stroke-dasharray="5 5" />\n'
            t += f'      <text x="{(12 * j + k + 1.5) * pasito}" y="{tamY + 20}" text-anchor="middle">{MONTHS[k]}</text>\n'

    # dibuja las líneas verticales de los años
    for j in range(len(YEARS)):
        t += f'      <line x1="{(12 * j + 13) * pasito}" y1="{-pasito / 2}" x2="{(12 * j + 13) * pasito}" y2="{tamY + 40}" \n'
        t += '        stroke-width="2" stroke="black" stroke-dasharray="5 5" />\n'
        t += f'      <text x="{(12 * j + 6.5) * pasito}" y="{tamY + 50}" text-anchor="middle">{YEARS[j]}</text>\n'

    # dibuja las gráficas
    for i in range(len(ACUMULADAS)):
        px = pasito / 2
        ind = ACUMULADAS[i][0]
        t += '      <polyline fill="none" stroke-width="2" stroke="RoyalBlue"\n'
        t += '        points="'
        for j in YEARS:
            for k in range(1, len(acumuladas_json[ind][j]) + 1):
                py = round(tamY - acumuladas_json[ind][j][str(k)] / pYmaximo * tamY)
                px += pasito
                t += f"{px},{py} "
        t += '"\n'
        t += "      />\n"
        t += f'      <text x="{px + 10}" y="{py + 5}" text-anchor="start">{ACUMULADAS[i][0]}</text>\n'
        # t += f'      <text x="{px + 10}" y="{py + 5}" text-anchor="start" style="stroke:white; stroke-width:0.6em">{ACUMULADAS[i][0]}</text>\n'
        # t += f'      <text x="{px + 10}" y="{py + 5}" text-anchor="start" style="fill:black">{ACUMULADAS[i][0]}</text>\n'

    t += "    </svg>\n"
    t += "  </p>\n"
    t += "\n"
    # FIN gráfica acumulada

    # Dibuja la gráfica de cada grupo de apuntes
    for i in range(len(APUNTES_ESTADISTICAS)):
        t += f"  <h2>{APUNTES_ESTADISTICAS[i][1]}</h2>\n"
        t += "\n"
        t += "  <p>\n"

        ind = APUNTES_ESTADISTICAS[i][0]
        pasito = 24
        tamX = pasito * 12 * len(YEARS)
        tamY = 300
        px = pasito / 2

        t += '    <svg version="1.1" xmlns="http://www.w3.org/2000/svg"\n'
        t += f'      width="{pasito * (12 * len(YEARS) + 4)}" height="{tamY + 110}" viewBox="-30 {-2 * pasito} {pasito * (12 * len(YEARS) + 4)} {tamY + 110}" font-family="sans-serif" font-size="18">\n'

        # dibuja los ejes principales
        t += f'      <polyline points="{pasito},{-pasito / 2} {pasito},{tamY} {tamX + pasito * 1.5},{tamY}" \n'
        t += '        stroke-width="3" stroke="black" fill="none" />\n'

        # divide el número de páginas por los días del mes
        for j in YEARS:
            for k in range(1, len(estadisticas_json[ind][j]) + 1):
                estadisticas_json[ind][j][str(k)] = round(
                    estadisticas_json[ind][j][str(k)] / monthrange(int(j), k)[1]
                )

        estadisticas[ind] = {}
        minimo = estadisticas_json[ind][YEARS[0]]["1"]
        maximo = estadisticas_json[ind][YEARS[0]]["1"]
        for j in YEARS:
            for k in range(1, len(estadisticas_json[ind][j]) + 1):
                if estadisticas_json[ind][j][str(k)] < minimo:
                    minimo = estadisticas_json[ind][j][str(k)]
                if estadisticas_json[ind][j][str(k)] > maximo:
                    maximo = estadisticas_json[ind][j][str(k)]
                # print(estadisticas_json[ind][j][str(k)])
        estadisticas[ind]["minimo"] = minimo
        estadisticas[ind]["maximo"] = maximo

        uniY = 10 ** (math.floor(math.log(estadisticas[ind]["maximo"], 10)) - 1)
        pYmaximo = round(math.ceil(estadisticas[ind]["maximo"] / uniY) * uniY)
        # Este if es para que el número de rayas horizontales no sea mayor que 10
        if pYmaximo / uniY <= 10:
            factor = 1
        elif pYmaximo / uniY <= 20:
            factor = 2
        elif pYmaximo / uniY <= 50:
            factor = 5
        else:
            uniY = uniY * 10
            factor = 1
        # Este if es para que si la escala del eje Y es 10 o 100 los números no superen el 10 (para que sea fácil interpretar los números)
        if uniY == 10 and math.floor(pYmaximo / uniY / factor) * factor > 10:
            uniY = 1
            factor = factor * 10
        elif uniY == 100 and math.floor(pYmaximo / uniY / factor) * factor > 10:
            uniY = 1
            factor = factor * 100

        # print(f'{estadisticas[ind]["maximo"]} {pYmaximo} => {pYmaximo/uniY} {uniY} => {math.floor(pYmaximo / uniY / factor)} {factor}\n')

        # leyenda eje Y
        t += f'      <text x="0" y="{-pasito}" text-anchor="start">x{"{:,}".format(uniY).replace(",",".")} al día</text>\n'

        # dibuja las líneas horizontales
        for i in range(1, math.floor(pYmaximo / uniY / factor) + 1):
            uniYpos = round(tamY - uniY * factor * i / pYmaximo * tamY)
            t += f'      <line x1="{pasito}" y1="{uniYpos}" x2="{tamX + pasito + pasito / 2}" y2="{uniYpos}" \n'
            t += '        stroke-width="1" stroke="black" stroke-dasharray="5 5" />\n'
            t += f'      <text x="{pasito - 10}" y="{uniYpos + 5}" text-anchor="end">{"{:,}".format(i * factor).replace(",",".")}</text>\n'

        # dibuja las líneas verticales de los meses
        for j in range(len(YEARS)):
            for k in range(12):
                t += f'      <line x1="{(12 * j + k + 2) * pasito}" y1="{-pasito / 2}" x2="{(12 * j + k + 2) * pasito}" y2="{tamY}" \n'
                t += '        stroke-width="1" stroke="red" stroke-dasharray="5 5" />\n'
                t += f'      <text x="{(12 * j + k + 1.5) * pasito}" y="{tamY + 20}" text-anchor="middle">{MONTHS[k]}</text>\n'

        # dibuja las líneas verticales de los años
        for j in range(len(YEARS)):
            t += f'      <line x1="{(12 * j + 13) * pasito}" y1="{-pasito / 2}" x2="{(12 * j + 13) * pasito}" y2="{tamY + 40}" \n'
            t += '        stroke-width="2" stroke="black" stroke-dasharray="5 5" />\n'
            t += f'      <text x="{(12 * j + 6.5) * pasito}" y="{tamY + 50}" text-anchor="middle">{YEARS[j]}</text>\n'

        # dibuja la gráfica
        t += '      <polyline fill="none" stroke-width="3" stroke="RoyalBlue"\n'
        t += '        points="'
        for j in YEARS:
            for k in range(1, len(estadisticas_json[ind][j]) + 1):
                py = round(tamY - estadisticas_json[ind][j][str(k)] / pYmaximo * tamY)
                px += pasito
                t += f"{px},{py} "
        t += '"\n'
        t += "      />\n"

        t += "    </svg>\n"
        t += "  </p>\n"
        t += "\n"

    t += "\n"
    t += '  <address id="ultmod">\n'
    t += "    Autor: Bartolomé Sintes Marco<br>\n"
    t += f"    Última modificación de esta página: {fecha_a_texto(str(date.today()))}\n"
    t += "  </address>\n"
    t += "</body>\n"
    t += "</html>\n"

    with open(FICHERO_ESTADISTICAS, "w", encoding="utf-8") as fichero:
        fichero.write(t)


def main():
    print("Estadísticas mclibre")
    # Descomentar las líneas del paso que se quiera realizar

    # Primero
    # en paso-0 hay que poner los logs originales de las semanas que se quieran analizar
    # en paso-1 se guardarán los ficheros separando clean, img, etc.
    # mclibre_limpia_logs()

    # Segundo
    # en paso-0 hay que poner los logs clean obtenidos con mclibre_limpia_logs()
    # en paso-2 se guardarán los ficheros separando grupos de apuntes
    # mclibre_divide_logs_apuntes()

    # cuenta_revistas()

    # en paso-2 tienen que estar los ficheros de cada grupo de apuntes
    # muestra por pantalla las páginas totales que hay en cada grupo (cuenta el intro final de más)
    # cuenta_paginas()

    # Tercero
    # en paso-2 tienen que estar los ficheros de cada grupo de apuntes
    # crea visitas.json con las páginas que hay en cada grupo
    # como argumento se pone el año que corresponde
    # cuenta_paginas_meses(2020)

    # Cuarto
    # une todos los ficheros visitas-YYYY.json en un único fichero
    # une_visitas_json()

    # Quinto
    # a partir de visitas-todas.json crea página de estadísticas
    genera_estadisticas()


if __name__ == "__main__":
    main()
