# Este programa fusiona en una sola lista todas las listas
# de los ficheros importados por los programas uc_1, uc_2 y uc_3

import copy
import os
import pathlib
import sys

import ucdef
from ficheros_2_importados import unicode_txt_importados as imp
from ficheros_2_importados import unicode_full_emoji_list as imp2
from ficheros_2_importados import unicode_full_emoji_modifier_sequences_list as imp3

fusionados_1 = []
fusionados_2 = []


def busca(codigos, lista):
    encontrado = False
    n = len(lista)
    i = 0
    # print("probando", lista[i][0], codigos)
    while not encontrado and i < n:
        # print(lista[i][0], codigos)
        if lista[i][0] == codigos:
            encontrado = True
        i += 1
        # input()
    if encontrado:
        return i - 1
    else:
        return -1


def fusion_1():
    # Fusiono las cinco listas en una sola
    global fusionados_1
    print()
    print("  Fusionando listas importadas ... ")

    # Añado full_emoji_list a fusionados_1
    for i in range(len(imp2.full_emoji_list)):
        fusionados_1 += [
            [
                imp2.full_emoji_list[i][3],
                ["emoji"] + imp2.full_emoji_list[i][:3] + imp2.full_emoji_list[i][4:],
                [],
                [],
                [],
                [],
                [],
            ]
        ]

    # Añado full_emoji_modifier_sequences_list a fusionados_1
    for i in range(len(imp3.full_emoji_modifier_sequences)):
        fusionados_1 += [
            [
                imp3.full_emoji_modifier_sequences[i][3],
                ["emoji_modifier_sequence"]
                + imp3.full_emoji_modifier_sequences[i][:3]
                + imp3.full_emoji_modifier_sequences[i][4:],
                [],
                [],
                [],
                [],
                [],
            ]
        ]

    # Añado emoji_test a fusionados_1
    for i in range(len(imp.emoji_test)):
        posicion = busca(imp.emoji_test[i][0], fusionados_1)
        if posicion != -1:
            fusionados_1[posicion][2] = imp.emoji_test[i][1:]
        else:
            fusionados_1 += [
                [
                    imp.emoji_test[i][0],
                    [],
                    imp.emoji_test[i][1:],
                    [],
                    [],
                    [],
                    [],
                ]
            ]

    # Añado emoji_data a fusionados_1
    for i in range(len(imp.emoji_data)):
        posicion = busca(imp.emoji_data[i][0], fusionados_1)
        if posicion != -1:
            fusionados_1[posicion][3] = [imp.emoji_data[i][1], imp.emoji_data[i][2]]
        else:
            fusionados_1 += [
                [
                    imp.emoji_data[i][0],
                    [],
                    [],
                    [imp.emoji_data[i][1], imp.emoji_data[i][2]],
                    [],
                    [],
                    [],
                ]
            ]

    # Añado emoji_variation_sequences a fusionados_1
    for i in range(len(imp.emoji_variation_sequences)):
        posicion = busca(imp.emoji_variation_sequences[i][0], fusionados_1)
        if posicion != -1:
            fusionados_1[posicion][4] = imp.emoji_variation_sequences[i][1:]
        else:
            fusionados_1 += [
                [
                    imp.emoji_variation_sequences[i][0],
                    [],
                    [],
                    [],
                    imp.emoji_variation_sequences[i][1:],
                    [],
                    [],
                ]
            ]

    # Añado emoji_zwj_sequences a fusionados_1
    for i in range(len(imp.emoji_zwj_sequences)):
        posicion = busca(imp.emoji_zwj_sequences[i][0], fusionados_1)
        if posicion != -1:
            fusionados_1[posicion][5] = imp.emoji_zwj_sequences[i][1:]
        else:
            fusionados_1 += [
                [
                    imp.emoji_zwj_sequences[i][0],
                    [],
                    [],
                    [],
                    [],
                    imp.emoji_zwj_sequences[i][1:],
                    [],
                ]
            ]

    # Añado emoji_sequences a fusionados_1
    for i in range(len(imp.emoji_sequences)):
        posicion = busca(imp.emoji_sequences[i][0], fusionados_1)
        if posicion != -1:
            fusionados_1[posicion][6] = imp.emoji_sequences[i][1:]
        else:
            fusionados_1 += [
                [
                    imp.emoji_sequences[i][0],
                    [],
                    [],
                    [],
                    [],
                    [],
                    imp.emoji_sequences[i][1:],
                ]
            ]


def comprueba_fusion_1_1():
    # Compruebo que no hay valores raros
    print("  Comprobando que no hay valores desconocidos en lista fusionada ... ")

    for c in fusionados_1:
        # Compruebo tipo: emoji / emoji_modifier_sequences
        if len(c[1]) > 0 and c[1][0] not in ucdef.uc_tipos:
            print("PROBLEMA: tipo no esperado")
            print(f"{c[1][0]}")

        # Compruebo group
        if len(c[1]) > 0 and c[1][2] not in ucdef.uc_group:
            print("PROBLEMA: grupo no esperado")
            print(f"{c[1][2]}")

        # Compruebo status: component / fully-qualified / minimally-qualified / unqualified
        if len(c[2]) > 0 and c[2][0] not in ucdef.uc_status:
            print("PROBLEMA: status no esperado")
            print(f"{c[2][0]}")

        # Compruebo propiedades: Emoji / Emoji_Presentation / Emoji_Modifier / Emoji_Modifier_Base / Emoji_Component / Extended_Pictographic / Extended_Pictographic
        if len(c[3]) > 0:
            for propiedad in c[3][0]:
                if propiedad not in ucdef.uc_property:
                    print("PROBLEMA: propiedad no esperada")
                    print(f"{propiedad}")

        # Compruebo versión de Unicode
        if len(c[2]) > 0 and c[2][2] not in ucdef.uc_version:
            print("PROBLEMA: versión no esperada")
            print(f"{c[2][2]}")

        # Compruebo group
        if len(c[2]) > 0 and c[2][4] not in ucdef.uc_group:
            print("PROBLEMA: grupo no esperado")
            print(f"{c[2][4]}")

        # Compruebo subgroup
        if len(c[2]) > 0 and c[2][5] not in ucdef.uc_subgroup:
            print("PROBLEMA: subgrupo no esperado")
            print(f"{c[2][5]}")

        # Compruebo versión de Unicode
        if len(c[3]) > 0 and c[3][1] not in ucdef.uc_version:
            print("PROBLEMA: versión no esperada")
            print(f"{c[3][1]}")

        # Compruebo style: text style / emoji style
        if len(c[4]) > 0 and c[4][0] not in ucdef.uc_style:
            print("PROBLEMA: style no esperado")
            print(f"{c[4][0]}")

        # Compruebo versión de Unicode
        if len(c[4]) > 0 and c[4][1] not in ucdef.uc_version_2:
            print("PROBLEMA: versión no esperada")
            print(f"{c[4][1]}")

        # Compruebo type_sequence: RGI_Emoji_ZWJ_Sequence
        if len(c[5]) > 0 and c[5][0] not in ucdef.uc_type_sequence:
            print("PROBLEMA: type no esperado")
            print(f"{c[5][0]}")

        # Compruebo versión de Unicode
        if len(c[5]) > 0 and c[5][2] not in ucdef.uc_version:
            print("PROBLEMA: versión no esperada")
            print(f"{c[5][2]}")

        # Compruebo type_sequence subgrupo: Family / Role / Gendered / Hair / Other
        if len(c[5]) > 0 and c[5][4] not in ucdef.uc_type_sequence_grupo:
            print("PROBLEMA: type grupo no esperado")
            print(f"{c[5][4]}")

        # Compruebo type: Basic_Emoji / Emoji_Keycap_Sequence / RGI_Emoji_Flag_Sequence / RGI_Emoji_Tag_Sequence / RGI_Emoji_Modifier_Sequence
        if len(c[6]) > 0 and c[6][0] not in ucdef.uc_type:
            print("PROBLEMA: type no esperado")
            print(f"{c[6][0]}")

        # Compruebo versión de Unicode
        if len(c[6]) > 0 and c[6][1] not in ucdef.uc_version:
            print("PROBLEMA: versión no esperada")
            print(f"{c[6][1]}")


def comprueba_campos_iguales(a1, a2, b1, b2):
    cx = cb = ca = 0
    for c in fusionados_1:
        # Si está el que queremos eliminar
        if len(c[b1]) > 0:
            cb += 1
            # Hay que comprobar que está el otro campo
            if len(c[a1]) > 0:
                ca += 1
                # Y que coinciden los valores
                if c[a1][a2] == c[b1][b2]:
                    cx += 1
                else:
                    print(f"    ERROR: campos distintos: {c[a1][a2]}   {c[b1][b2]}")
            else:
                print(f"    ERROR: {c}")

    # print(ca, cb, cx)
    # Si cada vez que está el valor en un sitio, también está en el otro, entonces lo podemos eliminar
    print("hola", ca, cb, cx, c)
    return ca == cb == cx


def comprueba_fusion_1_2():
    # Compruebo que puedo quitar c[1][2], c[1][3], c[1][4], c[1][5], c[5][1], c[5][2], c[5][3], c[6][1]
    print("  Comprobando valores en lista fusionada ... ")
    # Los puedo quitar porque cada vez que están esos campos, los mismos valores están en otro campo del mismo registro
    # for i in range(10):
    #     print(fusionados_1[i])
    # input("pulsa una tecla")
    candidatos_a_eliminar = [
        [2, 4, 1, 2], [2, 5, 1, 3], [2, 1, 1, 4], [2, 3, 1, 5],
        [2, 3, 5, 1], [2, 2, 5, 2], [2, 1, 5, 3],
        [2, 2, 6, 1]
    ]
    for candidato in candidatos_a_eliminar:
        [a1, a2, b1, b2] = candidato
        if comprueba_campos_iguales(a1, a2, b1, b2):
            print(f"    OK:c[{b1}][{b2}] es como c[{a1}][{a2}]")
        else:
            print(f"    ERROR: c[{b1}][{b2}] NO es como c[{a1}][{a2}]")
            # print(candidato)
            # input("pulsa una tecla")

    for c in fusionados_1:
        # Compruebo que el carácter es el mismo
        if len(c[1]) > 0 and len(c[2]) > 0 and c[1][4] != c[2][1]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[1][4]} {c[2][1]}")

        # Compruebo que CLDR es el mismo
        if len(c[1]) > 0 and len(c[2]) > 0 and c[1][5] != c[2][3]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[1][5]} {c[2][3]}")

        # Compruebo que los grupos son iguales
        if len(c[1]) > 0 and len(c[2]) > 0 and c[1][2] != c[2][4]:
            print("PROBLEMA: grupos distintos")
            print(f"{c[0]} {c[1][2]} {c[2][4]}")

        # Compruebo que los subgrupos son iguales
        if len(c[1]) > 0 and len(c[2]) > 0 and c[1][3] != c[2][5]:
            print("PROBLEMA: subgrupos distintos")
            print(f"{c[0]} {c[1][3]} {c[2][5]}")

        # Compruebo que la versión es la misma
        if len(c[2]) > 0 and len(c[3]) > 0 and c[2][2] != c[3][1]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[2][2]} {c[3][1]}")

        # Compruebo que CLDR es el mismo
        if len(c[1]) > 0 and len(c[4]) > 0 and c[1][5] != c[4][2]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[1][5]} {c[4][2]}")

        # Compruebo que la versión es la misma
        if len(c[2]) > 0 and len(c[5]) > 0 and c[2][2] != c[5][2]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[2][2]} {c[5][2]}")

        # Compruebo que el carácter es el mismo
        if len(c[1]) > 0 and len(c[5]) > 0 and c[1][4] != c[5][3]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[1][4]} {c[5][3]}")

        # Compruebo que la versión es la misma
        if len(c[2]) > 0 and len(c[6]) > 0 and c[2][2] != c[6][1]:
            print("PROBLEMA: caracteres distintos")
            print(f"{c[0]} {c[2][2]} {c[6][1]}")


def fusion_2():
    # Fusiono las cinco listas en una sola
    global fusionados_2
    fusionados_2 = copy.deepcopy(fusionados_1)
    for i in range(len(fusionados_2)):
        # Borro
        if len(fusionados_2[i][2]) and len(fusionados_2[i][1]):
            # Borro CDLR repetido
            del fusionados_2[i][1][5]
            # Borro carácter repetido
            del fusionados_2[i][1][4]
            # Borro subgrupo repetido
            del fusionados_2[i][1][3]
            # Borro grupo repetido
            del fusionados_2[i][1][2]
        if len(fusionados_2[i][2]) and len(fusionados_2[i][5]):
            # Borro carácter repetido
            del fusionados_2[i][5][3]
            # Borro número de versión repetido
            del fusionados_2[i][5][2]
            # Borro CDLR repetido
            del fusionados_2[i][5][1]
        if len(fusionados_2[i][2]) and len(fusionados_2[i][6]):
            # Borro número de versión repetido
            del fusionados_2[i][6][1]


def comprueba_tipos_de_registros():
    # Compruebo los ocho tipos de registros que hay
    print("  Comprobando tipos de registros ... ")
    ct = ct1 = ct2 = ct3 = ct4 = ct5 = ct6 = ct7 = ct8 = 0
    for c in fusionados_1:
        ct += 1
        if len(c[1]) and len(c[2]) and len(c[3]) and not len(c[4]) and not len(c[5]) and len(c[6]):
            ct1 += 1
        elif len(c[1]) and len(c[2]) and len(c[3]) and not len(c[4]) and not len(c[5]) and not(len(c[6])):
            ct2 += 1
        elif len(c[1]) and len(c[2]) and not len(c[3]) and not len(c[4]) and len(c[5]) and not(len(c[6])):
            ct3 += 1
        elif len(c[1]) and len(c[2]) and not len(c[3]) and not len(c[4]) and not len(c[5]) and len(c[6]):
            ct4 += 1
        elif not len(c[1]) and len(c[2]) and not len(c[3]) and len(c[4]) and not len(c[5]) and len(c[6]):
            ct5 += 1
        elif not len(c[1]) and len(c[2]) and not len(c[3]) and not len(c[4]) and not len(c[5]) and not len(c[6]):
            ct6 += 1
        elif not len(c[1]) and not len(c[2]) and len(c[3]) and not len(c[4]) and not len(c[5]) and not len(c[6]):
            ct7 += 1
        elif not len(c[1]) and not len(c[2]) and not len(c[3]) and len(c[4]) and not len(c[5]) and not len(c[6]):
            ct8 += 1
        else:
            print("    ERROR: Tipo distinto a los esperados")
            for i in c:
                print(i)
            print()
            exit(0)

    print(f"    OK: {ct} = {ct1} + {ct2} + {ct3} + {ct4} + {ct5} + {ct6} + {ct7} + {ct8}")

def fusion_3():
    # Fusiono las cinco listas en una sola
    global fusionados_2
    fusionados_2 = []
    for i in range(len(fusionados_1)):
        c = fusionados_1[i]
        c2 = []
        # c[0]
        c2 += [c[0]]
        # c[1]
        # if len(c1[0])

        fusionados_2 += [c2]
        # Borro



def exporta_listas():
    destino = ucdef.FICHERO_FUSIONADO_1
    print(f"  Creando {destino}")

    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda fusionados_1
        t += "fusionados_1 = [\n"
        for i in fusionados_1:
            t += "  [\n"
            t += f"    {i[0]},\n"
            t += f"    {i[1]},\n"
            t += f"    {i[2]},\n"
            t += f"    {i[3]},\n"
            t += f"    {i[4]},\n"
            t += f"    {i[5]},\n"
            t += f"    {i[6]},\n"
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)

    destino = ucdef.FICHERO_FUSIONADO_2
    print(f"  Creando {destino}")

    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda fusionados_2
        t += "fusionados_2 = [\n"
        for i in fusionados_2:
            t += "  [\n"
            t += f"    {i[0]},\n"
            t += f"    {i[1]},\n"
            t += f"    {i[2]},\n"
            t += f"    {i[3]},\n"
            t += f"    {i[4]},\n"
            t += f"    {i[5]},\n"
            t += f"    {i[6]},\n"
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def fusiona_listas_unicode():
    print("4. FUSIONANDO LISTAS UNICODE ORIGINALES EN UNA LISTA")
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p_1 = pathlib.Path(ucdef.FICHERO_FUSIONADO_1)
    p_2 = pathlib.Path(ucdef.FICHERO_FUSIONADO_2)
    respuesta = "N"
    if p_1.exists() or p_2.exists():
        print("  Alguno de los ficheros de destino FUSIONADOS ya existe.")
        respuesta = input("  Confirme que desea crearlos de nuevo (S): ")
        if respuesta == "S":
            if p_1.exists():
                os.remove(p_1)
            if p_2.exists():
                os.remove(p_2)
        else:
            print("  La fusión no se ha realizado.")
    if not p_1.exists() and not p_2.exists():
        fusion_1()
        comprueba_fusion_1_1()
        comprueba_fusion_1_2()
        comprueba_tipos_de_registros()
        fusion_2()
        exporta_listas()
    print()
    print("  Programa terminado.")
    print()
