import copy
import datetime
import pathlib
import runpy
import shutil
import sys
import webbrowser
from math import floor
from string import Template

import ucdef

imp = ucdef.importa_modulo(ucdef.FICHERO_UNICODE)
imp2 = ucdef.importa_modulo(ucdef.FICHERO_FUSIONADO_2)
imp3 = ucdef.importa_modulo(ucdef.FICHERO_MANUAL_1_TWEMOJI_ORIGINAL)
imp5 = ucdef.importa_modulo(ucdef.FICHERO_MANUAL_2)
imp6 = ucdef.importa_modulo(ucdef.FICHERO_MANUAL_1_NOTO)
imp7 = ucdef.importa_modulo(ucdef.FICHERO_MANUAL_1_TWEMOJI_JDECKED)

ORIGEN = pathlib.Path("sitio-plantilla")
DESTINO = pathlib.Path("sitio")
SECUENCIAS_ELIMINADAS = {
    tuple(int(codigo, 16) for codigo in codigos)
    for codigos in runpy.run_path(ucdef.FICHERO_ELIMINADOS)["eliminados"]
}
SECUENCIAS_FULLY_QUALIFIED = {
    tuple(int(codigo, 16) for codigo in c[0])
    for c in imp2.fusionados_2
    if len(c[0]) > 1 and c[2] and c[2][0] == "fully-qualified"
}


def esta_eliminado(codigos):
    return tuple(int(codigo, 16) for codigo in codigos) in SECUENCIAS_ELIMINADAS


def es_secuencia_fully_qualified(codigos):
    return len(codigos) <= 1 or tuple(
        int(codigo, 16) for codigo in codigos
    ) in SECUENCIAS_FULLY_QUALIFIED


def busca(aguja, pajar, posicion):
    encontrado = False
    n = len(pajar)
    i = 0
    while not encontrado and i < n:
        # print(pajar[i][posicion], aguja, end=" - ")
        if pajar[i][posicion] == aguja:
            encontrado = True
        i += 1
        # input()
    if encontrado:
        return i - 1
    else:
        return -1


def busca2(aguja, pajar):
    encontrado = False
    n = len(pajar)
    i = 0
    while not encontrado and i < n:
        # print(pajar[i][posicion], aguja, end=" - ")
        if pajar[i] == aguja:
            encontrado = True
        i += 1
        # input()
    if encontrado:
        return i - 1
    else:
        return -1


def agrega_selectores_variacion(codigos):
    codigos_con_selector = []
    for i, codigo in enumerate(codigos):
        codigos_con_selector.append(codigo)
        if codigo == "FE0F" or i == len(codigos) - 1:
            continue
        modificador_piel = 0x1F3FB <= int(codigos[i + 1], 16) <= 0x1F3FF
        if modificador_piel:
            continue
        posicion = busca(codigo, imp.derived_name, 0)
        if (
            posicion != -1
            and imp.derived_name[posicion][2] == "texto-emoji"
            and codigos[i + 1] != "FE0F"
        ):
            codigos_con_selector.append("FE0F")
    return codigos_con_selector


def genera_pagina(pagina):
    if pagina == ucdef.PAG_SIMBOLOS or pagina == ucdef.PAG_EMOJIS:
        return genera_pagina_caracteres(pagina)
    elif pagina == ucdef.PAG_BANDERAS:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_banderas)
    elif pagina == ucdef.PAG_GENEROS:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_generos)
    elif pagina == ucdef.PAG_FITZPATRICK:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_fitzpatrick)
    elif pagina == ucdef.PAG_PAREJAS:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_parejas)
    elif pagina == ucdef.PAG_SENTIDO:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_sentido)
    elif pagina == ucdef.PAG_OTRAS:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_otras)
    elif pagina == ucdef.PAG_TWEMOJI_ORIGINAL:
        return genera_pagina_twemoji(pagina)
    elif pagina == ucdef.PAG_NOTO:
        return genera_pagina_noto(pagina)
    elif pagina == ucdef.PAG_TWEMOJI_JDECKED:
        return genera_pagina_twemoji_jdecked(pagina)


def obtiene_lista_simbolos():
    seleccion_simbolos = []
    for grupo in ucdef.uc_tablas_caracteres[0]:
        caracteres = [
            c for c in imp.derived_name if c[3] == grupo[1] and c[2] != "emoji"
        ]
        caracteres.sort()
        if caracteres:
            seleccion_simbolos.append(
                [
                    [grupo[0], grupo[1], grupo[2], grupo[3], grupo[4]],
                    [c[0] for c in caracteres],
                ]
            )
    return seleccion_simbolos


def genera_lista_simbolos():
    # Esta función genera el fichero ucdef.FICHERO_SELECCION_SIMBOLOS.
    t = "seleccion_simbolos_manual = [\n"
    for datos_grupo, caracteres in obtiene_lista_simbolos():
        t += f"  [ {datos_grupo},\n"
        t += "    ["
        for caracter in caracteres:
            t += f"'{caracter}', "
        t += "\n"
        t += "    ],\n"
        t += "  ],\n"
    t += "]\n"
    with open(
        ucdef.UNICODE_FUSIONADOS_DIR + "/" + ucdef.FICHERO_SELECCION_SIMBOLOS,
        "w",
        encoding="utf-8",
    ) as fichero:
        fichero.write(t)


def convierte_version(valor):
    if floor(float(valor)) == float(valor):
        return floor(float(valor))
    else:
        return valor


def indica_version(codigo):
    for c in imp2.fusionados_2:
        if len(c[0]) == 1 and c[0][0] == codigo:
            if len(c[2]) > 2 and c[2][2] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[2][2])
            elif len(c[3]) > 1 and c[3][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[3][1])
            elif len(c[4]) > 1 and c[4][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[4][1])
            elif len(c[5]) > 2 and c[5][2] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[5][2])
            elif len(c[6]) > 1 and c[6][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[6][1])
            else:
                return -1
        elif len(c[0]) > 1 and c[0] == codigo:
            # print(f"codigo: {codigo} - caracter: {c[0]}")
            if len(c[2]) > 2 and c[2][2] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[2][2])
            elif len(c[3]) > 1 and c[3][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[3][1])
            elif len(c[4]) > 1 and c[4][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[4][1])
            elif len(c[5]) > 2 and c[5][2] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[5][2])
            elif len(c[6]) > 1 and c[6][1] in ucdef.uc_versiones_marcadas:
                return convierte_version(c[6][1])
            else:
                return -2
    return -3


def genera_pagina_twemoji(pagina):
    identificados = [
        copy.deepcopy(c)
        for c in imp3.manual_1
        if not esta_eliminado(c[0]) and es_secuencia_fully_qualified(c[0])
    ]
    for i in range(len(identificados) - 1, -1, -1):
        # print(identificados[i])
        if identificados[i][2] == "":
            del identificados[i]
    t = ""
    numero_identificados_1 = len(identificados)
    # Primero muestro los que son caracteres simples
    # aunque según Unicode los texto-emoji deberían llevar FE0F
    grupos = ucdef.uc_tablas_caracteres[0] + ucdef.uc_grupos_twemoji
    grupos_caracteres = []
    for grupo in grupos:
        grupos_caracteres += [grupo[1]]
    # print(grupos_caracteres)

    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[1] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[1]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            t += f'  <section id="{grupo[1]}">\n'
            t += f"    <h2>{grupo[0]}</h2>\n"
            t += "\n"
            if contador == 1:
                t += f"    <p>Se muestra aquí {contador} carácter "
            else:
                t += f"    <p>Se muestran aquí {contador} caracteres "
            t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 18.0</a> en formato PDF.</p>\n'
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                if len(c[0]) > 1:
                    print(f"  CUIDADO: HAY UN CARACTER CON MÁS DE UN CARÁCTER: {c[0]}")
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += f"          U+{int(c[0][0], 16):X}<br>\n"
                vers = indica_version(c[0][0])
                # print (" emojis ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{c[2]}">&#x{int(c[0][0], 16):X};</a></span>\n'
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0][0], 16):x};</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0][0], 16)};</strong>\n"
                t += "        </p>\n"
                tmp = busca(c[0][0], imp.derived_name, 0)
                # print(tmp, c[0], imp.derived_name[tmp])
                t += f'        <p class="no">{imp.derived_name[tmp][1]}</p>\n'
                hay_coment = busca([c[0]][0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += '        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                    t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                    t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"
            t += "\n"
    numero_identificados_2 = len(identificados)

    # Después muestro las secuencias
    grupos = (
        ucdef.uc_grupos_otras
        + ucdef.uc_grupos_banderas
        + ucdef.uc_grupos_generos
        + ucdef.uc_grupos_fitzpatrick
        + ucdef.uc_grupos_parejas
    )
    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[0] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[0]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        if grupo[3] != ucdef.ORDENA_ESPECIAL_NO:
            caracteres = ordena(caracteres, grupo[3])
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            info_grupo = []
            for i in grupos:
                if i[0] == grupo[0]:
                    info_grupo = i
            t += f'  <section id="{grupo[0]}">\n'
            t += f"    <h2>{info_grupo[1]}</h2>\n"
            t += "\n"
            t += info_grupo[2]
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += "          "
                for cn in c[0]:
                    t += f"U+{int(cn, 16):X} "
                t += "<br>\n"
                vers = indica_version(c[0])
                # print (" secuencias ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{c[2]}">'
                for cn in c[0]:
                    t += f"&#x{int(cn, 16):X};"
                t += "</a></span>\n"
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += "          Hex:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += "</strong><br>\n"
                t += "          Dec:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#{int(cn, 16)};"
                t += "</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                hay_coment = busca(c[0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += '        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                    t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                    t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"

    numero_identificados_3 = len(identificados)
    print(
        f"    Dibujos identificados: {numero_identificados_1} - Caracteres: {numero_identificados_1 - numero_identificados_2} - Secuencias: {numero_identificados_2 - numero_identificados_3}"
    )
    print(f"    Identificados pendientes de dibujar: {numero_identificados_3}")
    # for i in identificados:
    #     print(i)

    # Por último muestro los que no están identificados
    restos_twemoji = [
        c
        for c in imp3.restos_twemoji
        if not esta_eliminado(c[0]) and es_secuencia_fully_qualified(c[0])
    ]
    print(f"    Dibujos no existentes en Unicode: {len(restos_twemoji)}")
    t += '  <section id="gr-twemoji-no-unicode">\n'
    t += "    <h2>Dibujos de Twemoji no definidos en Unicode</h2>\n"
    t += "\n"
    t += "     <p>En este apartado se muestran las imágenes incluidas en Twemoji que no están definidas en Unicode.</p>\n"
    t += "\n"
    t += '    <div class="u-l">\n'
    for c in restos_twemoji:
        t += '      <div class="u">\n'
        t += '        <p class="uc">\n'
        t += "          "
        for cn in c[0]:
            t += f"U+{int(cn, 16):X} "
        t += "<br>\n"
        vers = indica_version(c[0])
        # print (" secuencias ", vers)
        if float(vers) > 0:
            if len(str(vers)) > 2:
                vers_size = 220
            else:
                vers_size = 240
            t += (
                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                + 'width="75" viewBox="0 0 1180 512">\n'
                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                + 'stroke-width="20" stroke="red" />\n'
                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                + "           </svg>\n"
                + "          </span>\n"
            )
        t += "        </p>\n"
        t += '        <p class="si">\n'
        t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/{c[1]}">'
        for cn in c[0]:
            t += f"&#x{int(cn, 16):X};"
        t += "</a></span>\n"
        t += "        </p>\n"
        t += '        <p class="en">\n'
        t += "          Hex:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#x{int(cn, 16):x};"
        t += "</strong><br>\n"
        t += "          Dec:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#{int(cn, 16)};"
        t += "</strong>\n"
        t += "        </p>\n"
        t += "      </div>\n"
        t += "\n"
    t += "    </div>\n"
    t += "  </section>\n"
    t += "\n"
    return t


def genera_pagina_noto(pagina):
    identificados = [
        copy.deepcopy(c)
        for c in imp6.manual_1
        if not esta_eliminado(c[0]) and es_secuencia_fully_qualified(c[0])
    ]
    for i in range(len(identificados) - 1, -1, -1):
        if identificados[i][2] == "":
            del identificados[i]
    t = ""
    numero_identificados_1 = len(identificados)
    # Primero muestro los que son caracteres simples
    # aunque según Unicode los texto-emoji deberían llevar FE0F
    grupos = ucdef.uc_tablas_caracteres[0] + ucdef.uc_grupos_noto
    grupos_caracteres = []
    for grupo in grupos:
        grupos_caracteres += [grupo[1]]
    # print(grupos_caracteres)

    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[1] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[1]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            t += f'  <section id="{grupo[1]}">\n'
            t += f"    <h2>{grupo[0]}</h2>\n"
            t += "\n"
            if contador == 1:
                t += f"    <p>Se muestra aquí {contador} carácter "
            else:
                t += f"    <p>Se muestran aquí {contador} caracteres "
            t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 18.0</a> en formato PDF.</p>\n'
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                if len(c[0]) > 1:
                    print(f"  CUIDADO: HAY UN CARACTER CON MÁS DE UN CARÁCTER: {c[0]}")
                tmp = busca(c[0][0], imp.derived_name, 0)
                con_fe0f = imp.derived_name[tmp][2] == "texto-emoji"
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += f"          U+{int(c[0][0], 16):X}{' U+FE0F' if con_fe0f else ''}<br>\n"
                vers = indica_version(c[0][0])
                # print (" emojis ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/googlefonts/noto-emoji/refs/heads/main/2D/svg/{c[2]}">&#x{int(c[0][0], 16):X};{"&#xfe0f;" if con_fe0f else ""}</a></span>\n'
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0][0], 16):x};{'&amp;#xfe0f;' if con_fe0f else ''}</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0][0], 16)};{'&amp;#65039;' if con_fe0f else ''}</strong>\n"
                t += "        </p>\n"
                # print(tmp, c[0], imp.derived_name[tmp])
                t += f'        <p class="no">{imp.derived_name[tmp][1]}</p>\n'
                # hay_coment = busca([c[0]][0], imp5.manual_2, 0)
                # if hay_coment != -1:
                #     t += '        <p class="co">\n'
                #     for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                #         t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                #     t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                #     t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"
            t += "\n"
    numero_identificados_2 = len(identificados)

    # Después muestro las secuencias
    grupos = (
        ucdef.uc_grupos_otras
        + ucdef.uc_grupos_banderas
        + ucdef.uc_grupos_generos
        + ucdef.uc_grupos_fitzpatrick
        + ucdef.uc_grupos_parejas
        + ucdef.uc_grupos_sentido
    )
    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[0] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[0]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        if grupo[3] != ucdef.ORDENA_ESPECIAL_NO:
            caracteres = ordena(caracteres, grupo[3])
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            info_grupo = []
            for i in grupos:
                if i[0] == grupo[0]:
                    info_grupo = i
            t += f'  <section id="{grupo[0]}">\n'
            t += f"    <h2>{info_grupo[1]}</h2>\n"
            t += "\n"
            t += info_grupo[2]
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += "          "
                for cn in c[0]:
                    t += f"U+{int(cn, 16):X} "
                t += "<br>\n"
                vers = indica_version(c[0])
                # print (" secuencias ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/googlefonts/noto-emoji/refs/heads/main/2D/svg/{c[2]}">'
                for cn in c[0]:
                    t += f"&#x{int(cn, 16):X};"
                t += "</a></span>\n"
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += "          Hex:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += "</strong><br>\n"
                t += "          Dec:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#{int(cn, 16)};"
                t += "</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                # hay_coment = busca(c[0], imp5.manual_2, 0)
                # if hay_coment != -1:
                #     t += '        <p class="co">\n'
                #     for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                #         t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                #     t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                #     t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"

    numero_identificados_3 = len(identificados)
    print(
        f"    Dibujos identificados: {numero_identificados_1} - Caracteres: {numero_identificados_1 - numero_identificados_2} - Secuencias: {numero_identificados_2 - numero_identificados_3}"
    )
    print(f"    Identificados pendientes de dibujar: {numero_identificados_3}")
    # for i in identificados:
    #     print(i)

    # Por último muestro los que no están identificados
    restos_noto = [
        c
        for c in imp6.restos_noto
        if not esta_eliminado(c[0]) and es_secuencia_fully_qualified(c[0])
    ]
    print(f"    Dibujos no existentes en Unicode: {len(restos_noto)}")
    t += '  <section id="gr-noto-no-unicode">\n'
    t += "    <h2>Dibujos de Noto no definidos en Unicode</h2>\n"
    t += "\n"
    t += "     <p>En este apartado se muestran las imágenes incluidas en Noto que no están definidas en Unicode.</p>\n"
    t += "\n"
    t += '    <div class="u-l">\n'
    for c in restos_noto:
        t += '      <div class="u">\n'
        t += '        <p class="uc">\n'
        t += "          "
        for cn in c[0]:
            t += f"U+{int(cn, 16):X} "
        t += "<br>\n"
        vers = indica_version(c[0])
        # print (" secuencias ", vers)
        if float(vers) > 0:
            if len(str(vers)) > 2:
                vers_size = 220
            else:
                vers_size = 240
            t += (
                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                + 'width="75" viewBox="0 0 1180 512">\n'
                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                + 'stroke-width="20" stroke="red" />\n'
                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                + "           </svg>\n"
                + "          </span>\n"
            )
        t += "        </p>\n"
        t += '        <p class="si">\n'
        t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/googlefonts/noto-emoji/refs/heads/main/2D/svg/{c[1]}">'
        for cn in c[0]:
            t += f"&#x{int(cn, 16):X};"
        t += "</a></span>\n"
        t += "        </p>\n"
        t += '        <p class="en">\n'
        t += "          Hex:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#x{int(cn, 16):x};"
        t += "</strong><br>\n"
        t += "          Dec:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#{int(cn, 16)};"
        t += "</strong>\n"
        t += "        </p>\n"
        t += "      </div>\n"
        t += "\n"
    t += "    </div>\n"
    t += "  </section>\n"
    t += "\n"
    return t


def genera_pagina_twemoji_jdecked(pagina):
    identificados = [
        copy.deepcopy(c)
        for c in imp7.manual_1
        if not esta_eliminado(c[0])
        and es_secuencia_fully_qualified(agrega_selectores_variacion(c[0]))
    ]
    for i in range(len(identificados) - 1, -1, -1):
        # print(identificados[i])
        if identificados[i][2] == "":
            del identificados[i]
    t = ""
    numero_identificados_1 = len(identificados)
    # Primero muestro los que son caracteres simples
    # aunque según Unicode los texto-emoji deberían llevar FE0F
    grupos = ucdef.uc_tablas_caracteres[0] + ucdef.uc_grupos_twemoji_jdecked
    grupos_caracteres = []
    for grupo in grupos:
        grupos_caracteres += [grupo[1]]
    # print(grupos_caracteres)

    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[1] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[1]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            t += f'  <section id="{grupo[1]}">\n'
            t += f"    <h2>{grupo[0]}</h2>\n"
            t += "\n"
            if contador == 1:
                t += f"    <p>Se muestra aquí {contador} carácter "
            else:
                t += f"    <p>Se muestran aquí {contador} caracteres "
            t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 18.0</a> en formato PDF.</p>\n'
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                if len(c[0]) > 1:
                    print(f"  CUIDADO: HAY UN CARACTER CON MÁS DE UN CARÁCTER: {c[0]}")
                tmp = busca(c[0][0], imp.derived_name, 0)
                con_fe0f = imp.derived_name[tmp][2] == "texto-emoji"
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += f"          U+{int(c[0][0], 16):X}{' U+FE0F' if con_fe0f else ''}\n<br>"
                vers = indica_version(c[0][0])
                # print (" emojis ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/jdecked/twemoji/refs/heads/main/assets/svg/{c[2]}">&#x{int(c[0][0], 16):X};{"&#xfe0f;" if con_fe0f else ""}</a></span>\n'
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0][0], 16):x};{'&amp;#xfe0f;' if con_fe0f else ''}</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0][0], 16)};{'&amp;#65039;' if con_fe0f else ''}</strong>\n"
                t += "        </p>\n"
                # print(tmp, c[0], imp.derived_name[tmp])
                t += f'        <p class="no">{imp.derived_name[tmp][1]}</p>\n'
                # hay_coment = busca([c[0]][0], imp5.manual_2, 0)
                # if hay_coment != -1:
                #     t += '        <p class="co">\n'
                #     for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                #         t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                #     t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                #     t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"
            t += "\n"
    numero_identificados_2 = len(identificados)

    # Después muestro las secuencias
    grupos = (
        ucdef.uc_grupos_otras
        + ucdef.uc_grupos_banderas
        + ucdef.uc_grupos_generos
        + ucdef.uc_grupos_fitzpatrick
        + ucdef.uc_grupos_parejas
        + ucdef.uc_grupos_sentido
    )
    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) - 1, -1, -1):
            if (
                grupo[0] in identificados[i][1]
            ):  # Hago in porque algunos caracteres están en varios gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) - 1, -1, -1):
                    if identificados[i][1][j] == grupo[0]:
                        del identificados[i][1][j]
                if len(identificados[i][1]) == 0:
                    del identificados[i]
        caracteres.sort()
        if grupo[3] != ucdef.ORDENA_ESPECIAL_NO:
            caracteres = ordena(caracteres, grupo[3])
        contador = len(caracteres)
        # print(grupo[0], contador, len(identificados))
        if contador > 0:
            info_grupo = []
            for i in grupos:
                if i[0] == grupo[0]:
                    info_grupo = i
            t += f'  <section id="{grupo[0]}">\n'
            t += f"    <h2>{info_grupo[1]}</h2>\n"
            t += "\n"
            t += info_grupo[2]
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                codigos = agrega_selectores_variacion(c[0])
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += "          "
                for cn in codigos:
                    t += f"U+{int(cn, 16):X} "
                t += "<br>\n"
                vers = indica_version(c[0])
                # print (" secuencias ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/jdecked/twemoji/refs/heads/main/assets/svg/{c[2]}">'
                for cn in codigos:
                    t += f"&#x{int(cn, 16):X};"
                t += "</a></span>\n"
                t += "        </p>\n"
                t += '        <p class="en">\n'
                t += "          Hex:&nbsp;<strong>"
                for cn in codigos:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += "</strong><br>\n"
                t += "          Dec:&nbsp;<strong>"
                for cn in codigos:
                    t += f"&amp;#{int(cn, 16)};"
                t += "</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                # hay_coment = busca(c[0], imp5.manual_2, 0)
                # if hay_coment != -1:
                #     t += '        <p class="co">\n'
                #     for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                #         t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                #     t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                #     t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"

    numero_identificados_3 = len(identificados)
    print(
        f"    Dibujos identificados: {numero_identificados_1} - Caracteres: {numero_identificados_1 - numero_identificados_2} - Secuencias: {numero_identificados_2 - numero_identificados_3}"
    )
    print(f"    Identificados pendientes de dibujar: {numero_identificados_3}")
    # for i in identificados:
    #     print(i)

    # Por último muestro los que no están identificados
    restos_twemoji = [
        c
        for c in imp7.restos_twemoji
        if not esta_eliminado(c[0])
        and es_secuencia_fully_qualified(agrega_selectores_variacion(c[0]))
    ]
    print(f"    Dibujos no existentes en Unicode: {len(restos_twemoji)}")
    t += '  <section id="gr-twemoji-no-unicode">\n'
    t += "    <h2>Dibujos de Twemoji no definidos en Unicode</h2>\n"
    t += "\n"
    t += "     <p>En este apartado se muestran las imágenes incluidas en Twemoji que no están definidas en Unicode.</p>\n"
    t += "\n"
    t += '    <div class="u-l">\n'
    for c in restos_twemoji:
        t += '      <div class="u">\n'
        t += '        <p class="uc">\n'
        t += "          "
        for cn in c[0]:
            t += f"U+{int(cn, 16):X} "
        t += "<br>\n"
        vers = indica_version(c[0])
        # print (" secuencias ", vers)
        if float(vers) > 0:
            if len(str(vers)) > 2:
                vers_size = 220
            else:
                vers_size = 240
            t += (
                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                + 'width="75" viewBox="0 0 1180 512">\n'
                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                + 'stroke-width="20" stroke="red" />\n'
                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                + "           </svg>\n"
                + "          </span>\n"
            )
        t += "        </p>\n"
        t += '        <p class="si">\n'
        t += f'          <span class="twe"><a href="https://raw.githubusercontent.com/jdecked/twemoji/refs/heads/main/assets/svg/{c[1]}">'
        for cn in c[0]:
            t += f"&#x{int(cn, 16):X};"
        t += "</a></span>\n"
        t += "        </p>\n"
        t += '        <p class="en">\n'
        t += "          Hex:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#x{int(cn, 16):x};"
        t += "</strong><br>\n"
        t += "          Dec:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#{int(cn, 16)};"
        t += "</strong>\n"
        t += "        </p>\n"
        t += "      </div>\n"
        t += "\n"
    t += "    </div>\n"
    t += "  </section>\n"
    t += "\n"
    return t


def genera_pagina_caracteres(pagina):
    if pagina == ucdef.PAG_SIMBOLOS:
        t = ""
        for datos_grupo, codigos_grupo in obtiene_lista_simbolos():
            caracteres = []
            for c in imp.derived_name:
                if (
                    c[3] == datos_grupo[1]
                    and c[0] in codigos_grupo
                    and c[2] != "emoji"
                    and not esta_eliminado([c[0]])
                ):
                    caracteres += [c]
            caracteres.sort()
            contador = len(caracteres)
            # print(datos_grupo[0], contador)
            if contador > 0:
                t += f'  <section id="{datos_grupo[1]}">\n'
                t += f"    <h2>{datos_grupo[0]}</h2>\n"
                t += "\n"
                if contador == 1:
                    t += f"    <p>Se muestra aquí {contador} carácter "
                else:
                    t += f"    <p>Se muestran aquí {contador} caracteres "
                t += f'Unicode del grupo que se extiende desde el carácter U+{datos_grupo[3]} hasta el carácter U+{datos_grupo[4]}. Puede descargar la <a href="unicode/{datos_grupo[2]}">tabla de códigos de caracteres Unicode 18.0</a> en formato PDF.</p>\n'
                t += "\n"
                t += '    <div class="u-l">\n'
                for c in caracteres:
                    if c[2] == "texto" or c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">\n'
                        t += f"          U+{int(c[0], 16):X}<br>\n"
                        vers = indica_version(c[0])
                        # print (" emojis ", vers)
                        if float(vers) > 0:
                            if len(str(vers)) > 2:
                                vers_size = 220
                            else:
                                vers_size = 240
                            t += (
                                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                                + 'width="75" viewBox="0 0 1180 512">\n'
                                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                                + 'stroke-width="20" stroke="red" />\n'
                                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                                + "           </svg>\n"
                                + "          </span>\n"
                            )
                        t += "        </p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += '        <p class="co">\n'
                            for comentario in range(
                                len(imp5.manual_2[hay_coment][1]) - 1
                            ):
                                t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                            t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                            t += "        </p>\n"
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "emoji-texto":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">\n'
                        t += f"          U+{int(c[0], 16):X} U+FE0E<br>\n"
                        vers = indica_version(c[0])
                        # print (" emojis ", vers)
                        if float(vers) > 0:
                            if len(str(vers)) > 2:
                                vers_size = 220
                            else:
                                vers_size = 240
                            t += (
                                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                                + 'width="75" viewBox="0 0 1180 512">\n'
                                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                                + 'stroke-width="20" stroke="red" />\n'
                                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                                + "           </svg>\n"
                                + "          </span>\n"
                            )
                        t += "        </p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0e;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amp;#xfe0e;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};&amp;#65038;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += '        <p class="co">\n'
                            for comentario in range(
                                len(imp5.manual_2[hay_coment][1]) - 1
                            ):
                                t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                            t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                            t += "        </p>\n"
                        t += "      </div>\n"
                        t += "\n"
                t += "    </div>\n"
                t += "  </section>\n"
                t += "\n"
    elif pagina == ucdef.PAG_EMOJIS:
        t = ""
        for grupo in ucdef.uc_tablas_caracteres[0]:
            caracteres = []
            for c in imp.derived_name:
                if (
                    c[3] == grupo[1]
                    and c[2] != "texto"
                    and not esta_eliminado([c[0]])
                ):
                    caracteres += [c]
            caracteres.sort()
            contador = len(caracteres)
            if contador > 0:
                t += f'  <section id="{grupo[1]}">\n'
                t += f"    <h2>{grupo[0]}</h2>\n"
                t += "\n"

                if contador == 1:
                    t += f"    <p>Se muestra aquí {contador} carácter "
                else:
                    t += f"    <p>Se muestran aquí {contador} caracteres "
                t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 18.0</a> en formato PDF.</p>\n'
                t += "\n"
                t += '    <div class="u-l">\n'
                for c in caracteres:
                    if c[2] == "emoji" or c[2] == "emoji-texto":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">\n'
                        t += f"          U+{int(c[0], 16):X}<br>\n"
                        vers = indica_version(c[0])
                        # print (" emojis ", vers)
                        if float(vers) > 0:
                            if len(str(vers)) > 2:
                                vers_size = 220
                            else:
                                vers_size = 240
                            t += (
                                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                                + 'width="75" viewBox="0 0 1180 512">\n'
                                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                                + 'stroke-width="20" stroke="red" />\n'
                                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                                + "           </svg>\n"
                                + "          </span>\n"
                            )
                        t += "        </p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += '        <p class="co">\n'
                            for comentario in range(
                                len(imp5.manual_2[hay_coment][1]) - 1
                            ):
                                t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                            t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                            t += "        </p>\n"
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">\n'
                        t += f"          U+{int(c[0], 16):X} U+FE0F<br>\n"
                        vers = indica_version(c[0])
                        # print (" emojis ", vers)
                        if float(vers) > 0:
                            if len(str(vers)) > 2:
                                vers_size = 220
                            else:
                                vers_size = 240
                            t += (
                                f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                                + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                                + 'width="75" viewBox="0 0 1180 512">\n'
                                + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                                + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                                + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                                + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                                + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                                + 'stroke-width="20" stroke="red" />\n'
                                + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                                + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                                + "           </svg>\n"
                                + "          </span>\n"
                            )
                        t += "        </p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0f;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amp;#xfe0f;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};&amp;#65039;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += '        <p class="co">\n'
                            for comentario in range(
                                len(imp5.manual_2[hay_coment][1]) - 1
                            ):
                                t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                            t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                            t += "        </p>\n"
                        t += "      </div>\n"
                        t += "\n"
                t += "    </div>\n"
                t += "  </section>\n"
                t += "\n"
    return t


def ordena(cs1, tipo):
    if tipo == ucdef.ORDENA_ESPECIAL_1:
        orden_generos = ("1F9D1", "1F468", "1F469")
        grupos_genero = {genero: {} for genero in orden_generos}
        otros = []
        for caracter in cs1:
            genero = caracter[0][0]
            if genero not in grupos_genero:
                otros.append(caracter)
                continue
            secuencia = tuple(caracter[0][1:])
            grupos_genero[genero].setdefault(secuencia, []).append(caracter)

        cs = []
        secuencias = sorted(set().union(*(grupo.keys() for grupo in grupos_genero.values())))
        for secuencia in secuencias:
            for genero in orden_generos:
                cs.extend(grupos_genero[genero].get(secuencia, []))
        return cs + sorted(otros)
        # for c in cs:
        #     print(c)
    elif tipo == ucdef.ORDENA_ESPECIAL_2:
        cs2 = []
        cs3 = []
        cs4 = []
        cs5 = []
        for i in range(len(cs1) - 1, -1, -1):
            if cs1[i][0][1] == "1F3FC":
                cs2 += [cs1[i]]
                del cs1[i]
            elif cs1[i][0][1] == "1F3FD":
                cs3 += [cs1[i]]
                del cs1[i]
            elif cs1[i][0][1] == "1F3FE":
                cs4 += [cs1[i]]
                del cs1[i]
            elif cs1[i][0][1] == "1F3FF":
                cs5 += [cs1[i]]
                del cs1[i]
        cs1.sort()
        cs2.sort()
        cs3.sort()
        cs4.sort()
        cs5.sort()
        cs = []
        for i in range(len(cs1)):
            cs += [cs1[i]]
            cs += [cs2[i]]
            cs += [cs3[i]]
            cs += [cs4[i]]
            cs += [cs5[i]]
        return cs
        # for c in cs:
        #     print(c)
    return cs1


def genera_pagina_secuencias(pagina, grupos):
    t = ""
    for grupo in grupos:
        caracteres = []
        for c in imp3.manual_1:
            if esta_eliminado(c[0]) or not es_secuencia_fully_qualified(c[0]):
                continue
            for cgrupo in c[1]:
                if cgrupo == grupo[0]:
                    caracteres += [c]
        caracteres.sort()
        if grupo[3] != ucdef.ORDENA_ESPECIAL_NO:
            caracteres = ordena(caracteres, grupo[3])
        contador = len(caracteres)
        if contador > 0:
            info_grupo = []
            for i in grupos:
                if i[0] == grupo[0]:
                    info_grupo = i
            t += f'  <section id="{grupo[0]}">\n'
            t += f"    <h2>{info_grupo[1]}</h2>\n"
            t += "\n"
            t += info_grupo[2]
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                t += '      <div class="u">\n'
                t += '        <p class="uc">\n'
                t += "          "
                for cn in c[0]:
                    t += f"U+{int(cn, 16):X} "
                t += "<br>\n"
                vers = indica_version(c[0])
                # print (" secuencias ", vers)
                if float(vers) > 0:
                    if len(str(vers)) > 2:
                        vers_size = 220
                    else:
                        vers_size = 240
                    t += (
                        f'          <span class="ve" title="Nuevo en Unicode {vers} ({ucdef.uc_versiones_years[vers]})">\n'
                        + '           <svg version="1.1" xmlns="http://www.w3.org/2000/svg" '
                        + 'width="75" viewBox="0 0 1180 512">\n'
                        + '              <polygon points="22,254 85,215 53,135 137,132 141,48 213,83 260,20 307,83 354,20 '
                        + "401,83 448,20 495,83 542,20 589,83 636,20 683,83 730,20 777,83 824,20 871,83 918,20 965,83 "
                        + "1037,48 1041,132 1125,135 1093,215 1156,254 1093,293 1125,373 1041,376 1037,460 965,425 918,488 "
                        + "871,425 824,488 777,425 730,488 683,425 636,488 589,425 542,488 495,425 448,488 401,425 354,488 "
                        + '307,425 260,488 213,425 141,460 137,376 53,373 85,293" fill="none" '
                        + 'stroke-width="20" stroke="red" />\n'
                        + f'              <text x="600" y="340" font-family="sans-serif" font-size="{vers_size}" '
                        + f'font-weight="bold" text-anchor="middle" fill="red">New {vers}</text>\n'
                        + "           </svg>\n"
                        + "          </span>\n"
                    )
                t += "        </p>\n"
                t += '        <p class="si">'
                for cn in c[0]:
                    t += f"&#x{int(cn, 16):X};"
                t += "</p>\n"
                t += '        <p class="en">\n'
                t += "          Hex:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += "</strong><br>\n"
                t += "          Dec:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#{int(cn, 16)};"
                t += "</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                # print(c[0])
                hay_coment = busca(c[0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += '        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f"          {imp5.manual_2[hay_coment][1][comentario]}<br>\n"
                    t += f"          {imp5.manual_2[hay_coment][1][-1]}\n"
                    t += "        </p>\n"
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"
        t += "\n"
    return t


def main():
    print()
    print("GENERADOR DE PÁGINAS SIMBOLOS UNICODE PARA APUNTES HTMLS/CSS")

    # Comprueba que DESTINO no existe y lo borra si existe
    p = pathlib.Path(DESTINO)
    if p.exists():
        print()
        print(f"  El directorio de destino /{DESTINO} ya existe.")
        print("  El directorio de destino existente se borrará completamente.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta != "S":
            print("  El sitio no se ha creado.")
            sys.exit(0)
        else:
            shutil.rmtree(p)

    directorio = DESTINO
    p = pathlib.Path(directorio)
    if not p.exists():
        # print(f"  {directorio}")
        p.mkdir(parents=True, exist_ok=True)

    for recurso in (ucdef.FICHERO_TWEMOJI_JS, ucdef.FICHERO_TWEMOJI_LICENCIA):
        shutil.copy2(ORIGEN / recurso, DESTINO / recurso)

    # Crea páginas
    print()
    print("  Creando páginas")

    paginas = [
        [ucdef.PAG_SIMBOLOS, ucdef.FICHERO_SITIO_SIMBOLOS],
        [ucdef.PAG_EMOJIS, ucdef.FICHERO_SITIO_EMOJIS],
        [ucdef.PAG_BANDERAS, ucdef.FICHERO_SITIO_BANDERAS],
        [ucdef.PAG_GENEROS, ucdef.FICHERO_SITIO_GENEROS],
        [ucdef.PAG_FITZPATRICK, ucdef.FICHERO_SITIO_FITZPATRICK],
        [ucdef.PAG_PAREJAS, ucdef.FICHERO_SITIO_PAREJAS],
        [ucdef.PAG_SENTIDO, ucdef.FICHERO_SITIO_SENTIDO],
        [ucdef.PAG_OTRAS, ucdef.FICHERO_SITIO_OTRAS],
        [ucdef.PAG_NOTO, ucdef.FICHERO_SITIO_NOTO],
        [ucdef.PAG_TWEMOJI_ORIGINAL, ucdef.FICHERO_SITIO_TWEMOJI_ORIGINAL],
        [ucdef.PAG_TWEMOJI_JDECKED, ucdef.FICHERO_SITIO_TWEMOJI_JDECKED],
        # # # [ucdef.PAG_PROBLEMAS, ucdef.FICHERO_SITIO_PROBLEMAS],
    ]

    for pagina in paginas:
        fichero_origen = ORIGEN / pagina[1]
        fichero_destino = DESTINO / pagina[1]
        print(f"  Creando {fichero_destino}")
        with open(fichero_origen, "r", encoding="utf-8") as fichero:
            texto = Template(fichero.read())

        meses = [
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
        fecha = f"{datetime.date.today().strftime('%e')} de {meses[int(datetime.date.today().strftime('%m')) - 1]} de {datetime.date.today().strftime('%Y')}".strip()

        resultado = texto.safe_substitute(
            contenido=genera_pagina(pagina[0]), fecha=fecha
        )

        with open(fichero_destino, "w", encoding="utf-8", newline="\n") as fichero:
            fichero.write(resultado)

    # Para generar la lista de símbolos completa, a la que luego
    # quito los símbolos que no quiero que se vean
    print(f"  Creando {ucdef.FICHERO_SELECCION_SIMBOLOS}")
    genera_lista_simbolos()


if __name__ == "__main__":
    main()
