import json, pathlib, re, shutil

PLANTILLA_JSON = "ejercicios-1.json"
DIR_FILES = "files"

def carga_ficheros(plantilla):
    ficheros_html = {}
    for i in plantilla["files"]["html"]:
        with open(f"{DIR_FILES}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_html[i] = fichero.read()
    ficheros_css = {}
    for i in plantilla["files"]["css"]:
        with open(f"{DIR_FILES}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_css[i] = fichero.read()
    return {"html": ficheros_html, "css": ficheros_css}

def graba_ficheros(ficheros, n):
    p = pathlib.Path(f"{DIR_FILES}/{n}")
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
    # print(ficheros)
    for i in ficheros["html"]:
        print(f"Guardo {i}")
        # print(i)
        # print(ficheros["html"][i])
        with open(f"{DIR_FILES}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["html"][i])


def quita_etiqueta(textos, etiqueta):
    for i in textos.keys():
        print(f"Quito etiqueta {etiqueta}")
        # print(textos[i])
        textos[i] = re.sub(f"<{etiqueta}[^>]*>", "", textos[i])
        textos[i] = re.sub(f"</{etiqueta}>", "", textos[i])
        # print(textos[i])
    return textos

def aplica_reglas(ficheros, paso):
    # print(paso)
    for i in paso:
        accion = next(iter(i.keys()))
        argumento = i[accion]
        # print(accion, argumento)
        if accion == "remove-tag":
            ficheros["html"] = quita_etiqueta(ficheros["html"], argumento)
    return ficheros


def main():
    # Carga sitio, revistas y ejemplares
    with open(PLANTILLA_JSON, encoding="utf-8") as json_file:
        plantilla = json.load(json_file)

    print(plantilla)
    print()
    ficheros = carga_ficheros(plantilla)
    print(plantilla["steps"])
    print()
    for i in plantilla["steps"]:
        print(f"Hago paso {i}")
        ficheros = aplica_reglas(ficheros, plantilla["steps"][i])
        graba_ficheros(ficheros, i)
        print()


if __name__ == "__main__":
    main()
