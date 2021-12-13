import copy
import pathlib
from string import Template
import shutil
import sys
import datetime
import webbrowser
import ucdef
from u14_ficheros_2_importados import unicode_txt_derived_name as imp
from u14_ficheros_3_fusionados import unicode_txt_fusionados_2 as imp2
from u14_ficheros_3_fusionados import unicode_txt_manual_1 as imp3
from u14_ficheros_3_fusionados import seleccion_simbolos_manual as imp4
from u14_ficheros_3_fusionados import unicode_txt_manual_2 as imp5

ORIGEN = pathlib.Path("sitio-plantilla")
DESTINO = pathlib.Path("sitio")

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
    elif pagina == ucdef.PAG_OTRAS:
        return genera_pagina_secuencias(pagina, ucdef.uc_grupos_otras)
    elif pagina == ucdef.PAG_TWEMOJI:
        return genera_pagina_twemoji(pagina)


def genera_lista_simbolos():
    # Esta función genera el fichero ucdef.FICHERO_SELECCION_SIMBOLOS
    # con todos los símbolos de las tablas de ucdef.uc_tablas_caracteres[0]
    t = "seleccion_simbolos_manual = [\n"
    for grupo in ucdef.uc_tablas_caracteres[0]:
        caracteres = []
        for c in imp.derived_name:
            if c[3] == grupo[1] and c[2] != "emoji":
                caracteres += [c]
        caracteres.sort()
        contador = len(caracteres)
        # print(grupo[1], contador)
        if contador > 0:
            t += f"  [ ['{grupo[0]}', '{grupo[1]}', '{grupo[2]}', '{grupo[3]}', '{grupo[4]}', ],\n"
            t += '    ['
            for c in caracteres:
                t += f"'{c[0]}', "
            t += "\n"
            t += "    ],\n"
            t += "  ],\n"
    t += "]\n"
    with open(ucdef.UNICODE_FUSIONADOS_DIR + "/" + ucdef.FICHERO_SELECCION_SIMBOLOS, "w", encoding="utf-8") as fichero:
        fichero.write(t)


def genera_pagina_twemoji(pagina):
    identificados = copy.deepcopy(imp3.manual_1)
    for i in range(len(identificados)-1, -1, -1):
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
        for i in range(len(identificados) -1, -1, -1):
            if grupo[1] in identificados[i][1]: # Hago in porque algunos caracteres están en vario gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) -1, -1, -1):
                    if identificados[i][1][j] == grupo[1]:
                        del(identificados[i][1][j])
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
            t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 14.0</a> en formato PDF.</p>\n'
            t += "\n"
            t += '    <div class="u-l">\n'
            for c in caracteres:
                if len(c[0]) > 1:
                    print(f"  CUIDADO: HAY UN CARACTER CON mÄS DE UN CARÁCTER: {c[0]}")
                t += '      <div class="u">\n'
                t += '        <p class="uc">'
                t += f"U+{int(c[0][0], 16):X} "
                t += "</p>\n"
                t += f'        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://github.com/twitter/twemoji/blob/master/assets/svg/{c[2]}">&#x{int(c[0][0], 16):X};</a></span>\n'
                t += '        </p>\n'
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0][0], 16):x};</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0][0], 16)};</strong>\n"
                t += "        </p>\n"
                tmp = busca(c[0][0], imp.derived_name, 0)
                # print(tmp, c[0], imp.derived_name[tmp])
                t += f'        <p class="no">{imp.derived_name[tmp][1]}</p>\n'
                hay_coment = busca([c[0]][0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += f'        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                    t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                    t += '        </p>\n'
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"
            t += "\n"
    numero_identificados_2 = len(identificados)

    # Después muestro las secuencias
    grupos = ucdef.uc_grupos_otras + ucdef.uc_grupos_banderas + ucdef.uc_grupos_generos + ucdef.uc_grupos_fitzpatrick + ucdef.uc_grupos_parejas
    for grupo in grupos:
        caracteres = []
        for i in range(len(identificados) -1, -1, -1):
            if grupo[0] in identificados[i][1]: # Hago in porque algunos caracteres están en vario gr
                caracteres += [identificados[i]]
                for j in range(len(identificados[i][1]) -1, -1, -1):
                    if identificados[i][1][j] == grupo[0]:
                        del(identificados[i][1][j])
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
                t += '        <p class="uc">'
                for cn in c[0]:
                    t += f"U+{int(cn, 16):X} "
                t += "</p>\n"
                t += f'        <p class="si">\n'
                t += f'          <span class="twe"><a href="https://github.com/twitter/twemoji/blob/master/assets/svg/{c[2]}">'
                for cn in c[0]:
                    t += f"&#x{int(cn, 16):X};"
                t += '</a></span>\n'
                t += f"        </p>\n"
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += f"</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#{int(cn, 16)};"
                t += f"</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                hay_coment = busca(c[0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += f'        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                    t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                    t += '        </p>\n'
                t += "      </div>\n"
                t += "\n"
            t += "    </div>\n"
            t += "  </section>\n"

    numero_identificados_3 = len(identificados)
    print(f"    Dibujos identificados: {numero_identificados_1} - Caracteres: {numero_identificados_1 - numero_identificados_2} - Secuencias: {numero_identificados_3 - numero_identificados_2}")
    print(f"    Identificados pendientes de dibujar: {numero_identificados_3}")
    # for i in identificados:
    #     print(i)

    # Por último muestro los que no están identificados
    print(f"    Dibujos no existentes en Unicode: {len(imp3.restos_twemoji)}")
    t += f'  <section id="gr-twemoji-no-unicode">\n'
    t += f"    <h2>Dibujos de Twemoji no definidos en Unicode</h2>\n"
    t += "\n"
    t += '     <p>En este apartado se muestran las imágenes incluidas en Twemoji que no están definidas en Unicode.</p>\n'
    t += "\n"
    t += '    <div class="u-l">\n'
    for c in imp3.restos_twemoji:
        t += '      <div class="u">\n'
        t += '        <p class="uc">'
        for cn in c[0]:
            t += f"U+{int(cn, 16):X} "
        t += "</p>\n"
        t += f'        <p class="si">\n'
        t += f'          <span class="twe"><a href="https://github.com/twitter/twemoji/blob/master/assets/svg/{c[1]}">'
        for cn in c[0]:
            t += f"&#x{int(cn, 16):X};"
        t += '</a></span>\n'
        t += f"        </p>\n"
        t += '        <p class="en">\n'
        t += f"          Hex:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#x{int(cn, 16):x};"
        t += f"</strong><br>\n"
        t += f"          Dec:&nbsp;<strong>"
        for cn in c[0]:
            t += f"&amp;#{int(cn, 16)};"
        t += f"</strong>\n"
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
        for grupo in imp4.seleccion_simbolos_manual:
            caracteres = []
            for c in imp.derived_name:
                if c[3] == grupo[0][1] and c[0] in grupo[1] and c[2] != "emoji":
                    caracteres += [c]
            caracteres.sort()
            contador = len(caracteres)
            # print(grupo[0], contador)
            if contador > 0:
                t += f'  <section id="{grupo[0][1]}">\n'
                t += f"    <h2>{grupo[0][0]}</h2>\n"
                t += "\n"
                if contador == 1:
                    t += f"    <p>Se muestra aquí {contador} carácter "
                else:
                    t += f"    <p>Se muestran aquí {contador} caracteres "
                t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[0][3]} hasta el carácter U+{grupo[0][4]}. Puede descargar la <a href="unicode/{grupo[0][2]}">tabla de códigos de caracteres Unicode 14.0</a> en formato PDF.</p>\n'
                t += "\n"
                t += '    <div class="u-l">\n'
                for c in caracteres:
                    if c[2] == "texto" or c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} "
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += f'        <p class="co">\n'
                            for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                                t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                            t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                            t += '        </p>\n'
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "emoji-texto":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} U+FE0E"
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0e;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amp;#xfe0e;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};&amp;#65038;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += f'        <p class="co">\n'
                            for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                                t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                            t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                            t += '        </p>\n'
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
                if c[3] == grupo[1] and c[2] != "texto":
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
                t += f'Unicode del grupo que se extiende desde el carácter U+{grupo[3]} hasta el carácter U+{grupo[4]}. Puede descargar la <a href="unicode/{grupo[2]}">tabla de códigos de caracteres Unicode 14.0</a> en formato PDF.</p>\n'
                t += "\n"
                t += '    <div class="u-l">\n'
                for c in caracteres:
                    if c[2] == "emoji" or c[2] == "emoji-texto":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} "
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += f'        <p class="co">\n'
                            for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                                t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                            t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                            t += '        </p>\n'
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} U+FE0F"
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0f;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amp;#xfe0f;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;#{int(c[0], 16)};&amp;#65039;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        hay_coment = busca([c[0]], imp5.manual_2, 0)
                        if hay_coment != -1:
                            t += f'        <p class="co">\n'
                            for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                                t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                            t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                            t += '        </p>\n'
                        t += "      </div>\n"
                        t += "\n"
                t += "    </div>\n"
                t += "  </section>\n"
                t += "\n"
    return t

def ordena(cs1, tipo):
    if tipo == ucdef.ORDENA_ESPECIAL_1:
        cs2 = []
        for i in range(len(cs1) - 1, -1, -1):
            if cs1[i][0][0] == "1F469":
                cs2 += [cs1[i]]
                del cs1[i]
        cs1.sort()
        cs2.sort()
        cs = []
        for i in range(len(cs1)):
            cs += [cs1[i]]
            cs += [cs2[i]]
        return cs
        for c in cs:
            print(c)
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
        for c in cs:
            print(c)
    return cs1

def genera_pagina_secuencias(pagina, grupos):
    t = ""
    for grupo in grupos:
        caracteres = []
        for c in imp3.manual_1:
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
                t += '        <p class="uc">'
                for cn in c[0]:
                    t += f"U+{int(cn, 16):X} "
                t += "</p>\n"
                t += f'        <p class="si">'
                for cn in c[0]:
                    t += f"&#x{int(cn, 16):X};"
                t += f"</p>\n"
                t += '        <p class="en">\n'
                t += f"          Hex:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#x{int(cn, 16):x};"
                t += f"</strong><br>\n"
                t += f"          Dec:&nbsp;<strong>"
                for cn in c[0]:
                    t += f"&amp;#{int(cn, 16)};"
                t += f"</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                hay_coment = busca(c[0], imp5.manual_2, 0)
                if hay_coment != -1:
                    t += f'        <p class="co">\n'
                    for comentario in range(len(imp5.manual_2[hay_coment][1]) - 1):
                        t += f'          {imp5.manual_2[hay_coment][1][comentario]}<br>\n'
                    t += f'          {imp5.manual_2[hay_coment][1][-1]}\n'
                    t += '        </p>\n'
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
        [ucdef.PAG_OTRAS, ucdef.FICHERO_SITIO_OTRAS],
        [ucdef.PAG_TWEMOJI, ucdef.FICHERO_SITIO_TWEMOJI],
        # [ucdef.PAG_PROBLEMAS, ucdef.FICHERO_SITIO_PROBLEMAS],
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
