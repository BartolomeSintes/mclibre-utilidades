import pathlib, html.parser, re

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
    [DICT_ESPANOL, "español"],
    [DICT_INGLES, "inglés"],
    [DICT_OTROS, "otros"],
    [DICT_HTML, "html"],
    [DICT_CSS, "css"],
    [DICT_SVG, "svg"],
    [DICT_MIS_CSS, "mis-css"],
    [DICT_JAVASCRIPT, "js"],
    [DICT_PYTHON, "py"],
    [DICT_PHP, "php"],
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
    # print(f"Diccionarios: {dicts}")

    print("Análisis")
    for extension in EXTENSIONES:
        contador = 0
        for filename in pathlib.Path(ORIGEN_HTML).rglob(f"**/*.{extension}"):
            contador += 1
            print()
            print(filename)
            urls_para_eliminar = elimina_urls(filename)
            with open(filename, "r", encoding="utf-8") as fichero:
                texto = fichero.read()
                # elimina números con unidades
                unidades = ["%", "px", "em", "rem"]
                for i in unidades:
                    x = re.search(f"[\d\.\d]+{i}", texto)
                    while x:
                        # print(x.group())
                        texto = texto.replace(x.group(), " ")
                        x = re.search(f"[\d\.\d]+{i}", texto)
                # elimina atributos que incluyen urls
                for i in urls_para_eliminar:
                    texto = texto.replace(i, " ")
                # elimina entidades numéricas
                elimina = [" - ", " -\n", "&lt;", "&gt;"]
                for i in elimina:
                    texto = texto.replace(i, " ")
                # elimina caracteres que no son letras
                elimina = '<>=""\'/().¿?¡!:,;[]()%'
                for i in elimina:
                    texto = texto.replace(i, " ")
                palabras = texto.split()
                print(palabras)
                for palabra in palabras:
                    if not palabra in dicts and not palabra.isnumeric():
                        print("0: Saltar - ", end="")
                        for _ in range(len(DICT_LIST)):
                            print(f"{_+1}: {DICT_LIST[_][1]} - ", end="")
                        print("x: SALIR")
                        print()
                        print(palabra)
                        print()
                        incluir = input("Incluir? ")
                        if incluir == "x":
                            exit(0)
                        elif 0 < int(incluir) < len(DICT_LIST):
                            with open(
                                DICT_LIST[int(incluir) - 1][0], "a", encoding="utf-8"
                            ) as fichero_dic:
                                print(f"{palabra} ", file=fichero_dic)
                            dicts += [palabra]


if __name__ == "__main__":
    main()
