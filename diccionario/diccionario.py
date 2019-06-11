import pathlib, re

ORIGEN_HTML = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\htmlcss"
# ORIGEN_HTML = "C:\\Users\\ASIR 7L\\Documents\\IAW\\apuntes\\htmlcss"
ORIGEN_PYTHON = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\python"
ORIGEN_INFORMATICA = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\informatica"
ORIGEN_WEBAPPS = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\webapps"
ORIGEN_XML = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\xml"
ORIGEN_PHP = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\php"

ORIGEN = ORIGEN_PHP

DICT_COD_PAISES = "dic_cod_paises.txt"
DICT_COD_TK = "dic_cod_tk.txt"
DICT_COD_UNICODE = "dic_cod_unicode.txt"
DICT_EXCEPCIONES = "dic_excepciones.txt"
DICT_EXCEPCIONES_XML = "dic_excepciones_xml.txt"
DICT_EXCEPCIONES_PHP = "dic_excepciones_php.txt"
DICT_GENERAL_ABREVIATURAS = "dic_general_abreviaturas.txt"
DICT_GENERAL_NOMBRES = "dic_general_nombres.txt"
DICT_GENERAL_SIGLAS = "dic_general_siglas.txt"
DICT_IDIOMAS_ESPANOL = "dic_idiomas_espanol.txt"
DICT_IDIOMAS_INGLES = "dic_idiomas_ingles.txt"
DICT_IDIOMAS_LATIN = "dic_idiomas_latin.txt"
DICT_IDIOMAS_NONSENSE = "dic_idiomas_nonsense.txt"
DICT_IDIOMAS_OTROS = "dic_idiomas_otros.txt"
DICT_IDIOMAS_VALENCIANO = "dic_idiomas_valenciano.txt"
DICT_TECNICO = "dic_tecnico.txt"
DICT_TECNICO_CSS = "dic_tecnico_css.txt"
DICT_TECNICO_HTML = "dic_tecnico_html.txt"
DICT_TECNICO_JAVASCRIPT = "dic_tecnico_javascript.txt"
DICT_TECNICO_MCLIBRE_CSS = "dic_tecnico_mclibre_css.txt"
DICT_TECNICO_PHP = "dic_tecnico_php.txt"
DICT_TECNICO_PYTHON = "dic_tecnico_python.txt"
DICT_TECNICO_SQL = "dic_tecnico_sql.txt"
DICT_TECNICO_SVG = "dic_tecnico_svg.txt"
DICT_TECNICO_XML = "dic_tecnico_xml.txt"

DICT_LIST = [
    [DICT_EXCEPCIONES, "excepciones", 1, 11],
    [DICT_IDIOMAS_ESPANOL, "español", 2, 12],
    [DICT_IDIOMAS_INGLES, "inglés", 3, 13],
    [DICT_GENERAL_NOMBRES, "nombres", 4, 14],
    [DICT_TECNICO, "técnicos", 5, 15],
    [DICT_TECNICO_HTML, "html", 6, 16],
    [DICT_TECNICO_CSS, "css", 7, 17],
    [DICT_TECNICO_MCLIBRE_CSS, "mis-css", 8, 18],
    [DICT_TECNICO_SVG, "svg", 21, 22],
    [DICT_TECNICO_JAVASCRIPT, "js", 23, 24],
    [DICT_TECNICO_PYTHON, "py", 25, 26],
    [DICT_TECNICO_PHP, "php", 27, 28],
    [DICT_TECNICO_XML, "xml", 29, 30],
    [DICT_TECNICO_SQL, "sql", 31, 32],
    [DICT_IDIOMAS_LATIN, "latín", 33, 34],
    [DICT_IDIOMAS_VALENCIANO, "valenciano", 35, 36],
    [DICT_IDIOMAS_NONSENSE, "nonsense", 37, 38],
    [DICT_IDIOMAS_OTROS, "Otros idiomas", 39, 40],
    [DICT_COD_UNICODE, "Unicode", 41, 42],
    [DICT_GENERAL_SIGLAS, "Siglas", 43, 44],
    [DICT_GENERAL_ABREVIATURAS, "Abreviaturas", 45, 46],
    [DICT_COD_PAISES, "Códigos países", 47, 48],
    [DICT_COD_TK, "Tk", 49, 50],
    [DICT_EXCEPCIONES_XML, "Excep. XML", 51, 52],
    [DICT_EXCEPCIONES_PHP, "Excep. PHP", 53, 54 ]
]

EXTENSIONES = ["html"]
EXTENSIONES_NO_ANALIZADAS = [
    "css",
    "svg",
    "php",
    "py",
    "js",
    "md",
    "png",
    "jpg",
    "webp",
    "gif",
    "ico",
    "cur",
    "swf",
    "pdf",
    "otf",
    "ttf",
    "git",
    "json",
    "woff",
    "woff2",
    "zip",
    ".gitignore",
]


def estadisticas():
    total = 0
    for _ in pathlib.Path(ORIGEN).glob(f"**/*.*"):
        total += 1
    print(f"Total: {total} ficheros")

    total_analizadas = 0
    print("Extensiones analizadas: ", end="")
    for extension in EXTENSIONES:
        contador = 0
        for _ in pathlib.Path(ORIGEN).glob(f"**/*.{extension}"):
            contador += 1
        total_analizadas += contador
        if contador:
            print(f"{extension}: {contador} - ", end="")
    print()
    print(f"Total: {total_analizadas} ficheros")

    print("Extensiones no analizadas: ", end="")
    total_no_analizadas = 0
    for extension in EXTENSIONES_NO_ANALIZADAS:
        contador = 0
        for _ in pathlib.Path(ORIGEN).glob(f"**/*.{extension}"):
            contador += 1
        total_no_analizadas += contador
        if contador:
            print(f"{extension}: {contador} - ", end="")
    print()
    print(f"Total: {total_no_analizadas} ficheros")

    print(
        f"En el directorio hay {total} ficheros: se analizarán {total_analizadas}, no se analizarán {total_no_analizadas}, {total - total_analizadas - total_no_analizadas} sin identificar"
    )
    print()


def ordena_diccionarios():
    no_cuenta = [DICT_EXCEPCIONES, DICT_EXCEPCIONES_XML, DICT_EXCEPCIONES_PHP, DICT_TECNICO_MCLIBRE_CSS, DICT_IDIOMAS_NONSENSE, DICT_GENERAL_NOMBRES, DICT_GENERAL_SIGLAS, DICT_GENERAL_ABREVIATURAS,  DICT_COD_TK, DICT_COD_UNICODE]
    print()
    print("Ordenando diccionarios ...")
    total_palabras = 0
    for i in DICT_LIST:
        dicts = []
        # Carga diccionario
        if pathlib.Path(i[0]).exists():
            with open(i[0], "r", encoding="utf-8") as fichero:
                palabras = fichero.read().split()
            dicts += palabras
            # Ordena diccionario
            dicts.sort(key=str.lower)
            # Borra valores repetidos
            for j in range(len(dicts) - 1, 0, -1):
                k = j - 1
                while k >= 0:
                    if dicts[k] == dicts[j]:
                        del dicts[j]
                        k = 0
                    k -= 1
            total_palabras += len(dicts)
            # Descuenta las palabras de DICT_EXCEPCIONES
            if i[0] in no_cuenta:
                total_palabras -= len(dicts)
        # Guarda diccionario
        with open(i[0], "w", encoding="utf-8") as fichero_dic:
            for palabra in dicts:
                print(f"{palabra} ", file=fichero_dic)
    print(f"Los diccionarios contienen ahora {total_palabras} términos.")


def main():
    estadisticas()

    # Carga todos los diccionarios
    dicts = []
    for i in DICT_LIST:
        if pathlib.Path(i[0]).exists():
            with open(i[0], "r", encoding="utf-8") as fichero:
                palabras = fichero.read().split()
            dicts += palabras

    print("Análisis")
    for extension in EXTENSIONES:
        contador = 0
        seguir_incluyendo = True
        for filename in pathlib.Path(ORIGEN).rglob(f"**/*.{extension}"):
            if seguir_incluyendo:
                contador += 1
                print()
                print(f"{contador}: {filename}")
                with open(filename, "r", encoding="utf-8") as fichero:
                    texto = fichero.read()

                    # elimina scripts JS
                    x = re.search(r"<script>[^<]+<\/script>", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"<script>[^<]+<\/script>", texto)

                    # elimina urls del tipo <a href=>url</a>
                    # utiliza grupos: https://docs.python.org/3/library/re.html#index-24
                    elimina = [
                        r"<a href=\"([^\"]+)\">\1</a>",
                        r"<a href=\"https://([^\"]+)/\">\1</a>",
                        r"<a href=\"https://([^\"]+)\">\1</a>",
                        r"<a href=\"http://([^\"]+)/\">\1</a>",
                        r"<a href=\"http://([^\"]+)\">\1</a>",
                    ]
                    for i in elimina:
                        x = re.search(i, texto)
                        while x:
                            texto = texto.replace(x.group(), " ")
                            x = re.search(i, texto)

                    # elimina etiquetas
                    x = re.search(r"<[^>]+>", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"<[^>]+>", texto)

                    # elimina etiquetas de los ejemplos de código
                    x = re.search(r"&lt;[^&]+&gt;", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"&lt;[^&]+&gt;", texto)

                    # elimina comentarios CSS /*  ... */
                    x = re.search(r"\/\*[^*]+\*\/", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"\/\*[^*]+\*\/", texto)

                    # elimina urls CSS
                    x = re.search(r"url\([^)]+\)", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"url\([^)]+\)", texto)

                    # elimina urls
                    elimina = ["https", "http", "ftp", "email"]
                    for i in elimina:
                        x = re.search(r"" + i + r"[^\s\"]+", texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(r"" + i + r"[^\s\"]+", texto)

                    # elimina nombres de archivos
                    # que no suelen llevar acentos
                    elimina = ["html", "css", "svg", "png", "jpg", "zip"]
                    for i in elimina:
                        x = re.search(
                            r"[^ ]+\." + i + r"(#[^\s,\,;)\"]+)?[\s,\.;)\"<]", texto
                        )
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(
                                r"[^ ]+\." + i + r"(#[^\s,\,;)\"]+)?[\s,\.;)\"<]", texto
                            )

                    # elimina direcciones de correo
                    # que no llevan acentos
                    x = re.search(r"[^\s]+@[^\s]+", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"[^\s]+@[^\s]+", texto)

                    # Tengo que eliminar primero los #RGB de 6 y luego los de 3
                    # porque si no eliminaba #000 y #FFF y se quedaban tres caracteres sueltos
                    # elimina códigos de colores #RGB
                    x = re.search(r"#[0-9a-fA-F]{6}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"#[0-9a-fA-F]{6}", texto)
                    x = re.search(r"#[0-9a-fA-F]{3}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"#[0-9a-fA-F]{3}", texto)

                    # elimina códigos de colores rgb()
                    x = re.search(r"rgb\([0-9, ]+\)", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"rgb\([0-9, ]+\)", texto)

                    # elimina códigos de colores hsl()
                    x = re.search(r"hsl\([0-9, ]+\)", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"hsl\([0-9, ]+\)", texto)

                    # elimina números sin unidades con guión detrás
                    # para los comentarios entre guiones que uso para fechas
                    x = re.search(r"\s-?[0-9]+-[\s,]", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"\s-?[0-9]+-[\s,]", texto)

                    # elimina fechas en formato AAAA-MM-DD
                    x = re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", texto)

                    # elimina entidades numéricas
                    x = re.search("&amp;[#0-9a-zA-Z]+;", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("&amp;[#0-9a-zA-Z]+;", texto)
                    x = re.search("&[#0-9a-zA-Z]+;", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("&[#0-9a-zA-Z]+;", texto)

                    # elimina códigos unicode U
                    x = re.search(r"U\+[0-9a-fA-F]+", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"U\+[0-9a-fA-F]+", texto)

                    # elimina números con unidades
                    unidades = [
                        "%",
                        "px",
                        "em",
                        "rem",
                        "pt",
                        "in",
                        "pc",
                        "cm",
                        "mm",
                        "ex",
                        "ch",
                        "q",
                        "dpi",
                        "s",
                        "m"
                    ]
                    for i in unidades:
                        x = re.search(r"-?[\d\.\d]+" + i + r'[\s.;,:")]', texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(r"-?[\d\.\d]+" + i + r'[\s.;,:")]', texto)

                    # # elimina comillas en palabras entrecomilladas
                    # No sirve tendría que dejar la palabra y qitar sólo las comillas
                    # x = re.search(r"\'[a-zA-Z]+\'", texto)
                    # # print(x.group())
                    # while x:
                    #     texto = texto.replace(x.group(), " ")
                    #     x = re.search("'[a-zA-Z]+'", texto)

                    # CASOS ESPECIALES

                    # elimina genitivo sajón
                    elimina = ["'s ", "’s " " d'"]
                    for i in elimina:
                        texto = texto.replace(i, " ")

                    # elimina ideograph-números (símbolos Unicode)
                    x = re.search(r"ideograph-[0-9a-fA-F]{4}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"ideograph-[0-9a-fA-F]{4}", texto)

                    # elimina juego de caracteres cp1252 (html-ut8.html)
                    x = re.search(r"cp1252 = '[^\n]+", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"cp1252 = '[^\n]+", texto)

                    # elimina códigos normas ISO
                    x = re.search(r"ISO-[0-9]+(-[0-9]+)?", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"ISO-[0-9]+(-[0-9]+)?", texto)

                    # elimina resto de caracteres que no son letras
                    elimina = r'<>=""\/().¿?¡!:,[]()%{}|;^&#±`@«»~€ªº²“‘’$≤'
                    for i in elimina:
                        texto = texto.replace(i, " ")

                    # elimina otros caracteres
                    elimina = [r"\s-\s", r"\s+\s", r"\s'", r"'\s", "'.", "';", "—", "''"]
                    for i in elimina:
                        texto = texto.replace(i, " ")

                    # elimina saltos de línea y espacios
                    texto = texto.replace("\n", " ")
                    texto = texto.replace("\r", " ")
                    x = re.search("  +", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("  +", texto)

                    # elimina números sin unidades
                    x = re.search(r"\s-?[0-9]+[\s;]", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"\s-?[0-9]+[\s;]", texto)

                    # elimina intervalos de números (años, básicamente)
                    elimina = [r"[>\s][0-9]+.[0-9]+"]
                    for i in elimina:
                        x = re.search(i, texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(i, texto)

                    # elimina operaciones con números
                    elimina = [r"\s[+*-]?([\d]+|[a-z])([+*-]([\d]+|[a-z]))+\s"]
                    for i in elimina:
                        x = re.search(i, texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(i, texto)

                    # print(texto)
                    palabras = texto.split()
                    # print(palabras)
                    for palabra in palabras:
                        # print(palabra)
                        palabra = palabra.strip("'\"-+*”·█_")
                        palabra_original = palabra
                        palabra = palabra.lower()

                        if (
                            palabra
                            and not palabra in dicts
                            and not palabra_original in dicts
                            and not palabra.isnumeric()
                            and seguir_incluyendo
                        ):
                            print()
                            print(palabra)
                            print()
                            print("0: Saltar - x: SALIR")
                            for _ in range(len(DICT_LIST)):
                                print(
                                    f"{DICT_LIST[_][2]}: {DICT_LIST[_][1]} - ", end=""
                                )
                            print()
                            print()
                            if palabra != palabra_original:
                                print(palabra_original)
                                print()
                                print("0: Saltar - x: SALIR")
                                for _ in range(len(DICT_LIST)):
                                    print(
                                        f"{DICT_LIST[_][3]}: {DICT_LIST[_][1]} - ",
                                        end="",
                                    )
                                print()
                                print()
                            incluir = input("¿Incluir? ")
                            if incluir == "x":
                                seguir_incluyendo = False
                            elif incluir != 0:
                                for _ in range(len(DICT_LIST)):
                                    if int(incluir) == DICT_LIST[_][2]:
                                        with open(
                                            DICT_LIST[_][0], "a", encoding="utf-8"
                                        ) as fichero_dic:
                                            print(f"{palabra} ", file=fichero_dic)
                                        dicts += [palabra]
                                for _ in range(len(DICT_LIST)):
                                    if int(incluir) == DICT_LIST[_][3]:
                                        with open(
                                            DICT_LIST[_][0], "a", encoding="utf-8"
                                        ) as fichero_dic:
                                            print(
                                                f"{palabra_original} ", file=fichero_dic
                                            )
                                        dicts += [palabra_original]

    ordena_diccionarios()


if __name__ == "__main__":
    main()
