# Este programa crea una página web con los grupos de emojis que hay definidos en manual_1
# Lo he hecho para mejorar uc_91_crea_manual_1 y que asigne automáticamente la mayor parte posible de los grupos

import os
import pathlib
import ucdef
import sys
from u14_ficheros_3_fusionados import unicode_txt_fusionados_2 as imp


def grupos(elemento):
    grupos = []
    if len(elemento[0]) == 1:
        for grupo in ucdef.uc_tablas_caracteres[0]:
            if elemento[0][0] >= grupo[3] and elemento[0][0] <= grupo[4]:
                grupos += [grupo[1]]
        if elemento[3][0][0] == "Emoji_Component":
            grupos += ["gr-componentes"]
    elif len(elemento[0]) == 2:
        # XXX VS15/VS16
        if elemento[0][1] == "FE0E" or elemento[0][1] == "FE0F":
            grupos += ["gr-texto-emoji"]
        # XXX FZ
        if elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF":
            grupos += ["gr-colores-piel-1"]
        # LETRA-REGIONAL LETRA-REGIONAL
        if elemento[0][0] >= "1F1E6" and elemento[0][0] <= "1F1FF" and elemento[0][1] >= "1F1E6" and elemento[0][1] <= "1F1FF":
            grupos += ["gr-banderas-paises"]
        # PAREJA FZ
        if (elemento[0][0] == "1F46B" or elemento[0][0] == "1F46C" or elemento[0][0] == "1F46D") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF"):
            grupos += ["gr-parejas-mano-piel-2"]
        # XXX KEYCAP
        if elemento[0][1] == "20E3":
            grupos += ["gr-keycap"]
    elif len(elemento[0]) == 3:
        # BANDERAS VARIAS
        if (elemento[0][0] == "1F3F3" or elemento[0][0] == "1F3F4") and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # M/W ZWJ NIÑO/NIÑA
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and (elemento[0][2] == "1F466" or elemento[0][2] == "1F467"):
            grupos += ["gr-familias"]
        # ADULTO ZWJ XXX
        if elemento[0][0] == "1F9D1" and elemento[0][1] == "200D":
            grupos += ["gr-genero-5"]
        # M/W ZWJ XXX
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and (elemento[0][2] != "1F466" and elemento[0][2] != "1F467"):
            grupos += ["gr-genero-1"]
        # XXX ZWJ M/F
        if elemento[0][1] == "200D" and (elemento[0][2] == "2640" or elemento[0][2] == "2642"):
            grupos += ["gr-genero-1"]
        # XXX KFE0F EYCAP
        if elemento[0][1] == "FE0F" and elemento[0][2] == "20E3":
            grupos += ["gr-keycap"]
    elif len(elemento[0]) == 4:
        # ADULTO ZWJ XXX
        if elemento[0][0] == "1F9D1" and elemento[0][1] == "200D" and elemento[0][3] == "FE0F":
            grupos += ["gr-genero-6"]
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F3" and elemento[0][1] == "FE0F" and elemento[0][2] == "200D":
            grupos += ["gr-banderas-otras"]
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F3" and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F4" and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # M/W ZWJ XXX VS16
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][3] == "FE0F":
            grupos += ["gr-genero-2"]
        # ZWJ M/F XXX VS16
        if elemento[0][1] == "200D" and (elemento[0][2] == "2640" or elemento[0][2] == "2642") and elemento[0][3] == "FE0F":
            grupos += ["gr-genero-3"]
        # XXX VS16 ZWJ M/F
        if elemento[0][1] == "FE0F" and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642"):
            grupos += ["gr-genero-7"]
        # ADULTO FZ ZWJ XXX
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D":
            grupos += ["gr-colores-piel-6"]
        # M/W FZ ZWJ XXX
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D":
            grupos += ["gr-colores-piel-2"]
        # XXX FZ ZWJ M/F
        if (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642"):
            grupos += ["gr-colores-piel-5"]
    elif len(elemento[0]) == 5:
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F3" and elemento[0][1] == "FE0F" and elemento[0][2] == "200D"and elemento[0][4] == "FE0F":
            grupos += ["gr-banderas-otras"]
        # HOMBRE/MUJER ZWJ NIÑO/NIÑA/HOMBRE/MUJER ZWJ NIÑO/NIÑA
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and (elemento[0][2] == "1F466" or elemento[0][2] == "1F467" or elemento[0][2] == "1F468" or elemento[0][2] == "1F469") and elemento[0][3] == "200D" and (elemento[0][4] == "1F466" or elemento[0][4] == "1F467"):
            grupos += ["gr-familias"]
        # HOMBRE/MUJER ZWJ CORAZÓN ZWJ HOMBRE/MUJER
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][2] == "2764" and elemento[0][3] == "200D" and (elemento[0][4] == "1F468" or elemento[0][4] == "1F469"):
            grupos += ["gr-parejas-corazon-1"]
        # ADULTO ZWJ APRETÓN-MANOS ZWJ ADULTO
        if elemento[0][0] == "1F9D1" and elemento[0][1] == "200D" and elemento[0][2] == "1F91D" and elemento[0][3] == "200D" and elemento[0][4] == "1F9D1":
            grupos += ["gr-parejas-mano-piel-1"]
        # XXX VS15 ZWJ M/F VS16
        if elemento[0][1] == "FE0F" and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642") and elemento[0][4] == "FE0F":
            grupos += ["gr-genero-4"]
        # ADULTO FZ ZWJ XXX VS16
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][4] == "FE0F":
            grupos += ["gr-colores-piel-7"]
        # MANO-DERECHA FZ ZWJ MANO-IZQUIERDA FZ
        if elemento[0][0] == "1FAF1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "1FAF2" and (elemento[0][4] == "1F3FB" or elemento[0][4] == "1F3FC" or elemento[0][4] == "1F3FD" or elemento[0][4] == "1F3FE" or elemento[0][4] == "1F3FF") :
            grupos += ["gr-colores-piel-8"]
        # M/W FZ ZWJ XXX XXX
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D":
            grupos += ["gr-colores-piel-3"]
        # XXX FZ ZWJ M/F XXX
        if (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642"):
            grupos += ["gr-colores-piel-4"]
    elif len(elemento[0]) == 6:
        # HOMBRE/MUJER ZWJ CORAZÓN VS16 ZWJ HOMBRE/MUJER
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][2] == "2764" and elemento[0][3] == "FE0F" and elemento[0][4] == "200D" and (elemento[0][5] == "1F468" or elemento[0][5] == "1F469"):
            grupos += ["gr-parejas-corazon-1"]
    elif len(elemento[0]) == 7:
        # BANDERA REGION
        if elemento[0][0] == "1F3F4":
            grupos += ["gr-banderas-regiones"]
        # M/W ZWJ NIÑO/NIÑA ZWJ HOMBRE/MUJER ZWJ NIÑO/NIÑA
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][3] == "200D" and (elemento[0][4] == "1F466" or elemento[0][4] == "1F467") and elemento[0][5] == "200D" and (elemento[0][6] == "1F466" or elemento[0][6] == "1F467"):
            grupos += ["gr-familias"]
        # ADULTO FZ ZWJ APRETÓN-MANOS ZWJ ADULTO FZ
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "1F91D" and elemento[0][4] == "200D" and elemento[0][5] == "1F9D1" and (elemento[0][6] == "1F3FB" or elemento[0][6] == "1F3FC" or elemento[0][6] == "1F3FD" or elemento[0][6] == "1F3FE" or elemento[0][6] == "1F3FF"):
            grupos += ["gr-parejas-mano-piel-1"]
        # HOMBRE/MUJER FZ ZWJ APRETÓN-MANOS ZWJ HOMBRE/MUJER FZ
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "1F91D" and elemento[0][4] == "200D" and (elemento[0][5] == "1F468" or elemento[0][5] == "1F469") and (elemento[0][6] == "1F3FB" or elemento[0][6] == "1F3FC" or elemento[0][6] == "1F3FD" or elemento[0][6] == "1F3FE" or elemento[0][6] == "1F3FF"):
            grupos += ["gr-parejas-mano-piel-2"]
        # ADULTO FZ ZWJ CORAZÓN ZWJ ZWJ ADULTO FZ
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and  elemento[0][4] == "200D" and elemento[0][5] == "1F9D1" and (elemento[0][6] == "1F3FB" or elemento[0][6] == "1F3FC" or elemento[0][6] == "1F3FD" or elemento[0][6] == "1F3FE" or elemento[0][6] == "1F3FF"):
            grupos += ["gr-parejas-corazon-piel-1"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN ZWJ ZWJ HOMBRE/MUJER FZ
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "200D" and (elemento[0][5] == "1F468" or elemento[0][5] == "1F469") and (elemento[0][6] == "1F3FB" or elemento[0][6] == "1F3FC" or elemento[0][6] == "1F3FD" or elemento[0][6] == "1F3FE" or elemento[0][6] == "1F3FF"):
            grupos += ["gr-parejas-corazon-piel-2"]
        # HOMBRE/MUJER ZWJ CORAZÓN ZWJ BESO ZWJ HOMBRE/MUJER
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][2] == "2764" and elemento[0][3] == "200D" and  elemento[0][4] == "1F48B" and elemento[0][5] == "200D" and (elemento[0][6] == "1F468" or elemento[0][6] == "1F469"):
            grupos += ["gr-parejas-beso-1"]
    elif len(elemento[0]) == 8:
        # HOMBRE/MUJER ZWJ CORAZÓN VS16 ZWJ BESO ZWJ HOMBRE/MUJER
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][2] == "2764" and elemento[0][3] == "FE0F" and elemento[0][4] == "200D" and  elemento[0][5] == "1F48B" and elemento[0][6] == "200D" and (elemento[0][7] == "1F468" or elemento[0][7] == "1F469"):
            grupos += ["gr-parejas-beso-1"]
        # ADULTO FZ ZWJ CORAZÓN VS16 ZWJ ZWJ ADULTO FZ
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "FE0F" and elemento[0][5] == "200D" and elemento[0][6] == "1F9D1" and (elemento[0][7] == "1F3FB" or elemento[0][7] == "1F3FC" or elemento[0][7] == "1F3FD" or elemento[0][7] == "1F3FE" or elemento[0][7] == "1F3FF"):
            grupos += ["gr-parejas-corazon-piel-1"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN VS16 ZWJ ZWJ HOMBRE/MUJER FZ
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "FE0F" and elemento[0][5] == "200D" and (elemento[0][6] == "1F468" or elemento[0][6] == "1F469") and (elemento[0][7] == "1F3FB" or elemento[0][7] == "1F3FC" or elemento[0][7] == "1F3FD" or elemento[0][7] == "1F3FE" or elemento[0][7] == "1F3FF"):
            grupos += ["gr-parejas-corazon-piel-2"]
    elif len(elemento[0]) == 9:
        # ADULTO FZ ZWJ CORAZÓN ZWJ BESO ZWJ ADULTO FZ
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "200D" and  elemento[0][5] == "1F48B" and elemento[0][6] == "200D" and elemento[0][7] == "1F9D1"  and (elemento[0][8] == "1F3FB" or elemento[0][8] == "1F3FC" or elemento[0][8] == "1F3FD" or elemento[0][8] == "1F3FE" or elemento[0][8] == "1F3FF"):
            grupos += ["gr-parejas-beso-piel-1"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN ZWJ BESO ZWJ HOMBRE/MUJER FZ
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "200D" and  elemento[0][5] == "1F48B" and elemento[0][6] == "200D" and (elemento[0][7] == "1F468" or elemento[0][7] == "1F469") and (elemento[0][8] == "1F3FB" or elemento[0][8] == "1F3FC" or elemento[0][8] == "1F3FD" or elemento[0][8] == "1F3FE" or elemento[0][8] == "1F3FF"):
            grupos += ["gr-parejas-beso-piel-2"]
    elif len(elemento[0]) == 10:
        # ADULTO FZ ZWJ CORAZÓN VS16 ZWJ BESO ZWJ ADULTO FZ
        if elemento[0][0] == "1F9D1" and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "FE0F" and elemento[0][5] == "200D" and  elemento[0][6] == "1F48B" and elemento[0][7] == "200D" and elemento[0][8] == "1F9D1"  and (elemento[0][9] == "1F3FB" or elemento[0][9] == "1F3FC" or elemento[0][9] == "1F3FD" or elemento[0][9] == "1F3FE" or elemento[0][9] == "1F3FF"):
            grupos += ["gr-parejas-beso-piel-1"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN VS16 ZWJ BESO ZWJ HOMBRE/MUJER FZ
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and elemento[0][3] == "2764" and elemento[0][4] == "FE0F" and elemento[0][5] == "200D" and  elemento[0][6] == "1F48B" and elemento[0][7] == "200D" and (elemento[0][8] == "1F468" or elemento[0][8] == "1F469") and (elemento[0][9] == "1F3FB" or elemento[0][9] == "1F3FC" or elemento[0][9] == "1F3FD" or elemento[0][9] == "1F3FE" or elemento[0][9] == "1F3FF"):
            grupos += ["gr-parejas-beso-piel-2"]
    return grupos


def crea_manual_1():
    global manual_1
    manual_1 = []
    for i in imp.fusionados_2:
        manual_1 += [[i[0], grupos(i)]]
    for i in manual_1:
        if not len(i[1]) and len(i[0]) > 1:
            i[1] = ["gr-restos"]
    cuenta_en_grupos = 0
    cuenta_en_varios_grupos = 0
    for i in manual_1:
        if len(i[1]):
            cuenta_en_grupos += 1
        if len(i[1]) > 1:
            cuenta_en_varios_grupos += 1
    print(f"  Hay {len(imp.fusionados_2)} elementos")
    print(f"  Ya clasificados en grupos: {cuenta_en_grupos}")
    print(f"  Pendientes de clasificar: {len(imp.fusionados_2) - cuenta_en_grupos}")
    print(f"  Pertenecientes a varios grupos: {cuenta_en_varios_grupos}")
    if cuenta_en_varios_grupos:
        for i in manual_1:
            if len(i[1]) > 1:
                print(f"    {i}")



def exporta_lista():
    destino = ucdef.FICHERO_MANUAL_1
    print(f"CREANDO {destino}")
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda Full emoji list
        t += "manual_1 = [\n"
        for i in manual_1:
            print
            t += "  [\n"
            t += f"    {i[0]},\n"
            t += f'    {i[1]},\n'
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def selecciona_grupo(nombre_grupo):
    # extrae y elimina de manual_1 los emojis de un grupo
    global manual_1
    grupo = []
    for i in range(len(manual_1) - 1, -1, -1):
        for j in range(len(manual_1[i][1])-1, -1, -1):
            if manual_1[i][1][j] == nombre_grupo:
                grupo += [manual_1[i]]
                # del manual_1[i][1][j]
        # if len(manual_1[i][1]) == 0:
        #     del manual_1[i]
    return grupo


def genera_entidad_numerica(codigo):
    t = ""
    if len(codigo) == 1:
        t = f"&#x{codigo[0]};"
    else:
        for i in range(len(codigo) - 1):
            t += f"&#x{codigo[i]};"
        t += f"&#x{codigo[-1]};"
    return t


def exporta_pagina():
    destino = ucdef.PAGINA_MANUAL_1
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = "<!DOCTYPE html>\n"
        t += '<html lang="es">\n'
        t += "<head>\n"
        t += '  <meta charset="utf-8">\n'
        t += "</head>\n"
        t += "<body>\n"
        t += "<h1>Emojis por gupos</h1>"
        for grupo in ucdef.uc_tablas_caracteres[0]:
            extraido = selecciona_grupo(grupo[1])
            t += f"  <p>{grupo[1]}\n"
            for i in extraido:
                t += f"    {genera_entidad_numerica(i[0])}\n"
            t += "  </p>\n"
        for grupo in ucdef.uc_grupos_2:
            extraido = selecciona_grupo(grupo)
            t += f"  <p>{grupo}\n"
            for i in extraido:
                t += f"    {genera_entidad_numerica(i[0])}\n"
            t += "  </p>\n"
        t += "</body>\n"
        t += "</html>\n"
        fichero.write(t)
    destino = ucdef.PAGINA_MANUAL_2
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = "<!DOCTYPE html>\n"
        t += '<html lang="es">\n'
        t += "<head>\n"
        t += '  <meta charset="utf-8">\n'
        t += "</head>\n"
        t += "<body>\n"
        t += "<h1>Emojis pendientes de incluir en grupo</h1>"
        # for grupo in ucdef.uc_tablas_caracteres[0]:
        #     extraido = selecciona_grupo(grupo[1])
        t += "<h2>Restos 1</h2>\n"
        cuenta_1 = 0
        t += f"  <p>\n"
        for i in manual_1:
            if len(i[1]) == 0 and len(i[0]) == 1:
                t += f"    {genera_entidad_numerica(i[0])}\n"
                t += f"    {i[0]}<br>\n"
                cuenta_1 += 1
        t += "  </p>\n"
        t += "<h2>Restos secuencias</h2>\n"
        cuenta_2 = 0
        t += f"  <p>\n"
        for i in manual_1:
            if len(i[1]) == 0 and len(i[0]) > 1:
                t += f"    {genera_entidad_numerica(i[0])}\n"
                t += f"    {i[0]}<br>\n"
                cuenta_2 += 1
        t += "  </p>\n"
        t += f"  <p>Pendientes de clasificar: {cuenta_1} simples y {cuenta_2} secuencias</p>\n"
        t += "</body>\n"
        t += "</html>\n"
        fichero.write(t)


def main():
    print("91. CREANDO FICHEROS MANUALES A PARTIR FUSIONADOS_2")
    crea_manual_1()
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p_1 = pathlib.Path(ucdef.FICHERO_MANUAL_1)
    respuesta = "N"
    if p_1.exists():
        print(f"  El fichero de destino MANUAL ya existe.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta == "S":
            if p_1.exists():
                os.remove(p_1)
        else:
            print("  No se ha creado el fichero.")
    if not p_1.exists():
        exporta_lista()
        exporta_pagina()


if __name__ == "__main__":
    main()
