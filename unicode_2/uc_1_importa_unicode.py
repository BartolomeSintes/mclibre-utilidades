# Este programa importa los ficheros txt
# - emoji-test.txt
# - emoji-data.txt
# - emoji-variation-sequences.txt
# - emoji-zwj-sequences.txt
# - emoji-sequences.txt

import ucdef
import os
import pathlib
import sys

emoji_test = []
emoji_data = emoji_data_simbolos = emoji_data_componentes = []
emoji_variation_sequences = []
emoji_zwj_sequences = []
emoji_sequences = []
derived_name = []

def importa_fichero_emoji_test():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_EMOJI_TEST}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_EMOJI_TEST,
        mode="r",
        encoding="utf-8",
    ) as f:
        grupo = ""
        subgrupo = ""
        for line in f:
            if line[:7] == "# group":
                grupo = line[9:-1].replace("&amp;", "&")
            elif line[:10] == "# subgroup":
                subgrupo = line[12:-1].replace("&amp;", "&")
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
    print(f"    comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "fully-qualified",
            "unqualified",
            "minimally-qualified",
            "component",
        ]:
            print("    Valor inesperado en campo [1]:", elemento[1])
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
            print("    Valor inesperado en campo [3]:", elemento[3])

    # Compruebo si hay registros con el código unicode repetido
    for i in range(len(importado)):
        for j in range(i + 1, len(importado)):
            if importado[i][0] == importado[j][0]:
                print("PROBLEMA: El campo código unicode coincide:")
                print(importado[i])
                print(importado[j])

    return importado


def importa_fichero_emoji_data():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_EMOJI_DATA}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_EMOJI_DATA,
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
    print(f"    comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "Emoji",
            "Emoji_Component",
            "Emoji_Modifier",
            "Emoji_Modifier_Base",
            "Emoji_Presentation",
            "Extended_Pictographic",
        ]:
            print("    Valor inesperado en campo [1]:", elemento[1])
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
            print("    Valor inesperado en campo [2]:", elemento[2])
    # No sé por qué incluyen elementos reservados. Si en las agrupaciones están todos reservados, los puedo eliminar
    # pero si solo están reservados una parte, tendré que mirar a mano cuáles están reservados
    print(
        "    eliminando elementos reservados cuando todos los de una agrupación están reservados ..."
    )
    for i in range(len(importado) - 1, -1, -1):
        if importado[i][5][:9] == "<reserved":
            del importado[i]
    print("    separando agrupaciones ...")
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
    for i in range(len(importado)):
        importado[i][0] = importado[i][0].split(" ")
    # # Esto está pendiente de hacer
    # # Elimino los elementos que son componentes que van a parar a emoji_data_componentes
    # print("  separando componentes ...")
    # encontrados = []
    # for i in range(len(importado)-1, -1, -1):
    #     encontrado = False
    #     # print(importado[i][0])
    #     for j in range(len(ucdef.emoji_data_componentes_auxiliar)):
    #         if importado[i][1] == "Emoji_Component" and importado[i][0] == ucdef.emoji_data_componentes_auxiliar[j]:
    #             # print (importado[i][0], ucdef.emoji_data_componentes_auxiliar[j])
    #             encontrado = True
    #             # input()
    #     if encontrado:
    #         encontrados += [importado[i]]
    #         del(importado[i])
    # if len(encontrados) == len(ucdef.emoji_data_componentes_auxiliar):
    #     print ("    Encontrados todos los componentes")
    # else:
    #     print(f"    CUIDADO: en vez de {len(ucdef.emoji_data_componentes_auxiliar)} he encontrado {len(encontrados)}")
    # # for i in encontrados:
    # #     print(i)
    # sys.exit()

    # Como hay elementos agrupados y los voy a separar, no tiene sentido mantener los caracteres ni sus nombres porque solo están en primero y el último
    print("    eliminando campo caracteres ...")
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

    # Algunos caracteres salen varias veces en la lista, cada vez con una propiedad
    # así que los agrupo haciendo una lista de propiedades
    for i in range(len(importado)):
        importado[i][1] = [importado[i][1]]
    # Primero confirmo que la versión coincide en los registros con carácter repetido
    for i in range(len(importado) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if importado[i][0] == importado[j][0]:
                if importado[i][2] != importado[j][2]:
                    print("PROBLEMA: El campo versión no coincide:")
                    print(importado[i])
                    print(importado[j])
                    sys.exit()
    # Creo una nueva lista con los valores agrupados
    importado2 = []
    for i in range(len(importado)):
        encontrado = -1
        for j in range(len(importado2)):
            if importado[i][0] == importado2[j][0]:
                encontrado = j
        if encontrado == -1:
            importado2 += [importado[i]]
        else:
            importado2[encontrado][1] += importado[i][1]

    # Compruebo si hay registros con el código unicode repetido
    for i in range(len(importado2)):
        for j in range(i + 1, len(importado2)):
            if importado2[i][0] == importado2[j][0]:
                print("PROBLEMA: El campo código unicode coincide:")
                print(importado2[i])
                print(importado2[j])

    # Algunos de los caracteres que he separado en realidad no existen en Unicode, así que los elimino
    print("    eliminando caracteres inexistentes ...")
    for i in range(len(importado2) - 1, -1, -1):
        encontrado = False
        for j in derived_name:
            if importado2[i][0][0] == j[0]:
                encontrado = True
        if not encontrado:
            print("      Elimino caracter no existente:", importado2[i])
            del importado2[i]

    return importado2


def importa_fichero_emoji_variation_sequence():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_EMOJI_VARIATION_SEQUENCES}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_EMOJI_VARIATION_SEQUENCES,
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
                linea += [resto[0][corta + 1 :].strip().lower()]
                importado += [linea]
    print(f"    comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "text style",
            "emoji style",
        ]:
            print("    Valor inesperado en campo [1]:", elemento[1])
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
            print("    Valor inesperado en campo [2]:", elemento[2])

    # Compruebo si hay registros con el código unicode repetido
    for i in range(len(importado)):
        for j in range(i + 1, len(importado)):
            if importado[i][0] == importado[j][0]:
                print("PROBLEMA: El campo código unicode coincide:")
                print(importado[i])
                print(importado[j])

    return importado


def importa_fichero_emoji_zwj_sequences():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_EMOJI_ZWJ_SEQUENCES}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_EMOJI_ZWJ_SEQUENCES,
        mode="r",
        encoding="utf-8",
    ) as f:
        grupo = ""
        for line in f:
            if line[:25] == "# RGI_Emoji_ZWJ_Sequence:":
                grupo = line[26:-1].replace("&amp;", "&")
            if line[0] != "#" and line[0] != "\n":
                linea = []
                # print(line)
                corta = line.find(";")
                resto = line
                linea += [resto[:corta].strip()]
                linea[0] = linea[0].split(" ")
                resto = [resto[corta + 1 :].strip()]
                corta = resto[0].find(";")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("# E")
                if corta != -1:
                    linea += [resto[0][:corta].strip()]
                    resto = [resto[0][corta + 3 :].strip()]
                else:
                    corta = resto[0].find("#E")
                    linea += [resto[0][:corta].strip()]
                    resto = [resto[0][corta + 2 :].strip()]
                corta = resto[0].find("[")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("] (")
                # No guardo este valor porque es siempre [1]
                # linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 3 :].strip()]
                corta = resto[0].find(")")
                linea += [resto[0][:corta].strip()]
                linea += [grupo]
                importado += [linea]
    print(f"    comprobando ...")
    for elemento in importado:
        if elemento[1] != "RGI_Emoji_ZWJ_Sequence":
            print("    Valor inesperado en campo [1]:", elemento[1])
        if elemento[3] not in [
            "2.0",
            "4.0",
            "5.0",
            "11.0",
            "12.0",
            "12.1",
            "13.0",
            "13.1",
            "14.0",
        ]:
            print("    Valor inesperado en campo [3]:", elemento[3])
            print(elemento)

    # Compruebo si hay registros con el código unicode repetido
    for i in range(len(importado)):
        for j in range(i + 1, len(importado)):
            if importado[i][0] == importado[j][0]:
                print("PROBLEMA: El campo código unicode coincide:")
                print(importado[i])
                print(importado[j])

    return importado


def importa_fichero_emoji_sequences():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_EMOJI_SEQUENCES}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_EMOJI_SEQUENCES,
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
                corta = resto[0].find(";")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("#")
                linea += [resto[0][:corta].strip()]
                resto = [resto[0][corta + 1 :].strip()]
                corta = resto[0].find("[")
                linea += [resto[0][1:corta].strip()]
                resto = [resto[0][corta:].strip()]
                corta = resto[0].find("]")
                linea += [resto[0][1:corta].strip()]
                linea[4] = int(linea[4])
                importado += [linea]
    print(f"    comprobando ...")
    for elemento in importado:
        if elemento[1] not in [
            "Basic_Emoji",
            "Emoji_Keycap_Sequence",
            "RGI_Emoji_Flag_Sequence",
            "RGI_Emoji_Tag_Sequence",
            "RGI_Emoji_Modifier_Sequence",
        ]:
            print("    Valor inesperado en campo [1]:", elemento[1])
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
            "13.0",
            "13.1",
            "14.0",
        ]:
            print("    Valor inesperado en campo [3]:", elemento[3])
    print("    separando agrupaciones ...")
    for i in range(len(importado) - 1, -1, -1):
        if importado[i][4] > 1:
            corta = importado[i][0].find(".")
            valor_inicial = int(importado[i][0][:corta], 16)
            for j in range(importado[i][4]):
                valor = valor_inicial + j
                valor = f"{valor:04x}".upper()
                tmp = importado[i][:]
                tmp[:0] = [valor]
                del tmp[1]
                importado[i + j + 1 : i + j + 1] = [tmp]
            del importado[i]
    for i in range(len(importado)):
        importado[i][0] = importado[i][0].split(" ")
    print("    eliminando campo caracteres ...")
    for i in range(len(importado) - 1, -1, -1):
        del importado[i][4]
        del importado[i][2]

    # Compruebo si hay registros con el código unicode repetido
    for i in range(len(importado)):
        for j in range(i + 1, len(importado)):
            if importado[i][0] == importado[j][0]:
                print("PROBLEMA: El campo código unicode coincide:")
                print(importado[i])
                print(importado[j])

    return importado


def importa_fichero_derived_name():
    print()
    print(f"  TRATANDO {ucdef.FICHERO_DERIVED_NAME}")
    print(f"    importando ...")
    importado = []
    with open(
        ucdef.FICHERO_DERIVED_NAME,
        mode="r",
        encoding="utf-8",
    ) as f:
        for line in f:
            if line[0] != "#" and line[0] != "\n" and line[-3:-1] != "-*":
                linea = []
                resto = line
                # códigos
                corta = line.find(";")
                linea += [resto[:corta].strip()]
                # nombre
                linea += [resto[corta + 1 :].strip().lower()]
                importado += [linea]

    for i in range(len(importado)):
        grupo_encontrado = ""
        for grupo in ucdef.uc_tablas_caracteres[0]:
            if int(importado[i][0], 16) >= int(grupo[3], 16) and int(importado[i][0], 16) <= int(grupo[4], 16):
                grupo_encontrado = grupo[1]
        importado[i] += [grupo_encontrado]

    return importado


def completa_fichero_derived_name():
    # Para saber si la presentación por defecto es emoji
    # hay que mirar emoji_data si tiene 'Emoji' y 'Emoji_Presentation'
    global derived_name
    print()
    print(f"  TRATANDO {ucdef.FICHERO_DERIVED_NAME}")
    print(f"    añadiendo texto/emoji  ...")

    # Cojo cada caracter unicode
    for i in range(len(derived_name)):
        codigo = derived_name[i][0]
        # Miro primero si está en emoji_avriation_sequencess
        es_emoji_texto = False
        for j in emoji_variation_sequences:
            # print(j[0][0])
            if codigo == j[0][0]:
                es_emoji_texto = True
        # Si está en emoji_variation_sequencess
        if es_emoji_texto:
            # Miro qué pone en emoji_data
            for j in emoji_data:
                if codigo == j[0][0]:
                    if "Emoji" in j[1] and "Emoji_Presentation" in j[1]:
                        derived_name[i][2:2] = ["emoji-texto"]
                    else:
                        derived_name[i][2:2] = ["texto-emoji"]
        else:
            # Miro qué pone en emoji_data
            encontrado = False
            for j in emoji_data:
                if codigo == j[0][0]:
                    encontrado = True
                    if "Emoji" in j[1]:
                        derived_name[i][2:2] = ["emoji"]
                    else:
                        derived_name[i][2:2] = ["texto"]
            if not encontrado:
                derived_name[i][2:2] = ["texto"]

    c_emoji = c_texto = c_texto_emoji = c_emoji_texto = 0
    for i in derived_name:
        if i[2] == "emoji":
            c_emoji += 1
        elif i[2] == "texto":
            c_texto += 1
        elif i[2] == "texto-emoji":
            c_texto_emoji += 1
        elif i[2] == "emoji-texto":
            c_emoji_texto += 1
    print(f"    Emoji: {c_emoji} - Texto: {c_texto} - Texto-emoji: {c_texto_emoji} - Emoji-texto: {c_emoji_texto}")
    print(f"    Total: {c_emoji_texto + c_texto_emoji + c_emoji + c_texto} de {len(derived_name)}")



def exporta_listas():
    destino = ucdef.FICHERO_IMPORTADO
    print()
    print(f"  CREANDO {destino}")

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
        # Guarda emoji_zwj_sequences
        t += "emoji_zwj_sequences = [\n"
        for i in emoji_zwj_sequences:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        # Guarda emoji_sequences
        t += "emoji_sequences = [\n"
        for i in emoji_sequences:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)

    destino = ucdef.FICHERO_UNICODE
    print()
    print(f"  CREANDO {destino}")
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda derived_name
        t += "derived_name = [\n"
        for i in derived_name:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def importa_unicode():
    global emoji_test, emoji_data, emoji_variation_sequences, emoji_zwj_sequences, emoji_sequences, derived_name
    print("1. IMPORTANDO FICHEROS UNICODE ORIGINALES EN MATRICES")
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p = pathlib.Path(ucdef.FICHERO_UNICODE)
    if not p.exists():
        print("El fichero NO EXISTE")
    p = pathlib.Path(ucdef.FICHERO_IMPORTADO)
    if p.exists():
        print(f"  El fichero de destino {ucdef.FICHERO_IMPORTADO} ya existe.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta != "S":
            print("  El fichero no se ha creado.")
        else:
            os.remove(p)
    if not p.exists():
        derived_name = importa_fichero_derived_name()
        emoji_test = importa_fichero_emoji_test()
        emoji_data = importa_fichero_emoji_data()
        emoji_variation_sequences = importa_fichero_emoji_variation_sequence()
        emoji_zwj_sequences = importa_fichero_emoji_zwj_sequences()
        emoji_sequences = importa_fichero_emoji_sequences()
        completa_fichero_derived_name()
        exporta_listas()
    print()
    print("  Programa terminado.")
    print()
