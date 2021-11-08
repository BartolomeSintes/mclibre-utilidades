import gendef
import sys

emoji_test = []
emoji_data = emoji_data_simbolos = emoji_data_componentes = []
emoji_variation_sequences = []


def importa_fichero_emoji_test():
    print(f"TRATANDO {gendef.FICHERO_EMOJI_TEST}")
    print(f"  importando ...")
    importado = []
    with open(
        gendef.UNICODE_ORIGINAL_DIR + gendef.FICHERO_EMOJI_TEST,
        mode="r",
        encoding="utf-8",
    ) as f:
        grupo = ""
        subgrupo = ""
        for line in f:
            if line[:7] == "# group":
                grupo = line[9:-1]
            elif line[:10] == "# subgroup":
                subgrupo = line[12:-1]
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
                linea += [grupo, subgrupo]
                importado += [linea]
    print(f"  comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "fully-qualified",
            "unqualified",
            "minimally-qualified",
            "component",
        ]:
            print("Valor inesperado en campo [1]:", elemento[1])
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
            print("Valor inesperado en campo [3]:", elemento[3])

    return importado


def importa_fichero_emoji_data():
    print(f"TRATANDO {gendef.FICHERO_EMOJI_DATA}")
    print(f"  importando ...")
    importado = []
    with open(
        gendef.UNICODE_ORIGINAL_DIR + gendef.FICHERO_EMOJI_DATA,
        mode="r",
        encoding="utf-8",
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
            print("Valor inesperado en campo [1]:", elemento[1])
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
            print("Valor inesperado en campo [2]:", elemento[2])
    # No sé por qué incluyen elementos reservados. Si en las agrupaciones están todos reservados, los puedo eliminar
    # pero si solo están reservados una parte, tendré que mirar a mano cuáles están reservados
    print(
        "  eliminando elementos reservados cuando todos los de una agrupación están reservados ..."
    )
    for i in range(len(importado) - 1, -1, -1):
        if importado[i][5][:9] == "<reserved":
            del importado[i]
    print("  separando agrupaciones ...")
    for i in range(len(importado) - 1, -1, -1):
        if importado[i][3] > 1:
            corta = importado[i][0].find(".")
            valor_inicial = int(importado[i][0][:corta], 16)
            for j in range(importado[i][3]):
                valor = valor_inicial + j
                valor = f"{valor:04x}".upper()
                tmp = importado[i][:]
                tmp[:0] = [valor]
                del tmp[1]
                importado[i + j + 1 : i + j + 1] = [tmp]
            del importado[i]
            # print()
    # # Esto está pendiente de hacer
    # # Elimino los elementos que son componentes que van a parar a emoji_data_componentes
    # print("  separando componentes ...")
    # encontrados = []
    # for i in range(len(importado)-1, -1, -1):
    #     encontrado = False
    #     # print(importado[i][0])
    #     for j in range(len(gendef.emoji_data_componentes_auxiliar)):
    #         if importado[i][1] == "Emoji_Component" and importado[i][0] == gendef.emoji_data_componentes_auxiliar[j]:
    #             # print (importado[i][0], gendef.emoji_data_componentes_auxiliar[j])
    #             encontrado = True
    #             # input()
    #     if encontrado:
    #         encontrados += [importado[i]]
    #         del(importado[i])
    # if len(encontrados) == len(gendef.emoji_data_componentes_auxiliar):
    #     print ("    Encontrados todos los componentes")
    # else:
    #     print(f"    CUIDADO: en vez de {len(gendef.emoji_data_componentes_auxiliar)} he encontrado {len(encontrados)}")
    # # for i in encontrados:
    # #     print(i)
    # sys.exit()

    # Como hay elementos agrupados y los voy a separar, no tiene sentido mantener los caracteres ni sus nombres porque solo están en primero y el último
    print("  eliminando campo caracteres ...")
    for i in range(len(importado) - 1, -1, -1):
        del importado[i][5]
        del importado[i][4]
        del importado[i][3]
    # print("  eliminando elementos reservados cuando sólo una parte están reservados ...")
    # print("    CUIDADO ESTÁ POR HACER")
    # encontrados = []
    # for i in range(len(importado)):
    #     encontrado = False
    #     # print(importado[i][0])
    #     for j in range(len(emoji_test)):
    #         if len(emoji_test[j][0]) == 1:
    #             if importado[i][0] == emoji_test[j][0][0]:
    #                 encontrado = True
    #     if not encontrado:
    #         encontrados += [importado[i][0]]
    # print(len(encontrados))
    # print(encontrados[0:300])

    return importado


def importa_fichero_emoji_variation_sequence():
    print(f"TRATANDO {gendef.FICHERO_EMOJI_VARIATION_SEQUENCES}")
    print(f"  importando ...")
    importado = []
    with open(
        gendef.UNICODE_ORIGINAL_DIR + gendef.FICHERO_EMOJI_VARIATION_SEQUENCES,
        mode="r",
        encoding="utf-8",
    ) as f:
        for line in f:
            if line[0] != "#" and line[0] != "\n":
                linea = []
                resto = line
                # códigos
                corta = line.find(";")
                linea += [resto[:corta].strip()]
                linea[0] = linea[0].split(" ")
                resto = [resto[corta + 1 :].strip()]
                # text / emoji style
                corta = resto[0].find(";")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                # número
                corta = resto[0].find("(")
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find(")")
                linea += [resto[0][:corta].strip()]
                # nombre
                linea += [resto[0][corta + 1 :].strip()]
                importado += [linea]
    print(f"  comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "text style",
            "emoji style",
        ]:
            print("Valor inesperado en campo [1]:", elemento[1])
        if elemento[2] not in [
            "1.1",
            "3.0",
            "3.2",
            "4.0",
            "4.1",
            "5.1",
            "5.2",
            "6.0",
            "7.0",
        ]:
            print("Valor inesperado en campo [2]:", elemento[2])

    return importado


def exporta_matrices():
    destino = gendef.FICHERO_IMPORTADO
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
        # Guarda emoji_variation_sequences
        t += "emoji_variation_sequences = [\n"
        for i in emoji_variation_sequences:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)
    print()

    print("Programa terminado.")


def main():
    global emoji_test, emoji_data, emoji_variation_sequences
    emoji_test = importa_fichero_emoji_test()
    emoji_data = importa_fichero_emoji_data()
    emoji_variation_sequences = importa_fichero_emoji_variation_sequence()
    exporta_matrices()


if __name__ == "__main__":
    main()
