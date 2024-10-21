# Este programa crea una página web con los grupos de emojis que hay definidos en manual_1
# Lo he hecho para mejorar uc_91_crea_manual_1 y que asigne automáticamente la mayor parte posible de los grupos

import os
import pathlib
import ucdef
import sys
from ficheros_3_fusionados import unicode_txt_fusionados_2 as imp


def grupos_paginas(elemento):
    grupos = []
    paginas = []
    # Sentido hacia la derecha
    if ("27A1" in elemento[0]):
        # GÉNEROS (1) CON SENTIDO DERECHA
        if (
            (len(elemento[0]) == 5 or len(elemento[0]) == 6)
            and elemento[0][2] in ["1F9AF", "1F9BC", "1F9BD"]
            and elemento[0][4] == "27A1"
        ):
            grupos += ["gr-sentido-1"]
        elif (
            (len(elemento[0]) == 6 or len(elemento[0]) == 7)
            and elemento[0][3] in ["1F9AF", "1F9BC", "1F9BD"]
            and elemento[0][5] == "27A1"
        ):
            grupos += ["gr-sentido-1"]
        # GÉNEROS (2) CON SENTIDO DERECHA
        elif (
            (len(elemento[0]) == 3 or len(elemento[0]) == 4)
            and elemento[0][0] in ["1F3C3", "1F6B6", "1F9CE"]
            and elemento[0][2] == "27A1"
        ):
            grupos += ["gr-sentido-2"]
        elif (
            (len(elemento[0]) == 4 or len(elemento[0]) == 5)
            and elemento[0][0] in ["1F3C3", "1F6B6", "1F9CE"]
            and elemento[0][3] == "27A1"
        ):
            grupos += ["gr-sentido-2"]
        elif (
            (len(elemento[0]) == 5 or len(elemento[0]) == 6)
            and elemento[0][0] in ["1F3C3", "1F6B6", "1F9CE"]
            and elemento[0][4] == "27A1"
        ):
            grupos += ["gr-sentido-2"]
        elif (
            (len(elemento[0]) == 6 or len(elemento[0]) == 7)
            and elemento[0][0] in ["1F3C3", "1F6B6", "1F9CE"]
            and elemento[0][5] == "27A1"
        ):
            grupos += ["gr-sentido-2"]
        elif (
            (len(elemento[0]) == 7 or len(elemento[0]) == 8)
            and elemento[0][0] in ["1F3C3", "1F6B6", "1F9CE"]
            and elemento[0][6] == "27A1"
        ):
            grupos += ["gr-sentido-2"]

    # Familias genéricas
    if len(elemento[0]) == 5 or len(elemento[0]) == 7:
        if elemento[0][0] == "1F9D1" and elemento[0][4] == "1F9D2":
            grupos += ["gr-familias-4"]

    if len(elemento[0]) == 1:
        for grupo in ucdef.uc_tablas_caracteres[0]:
            if int(elemento[0][0], 16) >= int(grupo[3], 16) and int(
                elemento[0][0], 16
            ) <= int(grupo[4], 16):
                grupos += [grupo[1]]
        if "Emoji_Component" in elemento[3][0]:
            grupos += ["gr-componentes"]
    elif len(elemento[0]) == 2:
        # XXX VS15/VS16
        if elemento[0][1] in ["FE0E", "FE0F"]:
            grupos += ["gr-texto-emoji"]
        # XXX FZ
        if elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]:
            grupos += ["gr-colores-piel-1"]
        # LETRA-REGIONAL LETRA-REGIONAL
        if (
            elemento[0][0] >= "1F1E6"
            and elemento[0][0] <= "1F1FF"
            and elemento[0][1] >= "1F1E6"
            and elemento[0][1] <= "1F1FF"
        ):
            grupos += ["gr-banderas-paises"]
        # PAREJA FZ
        if elemento[0][0] in ["1F46B", "1F46C", "1F46D"] and elemento[0][1] in [
            "1F3FB",
            "1F3FC",
            "1F3FD",
            "1F3FE",
            "1F3FF",
        ]:
            grupos += ["gr-parejas-mano-piel-1"]
        # XXX KEYCAP
        if elemento[0][1] == "20E3":
            grupos += ["gr-keycap-1"]
    elif len(elemento[0]) == 3:
        # BANDERAS VARIAS
        if elemento[0][0] in ["1F3F3", "1F3F4"] and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # M/W ZWJ NIÑO/NIÑA
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] in ["1F466", "1F467"]
        ):
            grupos += ["gr-familias-1"]
        # ADULTO ZWJ XXX
        if elemento[0][0] == "1F9D1" and elemento[0][1] == "200D":
            grupos += ["gr-genero-3"]
        # M/W ZWJ XXX
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            # ¡CUIDADO!
            and (elemento[0][2] != "1F466" and elemento[0][2] != "1F467")
        ):
            grupos += ["gr-genero-1"]
        # XXX ZWJ M/F
        if elemento[0][1] == "200D" and elemento[0][2] in ["2640", "2642"]:
            grupos += ["gr-genero-2"]
        # XXX KFE0F EYCAP
        if elemento[0][1] == "FE0F" and elemento[0][2] == "20E3":
            grupos += ["gr-keycap-2"]
    elif len(elemento[0]) == 4:
        # ADULTO ZWJ XXX
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] == "200D"
            and elemento[0][3] == "FE0F"
        ):
            grupos += ["gr-genero-7"]
        # BANDERAS VARIAS
        if (
            elemento[0][0] == "1F3F3"
            and elemento[0][1] == "FE0F"
            and elemento[0][2] == "200D"
        ):
            grupos += ["gr-banderas-otras"]
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F3" and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # BANDERAS VARIAS
        if elemento[0][0] == "1F3F4" and elemento[0][1] == "200D":
            grupos += ["gr-banderas-otras"]
        # M/W ZWJ XXX VS16
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][3] == "FE0F"
        ):
            grupos += ["gr-genero-4"]
        # ZWJ M/F XXX VS16
        if (
            elemento[0][1] == "200D"
            and elemento[0][2] in ["2640", "2642"]
            and elemento[0][3] == "FE0F"
        ):
            grupos += ["gr-genero-5"]
        # XXX VS16 ZWJ M/F
        if (
            elemento[0][1] == "FE0F"
            and elemento[0][2] == "200D"
            and elemento[0][3] in ["2640", "2642"]
        ):
            grupos += ["gr-genero-6"]
        # ADULTO FZ ZWJ XXX
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
        ):
            grupos += ["gr-colores-piel-4"]
        # M/W FZ ZWJ XXX
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
        ):
            grupos += ["gr-colores-piel-2"]
        # XXX FZ ZWJ M/F
        if (
            elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] in ["2640", "2642"]
        ):
            grupos += ["gr-colores-piel-3"]
    elif len(elemento[0]) == 5:
        # BANDERAS VARIAS
        if (
            elemento[0][0] == "1F3F3"
            and elemento[0][1] == "FE0F"
            and elemento[0][2] == "200D"
            and elemento[0][4] == "FE0F"
        ):
            grupos += ["gr-banderas-otras"]
        # HOMBRE/MUJER ZWJ NIÑO/NIÑA/HOMBRE/MUJER ZWJ NIÑO/NIÑA
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] in ["1F466", "1F467", "1F468", "1F469"]
            and elemento[0][3] == "200D"
            and elemento[0][4] in ["1F466", "1F467"]
        ):
            grupos += ["gr-familias-2"]
        # HOMBRE/MUJER ZWJ CORAZÓN ZWJ HOMBRE/MUJER
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] == "2764"
            and elemento[0][3] == "200D"
            and elemento[0][4] in ["1F468", "1F469"]
        ):
            grupos += ["gr-parejas-corazon-1"]
        # ADULTO ZWJ APRETÓN-MANOS ZWJ ADULTO
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] == "200D"
            and elemento[0][2] == "1F91D"
            and elemento[0][3] == "200D"
            and elemento[0][4] == "1F9D1"
        ):
            grupos += ["gr-parejas-mano-piel-3"]
        # XXX VS15 ZWJ M/F VS16
        if (
            elemento[0][1] == "FE0F"
            and elemento[0][2] == "200D"
            and elemento[0][3] in ["2640", "2642"]
            and elemento[0][4] == "FE0F"
        ):
            grupos += ["gr-genero-8"]
        # ADULTO FZ ZWJ XXX VS16
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][4] == "FE0F"
        ):
            grupos += ["gr-colores-piel-7"]
        # MANO-DERECHA FZ ZWJ MANO-IZQUIERDA FZ
        if (
            elemento[0][0] == "1FAF1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "1FAF2"
            and elemento[0][4] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-colores-piel-8"]
        # M/W FZ ZWJ XXX XXX
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
        ):
            grupos += ["gr-colores-piel-5"]
        # XXX FZ ZWJ M/F XXX
        if (
            elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] in ["2640", "2642"]
        ):
            grupos += ["gr-colores-piel-6"]
    elif len(elemento[0]) == 6:
        # HOMBRE/MUJER ZWJ CORAZÓN VS16 ZWJ HOMBRE/MUJER
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] == "2764"
            and elemento[0][3] == "FE0F"
            and elemento[0][4] == "200D"
            and elemento[0][5] in ["1F468", "1F469"]
        ):
            grupos += ["gr-parejas-corazon-2"]
    elif len(elemento[0]) == 7:
        # BANDERA REGION
        if elemento[0][0] == "1F3F4":
            grupos += ["gr-banderas-regiones"]
        # M/W ZWJ NIÑO/NIÑA ZWJ HOMBRE/MUJER ZWJ NIÑO/NIÑA
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][3] == "200D"
            and elemento[0][4] in ["1F466", "1F467"]
            and elemento[0][5] == "200D"
            and elemento[0][6] in ["1F466", "1F467"]
        ):
            grupos += ["gr-familias-3"]
        # ADULTO FZ ZWJ APRETÓN-MANOS ZWJ ADULTO FZ
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "1F91D"
            and elemento[0][4] == "200D"
            and elemento[0][5] == "1F9D1"
            and elemento[0][6] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-mano-piel-3"]
        # HOMBRE/MUJER FZ ZWJ APRETÓN-MANOS ZWJ HOMBRE/MUJER FZ
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "1F91D"
            and elemento[0][4] == "200D"
            and elemento[0][5] in ["1F468", "1F469"]
            and elemento[0][6] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-mano-piel-2"]
        # ADULTO FZ ZWJ CORAZÓN ZWJ ZWJ ADULTO FZ
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "200D"
            and elemento[0][5] == "1F9D1"
            and elemento[0][6] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-corazon-piel-3"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN ZWJ ZWJ HOMBRE/MUJER FZ
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "200D"
            and elemento[0][5] in ["1F468", "1F469"]
            and elemento[0][6] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-corazon-piel-1"]
        # HOMBRE/MUJER ZWJ CORAZÓN ZWJ BESO ZWJ HOMBRE/MUJER
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] == "2764"
            and elemento[0][3] == "200D"
            and elemento[0][4] == "1F48B"
            and elemento[0][5] == "200D"
            and elemento[0][6] in ["1F468", "1F469"]
        ):
            grupos += ["gr-parejas-beso-1"]
    elif len(elemento[0]) == 8:
        # HOMBRE/MUJER ZWJ CORAZÓN VS16 ZWJ BESO ZWJ HOMBRE/MUJER
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] == "200D"
            and elemento[0][2] == "2764"
            and elemento[0][3] == "FE0F"
            and elemento[0][4] == "200D"
            and elemento[0][5] == "1F48B"
            and elemento[0][6] == "200D"
            and elemento[0][7] in ["1F468", "1F469"]
        ):
            grupos += ["gr-parejas-beso-2"]
        # ADULTO FZ ZWJ CORAZÓN VS16 ZWJ ZWJ ADULTO FZ
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "FE0F"
            and elemento[0][5] == "200D"
            and elemento[0][6] == "1F9D1"
            and elemento[0][7] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-corazon-piel-4"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN VS16 ZWJ ZWJ HOMBRE/MUJER FZ
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "FE0F"
            and elemento[0][5] == "200D"
            and elemento[0][6] in ["1F468", "1F469"]
            and elemento[0][7] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-corazon-piel-2"]
    elif len(elemento[0]) == 9:
        # ADULTO FZ ZWJ CORAZÓN ZWJ BESO ZWJ ADULTO FZ
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "200D"
            and elemento[0][5] == "1F48B"
            and elemento[0][6] == "200D"
            and elemento[0][7] == "1F9D1"
            and elemento[0][8] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-beso-piel-3"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN ZWJ BESO ZWJ HOMBRE/MUJER FZ
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "200D"
            and elemento[0][5] == "1F48B"
            and elemento[0][6] == "200D"
            and elemento[0][7] in ["1F468", "1F469"]
            and elemento[0][8] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-beso-piel-1"]
    elif len(elemento[0]) == 10:
        # ADULTO FZ ZWJ CORAZÓN VS16 ZWJ BESO ZWJ ADULTO FZ
        if (
            elemento[0][0] == "1F9D1"
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "FE0F"
            and elemento[0][5] == "200D"
            and elemento[0][6] == "1F48B"
            and elemento[0][7] == "200D"
            and elemento[0][8] == "1F9D1"
            and elemento[0][9] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-beso-piel-4"]
        # HOMBRE/MUJER FZ ZWJ CORAZÓN VS16 ZWJ BESO ZWJ HOMBRE/MUJER FZ
        if (
            elemento[0][0] in ["1F468", "1F469"]
            and elemento[0][1] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
            and elemento[0][2] == "200D"
            and elemento[0][3] == "2764"
            and elemento[0][4] == "FE0F"
            and elemento[0][5] == "200D"
            and elemento[0][6] == "1F48B"
            and elemento[0][7] == "200D"
            and elemento[0][8] in ["1F468", "1F469"]
            and elemento[0][9] in ["1F3FB", "1F3FC", "1F3FD", "1F3FE", "1F3FF"]
        ):
            grupos += ["gr-parejas-beso-piel-2"]
    return grupos


def crea_manual_1():
    global manual_1
    manual_1 = []
    for i in imp.fusionados_2:
        manual_1 += [[i[0], grupos_paginas(i), ""]]
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
    print()
    # Muestra los que están en varios grupos
    # if cuenta_en_varios_grupos:
    #     for i in manual_1:
    #         if len(i[1]) > 1:
    #             print(f"    {i}")


def incluye_emojis():
    global manual_1, restos_twemoji

    twemoji_completo = os.listdir(ucdef.DIRECTORIO_TWEMOJI)
    restos_twemoji = []
    for i in twemoji_completo:
        i2 = i.replace(".svg", "").upper()
        if i2.find("-") == -1:
            i2 = [i2]
        else:
            i2 = i2.split("-")

        encontrado = -1
        j = 0
        while j < len(manual_1) and encontrado == -1:
            if manual_1[j][0] == i2:
                encontrado = j
            j += 1
        if encontrado == -1:
            restos_twemoji += [[i2, i]]
        else:
            manual_1[encontrado][2] = i

    cuenta_twemojis_asociados = 0
    cuenta_caracteres_no_asociados = 0
    for c in manual_1:
        if c[2] != []:
            cuenta_twemojis_asociados += 1
        else:
            cuenta_caracteres_no_asociados += 1

    if not cuenta_caracteres_no_asociados:
        print(f"  CUIDADO: HAY {len(restos_twemoji)} DIBUJOS DE TWEMOJI")
        print("           QUE NO CORRESPONDEN A SECUENCIAS")
    # print(cuenta_twemojis_asociados, cuenta_caracteres_no_asociados, len(restos_twemoji))
    print (restos_twemoji)
    print()

    cuenta_varios_grupos = 0
    for c in manual_1:
        if len(c[1]) > 1:
            cuenta_varios_grupos += 1
            # print(c)
    print(f"  CUIDADO: HAY {cuenta_varios_grupos} EN VARIOS GRUPOS")

    # # Caracteres asociados a mano, porque automáticamente no se asocian
    asociados_manuales = [
        [["00A9"], ["A9"], "a9.svg"],
        [["00AE"], ["AE"], "ae.svg"],
        [["0023", "20E3"], ["23", "20E3"], "23-20e3.svg"],
        [["002A", "20E3"], ["2A", "20E3"], "2a-20e3.svg"],
        [["0030", "20E3"], ["30", "20E3"], "30-20e3.svg"],
        [["0031", "20E3"], ["31", "20E3"], "31-20e3.svg"],
        [["0032", "20E3"], ["32", "20E3"], "32-20e3.svg"],
        [["0033", "20E3"], ["33", "20E3"], "33-20e3.svg"],
        [["0034", "20E3"], ["34", "20E3"], "34-20e3.svg"],
        [["0035", "20E3"], ["35", "20E3"], "35-20e3.svg"],
        [["0036", "20E3"], ["36", "20E3"], "36-20e3.svg"],
        [["0037", "20E3"], ["37", "20E3"], "37-20e3.svg"],
        [["0038", "20E3"], ["38", "20E3"], "38-20e3.svg"],
        [["0039", "20E3"], ["39", "20E3"], "39-20e3.svg"],
    ]
    for asociado in asociados_manuales:
        fin = len(manual_1)
        i = 0
        while i < fin:
            if manual_1[i][0] == asociado[0]:
                manual_1[i][2] = asociado[2]
                i = fin
            i += 1
        fin = len(restos_twemoji)
        i = 0
        while i < fin:
            if restos_twemoji[i][0] == asociado[1]:
                del restos_twemoji[i]
                i = fin
            i += 1

    # for i in restos_twemoji:
    #     print(i)


def exporta_lista():
    destino = ucdef.FICHERO_MANUAL_1
    print()
    print(f"  CREANDO {destino}")
    print()
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda Full emoji list
        t += "manual_1 = [\n"
        for i in manual_1:
            t += "  [\n"
            t += f"    {i[0]},\n"
            t += f"    {i[1]},\n"
            t += f"    '{i[2]}',\n"
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        t += "restos_twemoji = [\n"
        for i in restos_twemoji:
            t += "  [\n"
            t += f"    {i[0]},\n"
            t += f"    '{i[1]}',\n"
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def selecciona_grupo(nombre_grupo):
    # extrae y elimina de manual_1 los emojis de un grupo
    global manual_1
    grupo = []
    for i in range(len(manual_1) - 1, -1, -1):
        for j in range(len(manual_1[i][1]) - 1, -1, -1):
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
        t += "  <title>Emojis por grupos</title>\n"
        t += "</head>\n"
        t += "<body>\n"
        t += "<h1>Emojis por gupos</h1>\n"
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
        t += "  <p>\n"
        for i in manual_1:
            if len(i[1]) == 0 and len(i[0]) == 1:
                t += f"    {genera_entidad_numerica(i[0])}\n"
                t += f"    {i[0]}<br>\n"
                cuenta_1 += 1
        t += "  </p>\n"
        t += "<h2>Restos secuencias</h2>\n"
        cuenta_2 = 0
        t += "  <p>\n"
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
    print()
    print("92. CREANDO FICHEROS MANUALES A PARTIR FUSIONADOS_2")
    print()
    crea_manual_1()
    incluye_emojis()
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p_1 = pathlib.Path(ucdef.FICHERO_MANUAL_1)
    respuesta = "N"
    if p_1.exists():
        print("  El fichero de destino MANUAL ya existe.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta == "S":
            if p_1.exists():
                os.remove(p_1)
        else:
            print("  No se ha creado el fichero.")
    if not p_1.exists():
        exporta_lista()
        exporta_pagina()
    print("  Programa terminado")


if __name__ == "__main__":
    main()
