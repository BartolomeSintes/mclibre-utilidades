# Este programa fusiona en una sola lista todas las listas
# de los ficheros importados por los programas uc_1, uc_2 y uc_3

import ucdef
import os
import pathlib
import sys
import ucdef
from u14_ficheros_2_importados import unicode_txt_importados as imp
from u14_ficheros_2_importados import unicode_full_emoji_list as imp2
from u14_ficheros_2_importados import unicode_full_emoji_modifier_sequences_list as imp3

fusionados = []


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
    global fusionados

    # Añado full_emoji_list a fusionados
    for i in range(len(imp2.full_emoji_list)):
        fusionados += [
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

    # Añado full_emoji_modifier_sequences_list a fusionados
    for i in range(len(imp3.full_emoji_modifier_sequences)):
        fusionados += [
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

    # Añado emoji_test a fusionados
    for i in range(len(imp.emoji_test)):
        posicion = busca(imp.emoji_test[i][0], fusionados)
        if posicion != -1:
            fusionados[posicion][2] = imp.emoji_test[i][1:]
        else:
            fusionados += [
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

    # Añado emoji_data a fusionados
    for i in range(len(imp.emoji_data)):
        posicion = busca(imp.emoji_data[i][0], fusionados)
        if posicion != -1:
            fusionados[posicion][3] = [imp.emoji_data[i][1], imp.emoji_data[i][2]]
        else:
            fusionados += [
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

    # Añado emoji_variation_sequences a fusionados
    for i in range(len(imp.emoji_variation_sequences)):
        posicion = busca(imp.emoji_variation_sequences[i][0], fusionados)
        if posicion != -1:
            fusionados[posicion][4] = imp.emoji_variation_sequences[i][1:]
        else:
            fusionados += [
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

    # Añado emoji_zwj_sequences a fusionados
    for i in range(len(imp.emoji_zwj_sequences)):
        posicion = busca(imp.emoji_zwj_sequences[i][0], fusionados)
        if posicion != -1:
            fusionados[posicion][5] = imp.emoji_zwj_sequences[i][1:]
        else:
            fusionados += [
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

    # Añado emoji_sequences a fusionados
    for i in range(len(imp.emoji_sequences)):
        posicion = busca(imp.emoji_sequences[i][0], fusionados)
        if posicion != -1:
            fusionados[posicion][6] = imp.emoji_sequences[i][1:]
        else:
            fusionados += [
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


def exporta_listas():
    destino = ucdef.FICHERO_FUSIONADO_1
    print()
    print(f"  CREANDO {destino}")

    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda fusionados
        t += "fusionados = [\n"
        for i in fusionados:
            t += f"  [\n"
            t += f"    {i[0]},\n"
            t += f"    {i[1]},\n"
            t += f"    {i[2]},\n"
            t += f"    {i[3]},\n"
            t += f"    {i[4]},\n"
            t += f"    {i[5]},\n"
            t += f"    {i[6]},\n"
            t += f"  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def fusiona_listas_unicode():
    print("2. FUSIONANDO LISTAS UNICODE ORIGINALES EN UNA LISTA")
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p = pathlib.Path(ucdef.FICHERO_FUSIONADO_1)
    respuesta = "N"
    if p.exists():
        print(f"  El fichero de destino {ucdef.FICHERO_FUSIONADO_1} ya existe.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta == "S":
            os.remove(p)
        else:
            print("  El fichero no se ha creado.")
    if not p.exists():
        fusion_1()
        exporta_listas()
    print()
    print("  Programa terminado.")
    print()
