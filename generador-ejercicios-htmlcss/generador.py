import json, pathlib, re, shutil

JSON_STEPS = "ejercicios-1.json"
JSON_FILES = "ejercicios-2.json"
DIR_FILES_SOURCE = "files/source"
DIR_FILES_FINAL = "files/final"
OBL = "1"
OBL_OPT = "2"


def carga_ficheros(ejercicio):
    ficheros_html = {}
    directorio = f'{DIR_FILES_SOURCE}/{ejercicio["directory"]}'
    for i in ejercicio["files"]["html"]:
        with open(f"{directorio}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_html[i] = fichero.read()
    ficheros_css = {}
    for i in ejercicio["files"]["css"]:
        with open(f"{directorio}/{i}", "r", encoding="utf-8") as fichero:
            ficheros_css[i] = fichero.read()
            # Añade salto de línea al final de CSS por si no lo hay
            ficheros_css[i] = re.sub(r"\Z", "\n", ficheros_css[i])
    return {"html": ficheros_html, "css": ficheros_css}


def borra_directorio_final(ejercicio):
    directorio = f'{DIR_FILES_FINAL}/{ejercicio["directory"]}'
    p = pathlib.Path(directorio)
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)


def graba_ficheros(ejercicio, ficheros, n):
    directorio = f'{DIR_FILES_FINAL}/{ejercicio["directory"]}'
    p = pathlib.Path(f"{directorio}/{n}")
    p.mkdir(parents=True, exist_ok=True)
    print("Guardo html: ", end="")
    for i in ficheros["html"]:
        print(i, end=" ")
        with open(f"{directorio}/{n}/{i}", "w", encoding="utf-8") as fichero:
            fichero.write(ficheros["html"][i])
    print()
    print("Guardo css: ", end="")
    for i in ficheros["css"]:
        print(i, end=" ")
        with open(f"{directorio}/{n}/{i}", "w", encoding="utf-8") as fichero:
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


def quita_entidades_numericas(textos):
    for i in textos.keys():
        # print("Quito entidades numéricas")
        textos[i] = re.sub("&#[0-9a-f]+;", "", textos[i])


def sustituye_entidades_caracter(textos, step):
    if step == 1:
        for i in textos.keys():
            print(textos[i])
            # print("Sustituyo entidades de carácter")
            textos[i] = re.sub("&lt;", "<", textos[i])
            textos[i] = re.sub("&gt;", ">", textos[i])
            textos[i] = re.sub("&amp;", "&", textos[i])


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
            # No sé si se debe hacer como en quita_propiedades_relacionadas, escapando la j
            # o como es una sola línea se hace la sustitución
            # propiedades_encontradas = re.findall(cadena, textos[i], flags=re.MULTILINE)
            # for j in propiedades_encontradas:
            #     print (f"Cadena: {j}")
            #     textos[i] = re.sub(re.escape(j), "  ", textos[i], flags=re.MULTILINE)
    print()


def quita_propiedades_relacionadas(textos, propiedades):
    print("Quito propiedades relacionadas: ", end="")
    for propiedad in propiedades:
        print(f'{propiedad["property"]}/{propiedad["related"]}', end=" ")
        patron_regla = f"^[^{{]*{{[^}}]*}}"
        propiedad_eliminar = f'^[ ]*{propiedad["property"]}[ .#:][^;]*;'
        propiedad_relacionada = f'^[ ]*{propiedad["related"]}[ .#:][^;]*;'
        for i in textos.keys():
            reglas_encontradas = re.findall(patron_regla, textos[i], flags=re.MULTILINE)
            for j in reglas_encontradas:
                if re.search(propiedad_eliminar, j, flags=re.MULTILINE) and re.search(
                    propiedad_relacionada, j, flags=re.MULTILINE
                ):
                    regla_cambiada = re.sub(
                        propiedad_eliminar, "  ", j, flags=re.MULTILINE
                    )
                    # IMPORTANTE: Hay que escapar j porque puede incluir % (y no se haría la susitutción)
                    textos[i] = re.sub(
                        re.escape(j), regla_cambiada, textos[i], flags=re.MULTILINE
                    )
    print()


def quita_regla_arroba(textos, reglas):
    print("Quito reglas arroba: ", end="")
    for regla in reglas:
        for i in textos.keys():
            print(regla, end=" ")
            textos[i] = re.sub(f"@{regla}[^}}]*}}", "", textos[i])
    print()


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


def quita_reglas_vacias(textos):
    for i in textos.keys():
        # print("Quito reglas vacías")
        textos[i] = re.sub("\n[^(\n{)]+{[\n ]*}\n", "", textos[i])


def quita_sangrado(textos):
    for i in textos.keys():
        # print("Quito sangrado")
        textos[i] = re.sub("\n  [ ]+", "\n  ", textos[i])


def aplica_reglas(ficheros, paso):
    for accion in paso.keys():
        argumento = paso[accion]
        if accion == "tag":
            quita_etiqueta(ficheros["html"], argumento)
        elif accion == "property":
            quita_propiedad(ficheros["css"], argumento)
        elif accion == "atrule":
            quita_regla_arroba(ficheros["css"], argumento)
        elif accion == "related-properties":
            quita_propiedades_relacionadas(ficheros["css"], argumento)
    quita_lineas_vacias(ficheros["html"])
    quita_lineas_vacias(ficheros["css"])
    quita_reglas_vacias(ficheros["css"])


def limpia(ficheros, step):
    if step == 1 or step == 2:
        quita_entidades_numericas(ficheros["html"])
    quita_sangrado(ficheros["html"])


def main():
    # Carga json pasos
    with open(JSON_STEPS, encoding="utf-8") as json_file:
        json_steps = json.load(json_file)
    steps = json_steps["steps"]

    # Usuario elige Elementos obligatorios / Elementos obligatorios y opcionales
    print("Elija una opción. El resultado final contiene:")
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
    print("(0) Todos los ejercicios")
    for i in ejercicios:
        print(f'({i}) {ejercicios[i]["name"]}')
    ejercicio = input()
    print(ejercicio)
    while ejercicio not in ["0"] + list(ejercicios.keys()):
        ejercicio = input()

    if ejercicio == "0":
        rango = list(ejercicios.keys())
    else:
        rango = [ejercicio]

    # Genera pasos intermedios
    for n in rango:
        ficheros = carga_ficheros(ejercicios[n])
        borra_directorio_final(ejercicios[n])
        # Si sólo queremos elementos obligatorios, primero elimina los optativos
        if nivel == OBL:
            for i in range(len(steps), 0, -1):
                if "optional" in steps[str(i)]:
                    aplica_reglas(ficheros, steps[str(i)]["optional"])
        for i in range(len(steps), 0, -1):
            print(f"Hago paso {i}")
            aplica_reglas(ficheros, steps[str(i)]["compulsory"])
            if "optional" in steps[str(i)]:
                aplica_reglas(ficheros, steps[str(i)]["optional"])
            limpia(ficheros, i)
            sustituye_entidades_caracter(ficheros["html"], i)
            graba_ficheros(ejercicios[n], ficheros, str(i))
            print()

        # Genera paso final (igual que original, pero quitando optativos en su caso)
        ficheros = carga_ficheros(ejercicios[n])
        # Si sólo queremos elementos obligatorios, primero elimina los optativos
        if nivel == OBL:
            for i in range(len(steps), 0, -1):
                if "optional" in steps[str(i)]:
                    aplica_reglas(ficheros, steps[str(i)]["optional"])
        final = len(steps) + 1
        print(f"Hago paso {final} (final)")
        graba_ficheros(ejercicios[n], ficheros, str(final))
        print()


if __name__ == "__main__":
    main()
