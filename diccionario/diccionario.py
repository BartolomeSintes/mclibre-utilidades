import pathlib, html.parser, re

MINUSCULAS = True
MAYUSCULAS = False

DICT_ESPANOL = "diccionario_espanol.txt"
DICT_INGLES = "diccionario_ingles.txt"
DICT_HTML = "diccionario_html.txt"
DICT_CSS = "diccionario_css.txt"
DICT_SVG = "diccionario.txt"
DICT_MIS_CSS = "diccionario_mis_css.txt"
DICT_JAVASCRIPT = "diccionario_javascript.txt"
DICT_PYTHON = "diccionario_python.txt"
DICT_PHP = "diccionario.txt"
DICT_OTROS = "diccionario_otros.txt"

DICT_LIST = [
    [DICT_ESPANOL, "español", MINUSCULAS],
    [DICT_INGLES, "inglés", MINUSCULAS],
    [DICT_OTROS, "otros", MAYUSCULAS],
    [DICT_HTML, "html", MINUSCULAS],
    [DICT_CSS, "css", MINUSCULAS],
    [DICT_SVG, "svg", MINUSCULAS],
    [DICT_MIS_CSS, "mis-css", MINUSCULAS],
    [DICT_JAVASCRIPT, "js", MINUSCULAS],
    [DICT_PYTHON, "py", MINUSCULAS],
    [DICT_PHP, "php", MINUSCULAS],
]

ORIGEN_HTML = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\htmlcss"
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
    # Carga diccionarios
    total_palabras = 0
    for i in DICT_LIST:
        if i[2] == MINUSCULAS:
            dicts = []
            # print(f"Carga {i[1]}")
            if pathlib.Path(i[0]).exists():
                with open(i[0], "r", encoding="utf-8") as fichero:
                    palabras = fichero.read().split()
                dicts += palabras
                # print(f"El diccionario contine {len(dicts)}.")
                dicts.sort(reverse=True)
                for j in range(len(dicts)-1, -1, -1):
                    if dicts[j][0].lower() != dicts[j][0]:
                        busca = dicts[j][0].lower() + dicts[j][1:]
                        k = j
                        while k > 0:
                            # print(f"{k} ", end="")
                            if dicts[k] == busca:
                                # print(f"Repetida: {dicts[j]} {dicts[k]}")
                                del dicts[j]
                                k = 0
                            k -= 1
                # print(f"El diccionario contine {len(dicts)}.")
                for j in range(len(dicts)):
                    if len(dicts[j]) > 1 and dicts[j][0].lower() != dicts[j][0] and dicts[j][1].lower() == dicts[j][1]:
                        dicts[j] = dicts[j][0].lower() + dicts[j][1:]
                        # print(f"Cambia {dicts[j]}")
                    if len(dicts[j]) == 1 and dicts[j][0].lower() != dicts[j][0]:
                        dicts[j] = dicts[j][0].lower()
                        # print(f"Cambia {dicts[j]}")
                dicts.sort()
                total_palabras += len(dicts)
                # print(f"Diccionarios: {dicts}")
            with open(i[0], "w", encoding="utf-8") as fichero_dic:
                for palabra in dicts:
                    print(f"{palabra} ", file=fichero_dic)
    print(f"Los diccionarios contiene ahora {total_palabras} términos.")

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
                        self.lista_urls += [f'{i[1]}="{j[1]}"']
                        # print(f"encontrado {i[0]}, {i[1]}")


def elimina_urls(filename):
    with open(filename, "r", encoding="utf-8") as fichero:
        texto = fichero.read()
    parser = MyHTMLParser()
    parser.feed(texto)
    return parser.lista_urls


def main():
    estadisticas()

    # Carga diccionarios
    dicts = []
    for i in DICT_LIST:
        if pathlib.Path(i[0]).exists():
            with open(i[0], "r", encoding="utf-8") as fichero:
                palabras = fichero.read().split()
            dicts += palabras
    dicts_excepciones = []
    for i in DICT_LIST:
        if i[2] == MAYUSCULAS:
            if pathlib.Path(i[0]).exists():
                with open(i[0], "r", encoding="utf-8") as fichero:
                    palabras = fichero.read().split()
                dicts_excepciones += palabras
    # print(f"Diccionarios: {dicts}")

    print("Análisis")
    for extension in EXTENSIONES:
        contador = 0
        seguir_incluyendo = True
        for filename in pathlib.Path(ORIGEN_HTML).rglob(f"**/*.{extension}"):
            if seguir_incluyendo:
                contador += 1
                print()
                print(filename)
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
                    # elimina números con unidades
                    unidades = ["%", "px", "em", "rem", "pt", "in", "pc", "cm", "ex", "ch"]
                    for i in unidades:
                        x = re.search(r"-?[\d\.\d]+"+i, texto)
                        while x:
                            # print(x.group())
                            texto = texto.replace(x.group(), " ")
                            x = re.search(r"-?[\d\.\d]+"+i, texto)
                    # Tengo que eliminar primero los #RGB de 6 y luego cualquiera
                    # porque si no eliminaba #000 y #FFF y se quedaban tres caracteres sueltos
                    # elimina códigos de colores #RGB
                    x = re.search(r"#[0-9a-fA-F]{6}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"#[0-9a-fA-F]{6}", texto)
                    # elimina códigos de colores #RGB
                    x = re.search(r"#[0-9a-fA-F]+", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"#[0-9a-fA-F]+", texto)
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
                    # elimina números sin unidades
                    x = re.search(r"\s[0-9]+\s", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(r"\s[0-9]+\s", texto)
                    # elimina urls
                    for i in urls_para_eliminar:
                        texto = texto.replace(i, " ")
                    # elimina entidades numéricas
                    x = re.search("&amp;[#0-9a-zA-Z]+;", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("&amp;[#0-9a-zA-Z]+;", texto)
                    x = re.search("&[#0-9a-zA-Z]+;", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("&[#0-9a-zA-Z]+;", texto)
                    # elimina caracteres que no son letras
                    elimina = '<>=""\/().¿?¡!:,;[]()%{}|^'
                    for i in elimina:
                        texto = texto.replace(i, " ")
                    # elimina otros caracteres
                    elimina = [" - ", " -\n", "\n- ", " + "]
                    for i in elimina:
                        texto = texto.replace(i, " ")
                    # elimina saltos de línea y espacios
                    texto = texto.replace("\n", " ")
                    texto = texto.replace("\r", " ")
                    x = re.search("  +", texto)
                    while x:
                        texto = texto.replace(x.group(), " ")
                        x = re.search("  +", texto)

                    # print(texto)
                    palabras = texto.split()
                    # print(palabras)
                    for palabra in palabras:
                        palabra_original = palabra
                        if not palabra in dicts_excepciones:
                            if len(palabra) > 1 and palabra[0].lower() != palabra[0] and palabra[1].lower() == palabra[1]:
                                palabra = palabra[0].lower() + palabra[1:]
                                # print(f"Cambia {dicts[j]}")
                            if len(palabra) == 1 and palabra[0].lower() != palabra[0]:
                                palabra = palabra.lower()

                        if not palabra in dicts and not palabra.isnumeric() and seguir_incluyendo:
                            print("0: Saltar - ", end="")
                            for _ in range(len(DICT_LIST)):
                                print(f"{_+1}: {DICT_LIST[_][1]} - ", end="")
                            print("x: SALIR")
                            print()
                            print(palabra)
                            print()
                            incluir = input("Incluir? ")
                            if incluir == "x":
                                seguir_incluyendo = False
                            elif DICT_LIST[int(incluir) - 1][0] == DICT_OTROS:
                                with open(
                                    DICT_LIST[int(incluir) - 1][0], "a", encoding="utf-8"
                                ) as fichero_dic:
                                    print(f"{palabra_original} ", file=fichero_dic)
                                dicts += [palabra_original]
                                dicts_excepciones += [palabra_original]
                            elif 0 < int(incluir) < len(DICT_LIST):
                                with open(
                                    DICT_LIST[int(incluir) - 1][0], "a", encoding="utf-8"
                                ) as fichero_dic:
                                    print(f"{palabra} ", file=fichero_dic)
                                dicts += [palabra]

    ordena_diccionarios()

if __name__ == "__main__":
    main()
