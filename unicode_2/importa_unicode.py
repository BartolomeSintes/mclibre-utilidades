UNICODE_ORIGINAL_DIR = "ficheros-originales-u14/"
FICHERO_EMOJI_TEST = "u14-emoji-test.txt"
FICHERO_EMOJI_ZWJ_SEQUENCES = "u14-emoji-zwj-sequences.txt"
FICHERO_EMOJI_VARIATION_SEQUENCES = "u14-emoji-variation-sequences.txt"
FICHERO_EMOJI_SEQUENCES = "u14-emoji-sequences.txt"
FICHERO_EMOJI_DATA = "u14-emoji-data.txt"
FICHERO_IMPORTADO = "u14.py"

def importa_fichero_emoji_test():
    print(f"TRATANDO {FICHERO_EMOJI_TEST}")
    print(f"  importando ...")
    importado = []
    with open(
        UNICODE_ORIGINAL_DIR + FICHERO_EMOJI_TEST, mode="r", encoding="utf-8"
    ) as f:
        for line in f:
            if line[0] != "#" and line[0] != "\n":
                linea = []
                # print(line)
                corta = line.find(";")
                resto = line
                linea += [resto[:corta].strip()]
                linea[0] = linea[0].split(" ")
                resto = [resto[corta + 1 :].strip()]
                # He intentado usar split("#") pero me daba error con algunos caracteres porque lo detectaba varias veces
                corta = resto[0].find("#")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("E")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find(" ")
                linea += [resto[0][:corta].strip()]
                linea += [resto[0][corta + 1 :].strip()]
                importado += [linea]
    print(f"  comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "fully-qualified",
            "unqualified",
            "minimally-qualified",
            "component",
        ]:
            print("Valor inesperado en campo [1]:", i[1])
        if elemento[3] not in [
            "0.6",
            "0.7",
            "1.0",
            "2.0",
            "3.0",
            "4.0",
            "5.0",
            "11.0",
            "12.0",
            "12.1",
            "13.0",
            "13.1",
            "14.0",
        ]:
            print("Valor inesperado en campo [3]:", i[1])
    print()
    return importado

def importa_fichero_emoji_data():
    print(f"TRATANDO {FICHERO_EMOJI_DATA}")
    print(f"  importando ...")
    importado = []
    with open(
        UNICODE_ORIGINAL_DIR + FICHERO_EMOJI_DATA, mode="r", encoding="utf-8"
    ) as f:
        for line in f:
            if line[0] != "#" and line[0] != "\n":
                linea = []
                # print(line)
                corta = line.find(";")
                resto = line
                linea += [resto[:corta].strip()]
                # linea[0] = linea[0].split(" ")
                resto = [resto[corta + 1 :].strip()]
                corta = resto[0].find("#")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("[")
                linea += [resto[0][1:corta].strip()]
                resto = [resto[0][corta:].strip()]
                corta = resto[0].find("(")
                linea += [resto[0][:corta].strip()]
                linea[3] = int(linea[3][1:-1])
                resto = [resto[0][corta:].strip()]
                corta = resto[0].find(" ")
                linea += [resto[0][:corta].strip()]
                linea[4] = linea[4][1:-1]
                linea += [resto[0][corta:].strip()]
                importado += [linea]
    print(f"  comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "Emoji",
            "Emoji_Component",
            "Emoji_Modifier",
            "Emoji_Modifier_Base",
            "Emoji_Presentation",
            "Extended_Pictographic",
        ]:
            print("Valor inesperado en campo [1]:", i[1])
        if elemento[2] not in [
            "0.0",
            "0.6",
            "0.7",
            "1.0",
            "2.0",
            "3.0",
            "4.0",
            "5.0",
            "11.0",
            "12.0",
            "12.1",
            "13.0",
            "13.1",
            "14.0",
        ]:
            print("Valor inesperado en campo [2]:", i[1])
    # Como hay elementos agrupados y los voy a separar, no tiene sentido mantenerlos porque solo están en primero y el último
    print("  eliminando campo caracteres ...")
    for i in range(len(importado)-1, -1, -1):
        del importado[i][4]
    print("  eliminando elementos reservados ...")
    for i in range(len(importado)-1, -1, -1):
        if importado[i][4][:9] == "<reserved":
            del(importado[i])
    print()
    return importado


def exporta_matrices(emoji_test, emoji_data):
    destino = FICHERO_IMPORTADO
    print(f"CREANDO {destino}")

    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda emoji_test
        t += "emoji_test = [\n"
        for i in emoji_test:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        # Guarda emoji_data
        t += "emoji_data = [\n"
        for i in emoji_data:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)
    print()

    print("Programa terminado.")


def main():
    emoji_test = emoji_data = []
    emoji_test = importa_fichero_emoji_test()
    emoji_data = importa_fichero_emoji_data()
    exporta_matrices(emoji_test, emoji_data)


if __name__ == "__main__":
    main()
