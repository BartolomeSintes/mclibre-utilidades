import json, pathlib, re, shutil

JSON_STEPS = "ejercicios-1.json"
JSON_FILES = "ejercicios-2.json"
DIR_FILES = "files"
OBL = "1"
OBL_OPT = "2"


def carga_ficheros(ficheros):
    ficheros_html = {}
    dir = f'{DIR_FILES}/{ficheros["directory"]}'
    for i in ficheros["files"]["html"]:
        with open(f"{dir}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_html[i] = fichero.read()
    ficheros_css = {}
    for i in ficheros["files"]["css"]:
        with open(f"{dir}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_css[i] = fichero.read()
            # Añade salto de línea al final de CSS por si no lo hay
            ficheros_css[i] = re.sub(r"\Z", "\n", ficheros_css[i])
    return {"html": ficheros_html, "css": ficheros_css}


def graba_ficheros(ficheros, n):
    p = pathlib.Path(f"{DIR_FILES}/{n}")
    if p.exists():
        shutil.rmtree(p)
    p.mkdir(parents=True, exist_ok=True)
    print("Guardo html: ", end="")
    for i in ficheros["html"]:
        print(i, end=" ")
        with open(f"{DIR_FILES}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["html"][i])
    print()
    print("Guardo css: ", end="")
    for i in ficheros["css"]:
        print(i, end=" ")
        with open(f"{DIR_FILES}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["css"][i])
    print()


def quita_etiqueta(textos, etiquetas):
    print("Quito etiquetas: ", end="")
    for etiqueta in etiquetas:
        print(etiqueta, end=" ")
        for i in textos.keys():
            textos[i] = re.sub(f"<{etiqueta}>", "", textos[i])
            textos[i] = re.sub(f"<{etiqueta} [^>]*>", "", textos[i])
            textos[i] = re.sub(f"</{etiqueta}>", "", textos[i])
    print()
    return textos


def quita_entidades_numericas(textos):
    for i in textos.keys():
        # print("Quito entidades numéricas")
        textos[i] = re.sub("&#[0-9a-f]+;", "", textos[i])
    return textos


def quita_propiedad(textos, propiedades):
    print("Quito propiedades: ", end="")
    for propiedad in propiedades:
        print(propiedad, end=" ")
        for i in textos.keys():
            # Busca la propiedad desde el principio de la línea para que no
            # borre @font-face al borrar font o el right de border-right al borrar right
            # Necesita el flag=re.MULTILINE para hacer caso del ^ inicial
            # La línea que contenía una propiedad la dejo con un par de espacios
            # para que se distinga de las líneas en blanco que separan reglas
            cadena = f"^[ ]*{propiedad}[ .#:][^;]*;"
            textos[i] = re.sub(cadena, "  ", textos[i], flags=re.MULTILINE)
    print()
    return textos


def quita_regla_arroba(textos, reglas):
    print("Quito reglas arroba: ", end="")
    for regla in reglas:
        for i in textos.keys():
            print(regla, end=" ")
            textos[i] = re.sub(f"@{regla}[^}}]*}}", "", textos[i])
    print()
    return textos


def quita_lineas_vacias(textos):
    for i in textos.keys():
        # print("Quito líneas vacías")
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
        # print("Quito reglas vacías")
        textos[i] = re.sub("\n[^(\n{)]+{[\n ]*}\n", "", textos[i])
    return textos


def quita_sangrado(textos):
    for i in textos.keys():
        # print("Quito sangrado")
        textos[i] = re.sub("\n  [ ]+", "\n  ", textos[i])
    return textos


def aplica_reglas(ficheros, paso):
    for accion in paso.keys():
        argumento = paso[accion]
        if accion == "tag":
            ficheros["html"] = quita_etiqueta(ficheros["html"], argumento)
        elif accion == "property":
            ficheros["css"] = quita_propiedad(ficheros["css"], argumento)
        elif accion == "atrule":
            ficheros["css"] = quita_regla_arroba(ficheros["css"], argumento)
    ficheros["html"] = quita_lineas_vacias(ficheros["html"])
    ficheros["css"] = quita_lineas_vacias(ficheros["css"])
    ficheros["css"] = quita_reglas_vacias(ficheros["css"])
    return ficheros


def limpia(ficheros):
    ficheros["html"] = quita_entidades_numericas(ficheros["html"])
    ficheros["html"] = quita_sangrado(ficheros["html"])
    return ficheros


def main():
    # Carga json pasos
    with open(JSON_STEPS, encoding="utf-8") as json_file:
        json_steps = json.load(json_file)
    steps = json_steps["steps"]

    # Usuario elige Elementos obligatorios / Elementos obligatorios y opcionales
    print("Elija una opción:")
    print("(1) sólo elementos obligatorios:")
    print("(2) elementos obligatorios y optativos")
    nivel = input()
    while nivel != OBL and nivel != OBL_OPT:
        nivel = input()

    # Carga json ficheros
    with open(JSON_FILES, encoding="utf-8") as json_file:
        json_files = json.load(json_file)
    ejercicios = json_files["pages"]

    # Usuario elige Ejercicio a procesar
    print("Elija un ejercicio:")
    for i in ejercicios:
        print(f'({i}) {ejercicios[i]["name"]}')
    ejercicio = input()
    while ejercicio not in ejercicios:
        ejercicio = input()

    # Genera pasos intermedios
    ficheros = carga_ficheros(ejercicios[ejercicio])
    for i in range(len(steps), 0, -1):
        print(f"Hago paso {i}")
        ficheros = aplica_reglas(ficheros, steps[str(i)]["compulsory"])
        if "optional" in steps[str(i)]:
            ficheros = aplica_reglas(ficheros, steps[str(i)]["optional"])
        limpia(ficheros)
        graba_ficheros(ficheros, str(i))
        print()

    # Genera paso final (igual que original, pero quitando optativos en su caso)
    ficheros = carga_ficheros(ejercicios[ejercicio])
    final = len(steps) + 1
    print(f"Hago paso {final} (final)")
    if nivel == OBL:
        for i in range(len(steps), 0, -1):
            if "optional" in steps[str(i)]:
                ficheros = aplica_reglas(ficheros, steps[str(i)]["optional"])
    graba_ficheros(ficheros, str(final))
    print()


if __name__ == "__main__":
    main()
