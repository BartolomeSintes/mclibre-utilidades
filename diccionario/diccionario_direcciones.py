# 2019-06-01
# Este programa lee todos los ficheros de un directorio y lista todas las URL por fichero
#
# Guarda el fichero como JSON
# El problema es que el fichero es muy grande debe haber muchas url repetidas
# además se cuelga leyendo ficheros md, svg y js (no con todos, pero con algunos, creo que he leído que
# si no están bien formados HTMLParser se engancha
#
# HTMLParser está en standradlib, pero se ve que es cutre


import pathlib, html.parser, json

DICT_URL = "diccionario_url.txt"

ORIGEN_HTML = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\htmlcss"
# ORIGEN_HTML = "C:/tmp/python-diccionario-prueba"

EXTENSIONES = ["html", "css", "svg"]


class MyHTMLParser(html.parser.HTMLParser):
    lista_urls = []

    def handle_starttag(self, tag, attrs):
        busca = [["a", "href"], ["img", "src"], ["link", "href"], ["svg", "xmlns"]]
        for i in busca:
            if tag == i[0]:
                for j in attrs:
                    if j[0] == i[1]:
                        self.lista_urls += [j[1]]


def main():
    print("Análisis")
    urls = []
    for extension in EXTENSIONES:
        contador = 0
        for filename in pathlib.Path(ORIGEN_HTML).rglob(f"**/*.{extension}"):
            contador += 1
            print()
            print(filename)
            with open(filename, "r", encoding="utf-8") as fichero:
                texto = fichero.read()
            # print(texto)
            parser = MyHTMLParser()
            parser.feed(texto)
            urls += [f"{filename.parent}\\{filename.name}", parser.lista_urls]
            parser.lista_urls = []

    with open(DICT_URL, "w") as salida:
        json.dump(urls, salida)
    print("Resultado")
    for _ in urls:
        print()
        print(_)


if __name__ == "__main__":
    main()
