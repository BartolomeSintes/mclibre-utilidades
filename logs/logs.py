import pathlib, re

# para ejecutar esta aplicación,
# escriba en MCL_0 la raíz de los ficheros a analizar
# y ejecute la orden py diccionario.py

MCL_0 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-0"
MCL_1 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-1"
MCL_2 = "D:\\Barto\\logs\\logs.mclibre.org\\paso-2"
# usar \\ en vez de / porque pathlib usa \ y no funciona replace

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
    ".odt",
    ".odp",
    ".ods",
    ".sxi",
    ".swf",
    ".mp3",
    ".mp4",
    ".exe",
    ".zip",
    ".7z",
    ".gz",
    ".tgz",
    ".iso",
    "ova",
]
IMG = [".jpg", ".png", ".svg", ".gif", ".webp", ".ico", ".cur"]
OTROS = [".css", ".js", ".woff", ".otf", ".ttf", ".po", ".eot"]
APUNTES = [
    "consultar/amaya",
    "consultar/documentacion",
    "consultar/google",
    "consultar/htmlcss",
    "consultar/informatica",
    "consultar/linux",
    "consultar/php",
    "consultar/primaria",
    "consultar/python",
    "consultar/webapps",
    "consultar/xml",
]


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
                    for i in LIMPIA:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=clean)
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
            str(source_file).replace(MCL_0, MCL_2 + "\\iaig_pendientes")
            + ".iaig_pendientes"
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
        file_linux = str(source_file).replace(MCL_0, MCL_2 + "\\linux") + ".linux"
        file_musica = str(source_file).replace(MCL_0, MCL_2 + "\\musica") + ".musica"
        file_pau = str(source_file).replace(MCL_0, MCL_2 + "\\pau") + ".pau"
        file_php = str(source_file).replace(MCL_0, MCL_2 + "\\php") + ".php"
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
        linux = open(file_linux, "w", encoding="utf-8")
        musica = open(file_musica, "w", encoding="utf-8")
        pau = open(file_pau, "w", encoding="utf-8")
        php = open(file_php, "w", encoding="utf-8")
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
                elif (
                    "consultar/iaig_pendientes" in texto
                    or "consultar//iaig_pendientes" in texto
                ):
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
                elif "consultar/linux" in texto or "consultar//linux" in texto:
                    print(texto, end="", file=linux)
                elif "consultar/musica" in texto or "consultar//musica" in texto:
                    print(texto, end="", file=musica)
                elif "/pau" in texto:
                    print(texto, end="", file=pau)
                elif "consultar/php" in texto or "consultar//php" in texto:
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
        linux.close()
        musica.close()
        pau.close()
        php.close()
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


def cuenta_paginas():
    print("Cuenta páginas")
    APUNTES = [
        "charlas",
        "docs",
        "htmlcss",
        "informatica",
        "php",
        "primaria",
        "python",
        "webapps",
        "xml",
    ]
    contadores = []
    for i in range(len(APUNTES)):
        contadores += [0]

        for source_file in pathlib.Path(MCL_2 + "/" + APUNTES[i]).rglob(f"**/*.*"):
            print(source_file)
            with open(source_file, "r", encoding="utf-8") as file:
                texto = file.readline()
                contadores[i] += 1
                while texto:
                    texto = file.readline()
                    contadores[i] += 1

    for i in range(len(APUNTES)):
        print(f"{APUNTES[i]}: {contadores[i]:,}")


def main():
    # mclibre_limpia_logs()
    # mclibre_divide_logs_apuntes()
    # cuenta_revistas()
    cuenta_paginas()


if __name__ == "__main__":
    main()
