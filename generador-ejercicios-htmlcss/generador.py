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
            # Añade salto de línea al final de CSS por si no lo hay
            ficheros_css[i] = re.sub(r"\Z", "\n", ficheros_css[i])
    return {"html": ficheros_html, "css": ficheros_css}


def graba_ficheros(ficheros, n):
    p = pathlib.Path(f"{DIR_FILES}/{n}")
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)
    for i in ficheros["html"]:
        print(f"Guardo {i}")
        with open(f"{DIR_FILES}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["html"][i])
    for i in ficheros["css"]:
        print(f"Guardo {i}")
        with open(f"{DIR_FILES}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["css"][i])


def quita_etiqueta(textos, etiquetas):
    for i in textos.keys():
        print("Quito etiquetas: ", end="")
        for etiqueta in etiquetas:
            print(etiqueta, end=" ")
            textos[i] = re.sub(f"<{etiqueta}>", "", textos[i])
            textos[i] = re.sub(f"<{etiqueta} [^>]*>", "", textos[i])
            textos[i] = re.sub(f"</{etiqueta}>", "", textos[i])
        print()
    return textos


def quita_entidades_numericas(textos):
    for i in textos.keys():
        print("Quito entidades numéricas")
        textos[i] = re.sub("&#[0-9a-f]+;", "", textos[i])
        print()
    return textos


def quita_propiedad(textos, propiedades):
    for i in textos.keys():
        print(f"Quito propiedades: ", end="")
        for propiedad in propiedades:
            print(propiedad, end=" ")
            textos[i] = re.sub(f"{propiedad}[^;]*;", "", textos[i])
        print()
    return textos


def quita_regla_arroba(textos, reglas):
    for i in textos.keys():
        print(f"Quito reglas arroba: ", end="")
        for regla in reglas:
            print(regla, end=" ")
            textos[i] = re.sub(f"@{regla}[^}}]*}}", "", textos[i])
        print()
    return textos


def quita_lineas_vacias(textos):
    for i in textos.keys():
        print(f"Quito líneas vacías")
        textos[i] = re.sub("[ ]+\n", "", textos[i])
        # Deja una línea en blanco a lo largo del fichero
        textos[i], cambios = re.subn("\n\n\n", "\n\n", textos[i])
        while cambios:
            textos[i], cambios = re.subn("\n\n\n", "\n\n", textos[i])
        # Deja una línea en blanco al final del fichero
        textos[i], cambios = re.subn(r"\n\n\Z", "\n", textos[i])
        while cambios:
            textos[i], cambios = re.subn(r"\n\n\Z", "\n", textos[i])
    return textos


def quita_reglas_vacias(textos):
    for i in textos.keys():
        print(f"Quito reglas vacías")
        textos[i] = re.sub("\n[^(\n{)]+{[\n ]*}\n", "", textos[i])
    return textos


def quita_sangrado(textos):
    for i in textos.keys():
        print(f"Quito sangrado")
        textos[i] = re.sub("\n  [ ]+", "\n  ", textos[i])
    return textos


def aplica_reglas(ficheros, paso):
    # print(paso)
    for accion in paso[0].keys():
        argumento = paso[0][accion]
        # print(accion, argumento)
        if accion == "remove-tag":
            ficheros["html"] = quita_etiqueta(ficheros["html"], argumento)
        elif accion == "remove-property":
            ficheros["css"] = quita_propiedad(ficheros["css"], argumento)
        elif accion == "remove-atrule":
            ficheros["css"] = quita_regla_arroba(ficheros["css"], argumento)
    ficheros["html"] = quita_entidades_numericas(ficheros["html"])
    ficheros["html"] = quita_lineas_vacias(ficheros["html"])
    ficheros["html"] = quita_sangrado(ficheros["html"])
    ficheros["css"] = quita_lineas_vacias(ficheros["css"])
    ficheros["css"] = quita_reglas_vacias(ficheros["css"])
    return ficheros


def main():
    # Carga sitio, revistas y ejemplares
    with open(PLANTILLA_JSON, encoding="utf-8") as json_file:
        plantilla = json.load(json_file)

    # print(plantilla)
    # print()
    ficheros = carga_ficheros(plantilla)
    for i in range(len(plantilla["steps"]), 0, -1):
        print(f"Hago paso {i}")
        ficheros = aplica_reglas(ficheros, plantilla["steps"][str(i)])
        graba_ficheros(ficheros, str(i))
        print()


if __name__ == "__main__":
    main()
