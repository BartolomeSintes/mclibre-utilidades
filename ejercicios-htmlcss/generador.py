import json, pathlib, re, shutil
from datetime import date


JSON_FILE = "ejercicios.json"
DIR_FILES_SOURCE = "files/source"
DIR_FILES_FINAL = "files/final"
OBL = "compulsory"
OBL_OPT = "optional"
INDEX_FILE = "index.html"
MES = [
    "",
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


def fecha_a_texto(numero):
    return (
        str(int(numero[8:10]))
        + " de "
        + MES[int(numero[5:7])]
        + " de "
        + str(numero[0:4])
    )


def elemento_con_clave__valor(lista, clave, valor):
    for i in lista:
        if i[clave] == valor:
            return i
    return None


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


def copia_ficheros(ejercicio, n):
    directorio_origen = f'{DIR_FILES_SOURCE}/{ejercicio["directory"]}'
    directorio_destino = f'{DIR_FILES_FINAL}/{ejercicio["directory"]}'
    # Copia imágenes y webfonts
    for tipo in ["img", "font"]:
        for i in ejercicio["files"][tipo]:
            if i["directory"] == "":
                p = pathlib.Path(f"{directorio_destino}/{n}")
            else:
                p = pathlib.Path(f'{directorio_destino}/{n}/{i["directory"]}')
                p.mkdir(parents=True, exist_ok=True)
            print("Guardo html: ", end="")
            for j in i["files"]:
                shutil.copy2(
                    f'{directorio_origen}/{i["directory"]}/{j}',
                    f'{directorio_destino}/{n}/{i["directory"]}/{j}',
                )


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
        textos[i] = re.sub("&#[x0-9a-fA-F]+;", "", textos[i])


def sustituye_entidades_caracter(textos, step):
    if step == 1:
        for i in textos.keys():
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
        elif accion == "other":
            for i in paso["other"]:
                if i == "numeric-entity":
                    quita_entidades_numericas(ficheros["html"])
                elif i == "character-entity":
                    sustituye_entidades_caracter(ficheros["html"], i)
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
    quita_sangrado(ficheros["html"])


def main():
    # Carga json
    with open(JSON_FILE, encoding="utf-8") as file:
        json_file = json.load(file)
    steps = json_file["steps"]
    step_sets = json_file["step-sets"]
    exercises = json_file["exercises"]
    exercise_sets = json_file["exercise-sets"]

    # Usuario elige Grupo de ejercicios a procesar
    print("Elija un grupo de ejercicios:")
    for i, exercise_set in enumerate(exercise_sets):
        print(f'({i+1}) {exercise_set["name"]}')
    selected_set = int(input()) - 1
    while selected_set not in range(0, len(exercise_sets)):
        selected_set = int(input()) - 1
    print()

    # Genera pasos intermedios y plantilla de cada ejercicio seleccionado
    for exercise in exercise_sets[selected_set]["pages"]:
        exercise_details = elemento_con_clave__valor(
            exercises, "directory", exercise["name"]
        )
        exercise_steps = elemento_con_clave__valor(step_sets, "name", exercise["steps"])
        ficheros = carga_ficheros(exercise_details)
        borra_directorio_final(exercise_details)
        # Si sólo queremos elementos obligatorios, primero elimina los optativos
        if exercise["level"] == OBL:
            for i in range(len(exercise_steps["steps"]) - 1, -1, -1):
                for j in exercise_steps["steps"][i]:
                    if "optional" in steps[j]:
                        aplica_reglas(ficheros, steps[j]["optional"])
        dir_name = []
        for i in range(len(exercise_steps["steps"])):
            dir_name_tmp = f"{i:02d}"
            for j in exercise_steps["steps"][i]:
                dir_name_tmp += f"-{j}"
            dir_name += [dir_name_tmp]
        dir_name[0] = f'{exercise["name"]}-plantilla'

        for i in range(len(exercise_steps["steps"]) - 1, 0, -1):
            for j in exercise_steps["steps"][i]:
                print(f"Hago paso {i}")
                if "compulsory" in steps[j]:
                    aplica_reglas(ficheros, steps[j]["compulsory"])
                if "optional" in steps[j]:
                    aplica_reglas(ficheros, steps[j]["optional"])
                limpia(ficheros, i)
            graba_ficheros(exercise_details, ficheros, dir_name[i - 1])
            print()
            # Copia imágenes y webfonts
            copia_ficheros(exercise_details, dir_name[i - 1])

        # Genera paso final (igual que original, pero quitando optativos en su caso)
        ficheros = carga_ficheros(exercise_details)
        # Si sólo queremos elementos obligatorios, primero elimina los optativos
        if exercise["level"] == OBL:
            for i in range(len(exercise_steps["steps"]) - 1, 0, -1):
                for j in exercise_steps["steps"][i]:
                    if "optional" in steps[j]:
                        aplica_reglas(ficheros, steps[j]["optional"])
        print(f"Hago paso final")
        graba_ficheros(exercise_details, ficheros, dir_name[-1])
        # Copia imágenes y webfonts
        copia_ficheros(exercise_details, dir_name[-1])
        print()

        # Comprime plantilla
        directorio_zip = (
            f'{DIR_FILES_FINAL}/{exercise_details["directory"]}/{dir_name[0]}'
        )
        shutil.make_archive(f"{directorio_zip}", "zip", directorio_zip)

    # Genera índice
    t = ""
    t += "<!DOCTYPE html>\n"
    t += '<html lang="es">\n'
    t += "<head>\n"
    t += '  <meta charset="utf-8">\n'
    t += f"  <title>Generador ejercicios HTML/CSS. Bartolomé Sintes Marco. www.mclibre.org</title>\n"
    t += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    t += "  <style>html { font-family: sans-serif; font-size: 150%; } li { margin-bottom: 20px; }</style>\n"
    t += "</head>\n"
    t += "\n"
    t += "<body>\n"
    t += f"  <h1>Ejercicios progresivos</h1>\n"

    t += "  <ul>\n"

    for n in exercise_sets[selected_set]["pages"]:
        dir_name = []
        for i in range(len(exercise_steps["steps"])):
            dir_name_tmp = f"{i:02d}"
            for j in exercise_steps["steps"][i]:
                dir_name_tmp += f"-{j}"
            dir_name += [dir_name_tmp]
        dir_name[0] = f'{exercise_details["directory"]}-plantilla'

        t += "    <li>\n"
        t += f'      {exercise_details["name"]}<br>\n'
        t += f'      <a href="{exercise_details["directory"]}/{dir_name[0]}.zip">Plantilla</a>\n'
        t += f'      (<a href="{exercise_details["directory"]}/{dir_name[0]}/{exercise_details["files"]["html"][0]}">html</a> -\n'
        t += f'      <a href="{exercise_details["directory"]}/{dir_name[0]}/{exercise_details["files"]["css"][0]}">css</a>) -\n'
        for i in range(1, len(exercise_steps["steps"])):
            t += f'      <a href="{exercise_details["directory"]}/{dir_name[i]}/{exercise_details["files"]["html"][0]}">T{i}</a> -\n'
        t += "    </li>\n"
    t += "  </ul>\n"
    t += "\n"
    t += '  <address id="ultmod">\n'
    t += "    Autor: Bartolomé Sintes Marco<br>\n"
    t += f"    Última modificación de esta página: {fecha_a_texto(str(date.today()))}\n"
    t += "  </address>\n"
    t += "</body>\n"
    t += "</html>\n"
    with open(f"{DIR_FILES_FINAL}/{INDEX_FILE}", "w", encoding="utf-8") as fichero:
        fichero.write(t)


if __name__ == "__main__":
    main()
