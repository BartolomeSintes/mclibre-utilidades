import pathlib, html.parser, re

DICT_EXCEPCIONES = "diccionario_excepciones.txt"
DICT_ESPANOL = "diccionario_espanol.txt"
DICT_INGLES = "diccionario_ingles.txt"
DICT_FRANCES = "diccionario_frances.txt"
DICT_LATIN = "diccionario_latin.txt"
DICT_VALENCIANO = "diccionario_valenciano.txt"
DICT_ALEMAN = "diccionario_aleman.txt"
DICT_NONSENSE = "diccionario_nonsense.txt"
DICT_NOMBRES = "diccionario_nombres.txt"
DICT_TECNICOS = "diccionario_tecnicos.txt"
DICT_HTML = "diccionario_html.txt"
DICT_CSS = "diccionario_css.txt"
DICT_MIS_CSS = "diccionario_mis_css.txt"
DICT_SVG = "diccionario_svg.txt"
DICT_JAVASCRIPT = "diccionario_javascript.txt"
DICT_PYTHON = "diccionario_python.txt"
DICT_PHP = "diccionario_php.txt"

DICT_LIST = [
    [DICT_EXCEPCIONES, "excepciones", 1, 11],
    [DICT_ESPANOL, "español", 2, 12],
    [DICT_INGLES, "inglés", 3, 13],
    [DICT_NOMBRES, "nombres", 4, 14],
    [DICT_TECNICOS, "técnicos", 5, 15],
    [DICT_HTML, "html", 6, 16],
    [DICT_CSS, "css", 7, 17],
    [DICT_MIS_CSS, "mis-css", 8, 18],
    [DICT_SVG, "svg", 21, 22],
    [DICT_JAVASCRIPT, "js", 23, 24],
    [DICT_PYTHON, "py", 25, 26],
    [DICT_PHP, "php", 27, 28],
    [DICT_FRANCES, "francés", 31, 32],
    [DICT_LATIN, "latín", 33, 34],
    [DICT_VALENCIANO, "valenciano", 35, 36],
    [DICT_ALEMAN, "alemán", 37, 38],
    [DICT_NONSENSE, "nonsense", 39, 40],
]

ORIGEN_HTML = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\htmlcss"
# ORIGEN_HTML = "C:\\Users\\ASIR 7L\\Documents\\IAW\\apuntes\\htmlcss"
# ORIGEN_HTML = "C:/tmp/python-diccionario-prueba"

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
    for _ in pathlib.Path(ORIGEN_HTML).glob(f"**/*.*"):
        total += 1
    print(f"Total: {total} ficheros")

    total_analizadas = 0
    print("Extensiones analizadas: ", end="")
    for extension in EXTENSIONES:
        contador = 0
        for _ in pathlib.Path(ORIGEN_HTML).glob(f"**/*.{extension}"):
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
        for _ in pathlib.Path(ORIGEN_HTML).glob(f"**/*.{extension}"):
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
    total_palabras = 0
    for i in DICT_LIST:
        dicts = []
        # Carga diccionario
        if pathlib.Path(i[0]).exists():
            with open(i[0], "r", encoding="utf-8") as fichero:
                palabras = fichero.read().split()
            dicts += palabras
            # Ordena diccionario
            dicts.sort()
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
            if i[0] == DICT_EXCEPCIONES or i[0] == DICT_MIS_CSS:
                total_palabras -= len(dicts)
        # Guarda diccionario
        with open(i[0], "w", encoding="utf-8") as fichero_dic:
            for palabra in dicts:
                print(f"{palabra} ", file=fichero_dic)
    print(f"Los diccionarios contienen ahora {total_palabras} términos.")


class MyHTMLParser(html.parser.HTMLParser):
    lista_urls = []

    def handle_starttag(self, tag, attrs):
        busca = [
            ["a", "href"],
            ["img", "src"],
            ["link", "href"],
            ["svg", "xmlns"],
            ["img", "data-canonical-src"],
            ["object", "data"],
        ]
        for i in busca:
            if tag == i[0]:
                for j in attrs:
                    if j[0] == i[1]:
                        self.lista_urls += [f'{i[1]}="{j[1]}"', j[1]]
                        # print(f"encontrado {i[0]}, {i[1]}")


def elimina_urls(filename):
    with open(filename, "r", encoding="utf-8") as fichero:
        texto = fichero.read()
    parser = MyHTMLParser()
    parser.feed(texto)
    return parser.lista_urls


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
        for filename in pathlib.Path(ORIGEN_HTML).rglob(f"**/*.{extension}"):
            if seguir_incluyendo:
                contador += 1
                print()
                print(f"{contador}: {filename}")
                urls_para_eliminar = elimina_urls(filename)
                with open(filename, "r", encoding="utf-8") as fichero:
                    texto = fichero.read()

                    # elimina scripts JS
                    x = re.search(r"<script>[^<]+<\/script>", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"<script>[^<]+<\/script>", texto)

                    # elimina etiquetas
                    x = re.search(r"<[^>]+>", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"<[^>]+>", texto)

                    # elimina comentarios CSS /*  ... */
                    x = re.search(r"\/\*[^*]+\*\/", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"\/\*[^*]+\*\/", texto)

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

                    # elimina urls
                    for i in urls_para_eliminar:
                        texto = texto.replace(i, " ")

                    # elimina urls CSS
                    x = re.search(r"url\([^)]+\)", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"url\([^)]+\)", texto)

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
                    ]
                    for i in unidades:
                        x = re.search(r"-?[\d\.\d]+" + i + r"[\s.;,)]", texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(r"-?[\d\.\d]+" + i + r"[\s.;,)]", texto)

                    # # elimina comillas en palabras entrecomilladas
                    # No sirve tendría que dejar la palabra y qitar sólo las comillas
                    # x = re.search(r"\'[a-zA-Z]+\'", texto)
                    # # print(x.group())
                    # while x:
                    #     texto = texto.replace(x.group(), " ")
                    #     x = re.search("'[a-zA-Z]+'", texto)

                    # elimina resto de caracteres que no son letras
                    elimina = r'<>=""\/().¿?¡!:,[]()%{}|;^'
                    for i in elimina:
                        texto = texto.replace(i, " ")

                    # elimina otros caracteres
                    elimina = [" - ", " -\n", "\n- ", " + ", " '", "' ", "'."]
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

                    # print(texto)
                    palabras = texto.split()
                    # print(palabras)
                    for palabra in palabras:
                        palabra_original = palabra
                        palabra = palabra.lower()

                        if (
                            not palabra in dicts
                            and not palabra_original in dicts
                            # and not palabra.isnumeric()
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
