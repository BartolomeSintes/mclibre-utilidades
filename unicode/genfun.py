# 1 de septiembre de 2018
import copy
import gendef
import unicode_grupos


# CAMPOS
# rutaSVG = "https://github.com/emojione/emojione/blob/2.2.7/assets/svg"
# rutaSVG = "https://github.com/twitter/twemoji/blob/gh-pages/2/svg" # cambiado en 2019-10-27
RUTAS_SVG = "https://github.com/twitter/twemoji/blob/master/assets/svg"

# genera_enlace_tg(c)
# * le llegan sólo los códigos unicode para poder enlazar al repositorio de gendef.TWEmoji
# * no analiza nada, lo que le llega lo pone en el enlace
#
# genera_caracter(c, fuente)
# * le llegan los códigos unicode y la fuente en que debe verse la entidad numérica
# * sólo analiza qué fuente se ha pedido para poner la clase corespondiente en el span y en su caso, el enlace al repositorio de gendef.TWEmoji
#
# funcion genera_ficha(simbolos)
# * le llegan una matriz de parejas [c, fuente]
# * no analiza nada, sólo crea la ficha. El texto lo saca de la primera pareja simbolos[0]
#
# funcion genera_fichas(c, fuentes)
# * le llegan los caracteres unicode y una matriz de fuentes
# * tiene que analizar

# def aVer(dato):
# {
#     if gettype(dato)=="array":
#         print "\n<pre>"
#         print_r(dato)
#         print "</pre>\n"
#     else:
#         print "\n<span style=\"red\">*** dato ***</span>\n"
#     }
# }


def genera_enlace_tgh(c):
    resp = '<a href="' + RUTAS_SVG + "/"
    for valor in c:
        resp += f"{int(valor, 16):x}-"
    resp = resp[:-1]    # Quita el ultimo guion
    resp += '.svg">'
    return resp


def genera_caracter(c, fuente):
    # fuente puede ser vacío, SS, TCF, TGH, SYM,
    resp = ""
    span = enlace = False
    if fuente == "SS":
        resp = '\n          <span class="ss">'
        span = True
    elif fuente == "SYM":
        resp = '\n          <span class="sy">'
        span = True
    elif fuente == "TGH":
        resp = '\n          <span class="twe">'
        if c[gendef.TWE] != "":
            resp += genera_enlace_tgh(c[gendef.UCO])
            enlace = True
        span = True
    elif fuente == "TCF":
        resp = '\n          <span class="te">'
        if c[gendef.TWE] != "":
            resp += genera_enlace_tgh(c[gendef.UCO])
            enlace = True
        span = True
    # else:
    #     print(f"Error: Sin fuente en genera_caracter()")
    #     traceback.print_exc()
    for tmp in c[gendef.UCO]:
        resp += f"&#x{int(tmp, 16):X};"
    if enlace:
        resp += "</a>"
    if span:
        resp += "</span>\n"
    return resp


def genera_ficha(simbolos):
    # simbolos es una matriz de parejas [c, fuente]
    # c ya incluye gendef.VS o Fitzpatrick
    # fuente puede ser SS, TCF, TGH, SYM,
    t = ""
    if len(simbolos) == 1:
        t += '      <div class="u">\n'
    else:
        t += '      <div class="u2">\n'
    t += '        <p class="uc">'
    # Código Unicode
    for tmp in simbolos[0][0][gendef.UCO]:
        t += f"U+{int(tmp, 16):X} "
    t += "</p>\n"
    # Dibujo(s)
    t += '        <p class="si">'
    # Este if era para que si sólo hay un símbolo no ponga class="SS", pero me da igual que lo ponga
    # if len(simbolos) == 1 and simbolos[0][1] == "SS":
    #     simbolos[0][1] = ""
    for simbolo in simbolos:
        c = simbolo[0]
        f = simbolo[1]
        t += genera_caracter(c, f)
    t += "        </p>\n"
    # Entidad numérica hexadecimal
    t += '        <p class="en">Hex: <strong>'
    for tmp in simbolos[0][0][gendef.UCO]:
        t += f"&amp;#x{int(tmp, 16):x};"
    t += "</strong></p>\n"
    # Entidad numérica adecimal
    t += '        <p class="en">Dec: <strong>'
    for tmp in simbolos[0][0][gendef.UCO]:
        t += f"&amp;#{int(tmp, 16)};"
    t += "</strong></p>\n"
    # Descripción
    t += f'        <p class="no">{c[gendef.DESC]}</p>\n'
    t += "      </div>\n"
    t += "\n"
    return t


def prepara_ficha(c, fuentes, pagina):
    # simbolos es una matriz de [c, gendef.VS, fp, fuente]
    # c es el código Unicode con toda la información
    # gendef.VSte es qué se hace con gendef.VS: Vacío / gendef.VSE / gendef.VST
    # fp es qué hace con FP: Vacío / pone uno en concreto o pone todos
    # fuente puede ser SS, SYM, TGH, TCF o mixto SS-TCF-TGH-SYM, SS-TGH, SS-SYM, SS-TGH-
    datos = []
    for fuente in fuentes:
        tmp = []
        if fuente == "":
            t += "<h1>Error: No se ha indicado fuente en genera_fichas()</h1>\n"
        elif fuente == "SS":
            tmp = [c, "SS"]
        elif fuente == "SS-VST":
            # Tengo que hacer deepcopy para que el FE0E no aparezca en el enlace a Twemoji
            c2 = copy.deepcopy(c)
            if c2[gendef.VS] == "VSE":
                c2[gendef.UCO] += ["FE0E"]
            tmp = [c2, "SS"]
        elif fuente == "SS-VSE":
            # Tengo que hacer deepcopy para que el FE0E no aparezca en el enlace a Twemoji
            c2 = copy.deepcopy(c)
            # Este if es para el caso especial de las keycap sequences en las que FE0F va en segundo lugar
            # tendré que cambiarlo cuando llegue a las secuencias seguro
            if len(c2[gendef.UCO]) == 2 and c2[gendef.UCO][1] == "0020E3":
                c2[gendef.UCO] = [c2[gendef.UCO][0], "FE0F", c2[gendef.UCO][1]]
            elif c2[gendef.VS] == "VST":
                c2[gendef.UCO] += ["FE0F"]
            tmp = [c2, "SS"]
        elif fuente == "TGH":
            tmp = [c, "TGH"]
        elif fuente == "TCF":
            tmp = [c, "TCF"]
        elif fuente == "SYM":
            tmp = [c, "SYM"]
        elif fuente == "TCF-TGH":
            if c[gendef.TWO] == "TCF":
                tmp = [c, "TCF"]
            elif c[gendef.TWO] == "TGH":
                tmp = [c, "TGH"]
        if pagina == gendef.PAG_SIMBOLOS:
            if fuente == "SYM" and c[gendef.WIN] != "":
                pass
            else:
                datos += [tmp]
        elif pagina == gendef.PAG_EMOJIS:
            if fuente == "SS-VSE":
                datos += [tmp]
            elif fuente == "TCF-TGH" and c[gendef.TWE] != "":
                datos += [tmp]
    return genera_ficha(datos)
    # if segundo == "TGH" or c[gendef.WIN] == "" andc[gendef.TWO] == "TGH" andc[gendef.VS] != "gendef.VST":
    #     print genera_caracter(c[gendef.UCO], "TGH")
    # elif segundo == "TCF" or segundo = "" andc[gendef.WIN] == "" andc[gendef.TWO] == "TCF" andc[gendef.VS] != "gendef.VST":
    #     print genera_caracter(c[gendef.UCO], "TCF")


def genera_grupo(
    matriz, grupo, identificador, pdf, cuenta, inicial, final, fuentes, pagina
):
    if cuenta:
        contador = len(matriz)
    t = ""
    if not (cuenta) or cuenta and contador > 0:
        t += f'  <section id="{identificador}">\n'
        t += f"    <h2>{grupo}</h2>\n"
        t += "\n"

        if cuenta:
            if contador == 1:
                t += f"    <p>Se muestra aquí {contador} carácter "
            else:
                t += f"    <p>Se muestran aquí {contador} caracteres "
            t += f'Unicode del grupo que se extiende desde el carácter U+{inicial} hasta el carácter U+{final}. Puede descargar la <a href="unicode/{pdf}">tabla de códigos de caracteres Unicode 13.0</a> en formato PDF.</p>\n'
            t += "\n"

        t += '    <div class="u-l">\n'
        for c in matriz:
            t += prepara_ficha(c, fuentes, pagina)
        t += "    </div>\n"
        t += "  </section>\n"
        t += "\n"
    return t


def genera_grupos(pagina, fuentes):
    t = ""

    # Como están ya incluidos en la plantilla, no gebnero el índice
    # aunque estaría bien generarlos y quitarlos de la plantilla
    # t += "  <ul>\n"
    # for g in unicode_grupos.grupos[pagina]:
    #     t += f'    <li><a href="#{g[2]}">{g[1]}</a></li>\n'
    # t += "  </ul>\n"
    # t += "\n"

    for g in unicode_grupos.grupos[pagina]:
        t += genera_grupo(g[0], g[1], g[2], g[3], g[4], g[5], g[6], fuentes, pagina)

    return t


# foreach (caracteres_unicode as c:
#     # foreach (caracteres_unicode_seleccion as c:
#         print "<div class=\"u-l\">\n"
#         prepara_ficha(c, ["SS-VST"])
#         prepara_ficha(c, ["SS-VSE"])
#         prepara_ficha(c, ["TGH"])
#         print "</div>\n"
#     }


def genera_pagina(pagina):
    if pagina == gendef.PAG_SIMBOLOS:
        # HAY QUE CAMBIAR VARIABLE MUESTRA EN LINEA 6 A SIMBOLOS O EMOJIS
        return genera_grupos(gendef.PAG_SIMBOLOS, ["SS-VST", "SYM"])
    elif pagina == gendef.PAG_EMOJIS:
        # HAY QUE CAMBIAR VARIABLE MUESTRA EN LINEA 6 A SIMBOLOS O EMOJIS
        return genera_grupos(gendef.PAG_EMOJIS, ["SS-VSE", "TCF-TGH"])

    # genera_variantes(variacion, "Secuencias de variación", "variacion")


# HAY CAMBIAR VARIABLE MUESTRA EN LINEA 6 A EMOJIS
# genera_grupos(grupos_secuencias_1, ["ss", "te"])      # Banderas
# genera_grupos(grupos_secuencias_2, ["ss", "te"])      # Géneros OK
# genera_tablas(grupos_secuencias_3, ["ss", "te"])      # Colores de piel: OK
# genera_grupos(grupos_secuencias_4, ["ss", "te"])      # Familias y parejas
# genera_grupos(grupos_secuencias_problematicas_1, ["ss", "te"])     # Animales y otros: No Windows
# genera_grupos(grupos_secuencias_problematicas_2, ["ss", "te"])     # Géneros: No Windows o No gendef.TWEmoji
# genera_tablas(grupos_secuencias_problematicas_3, ["ss", "te"])     # Colores de piel: No Windows o No gendef.TWEmoji

# aVer(filtra_grupo(caracteres_unicode, "0000", "007F", gendef.PAG_SIMBOLOS))
# genera_pagina(gendef.PAG_SIMBOLOS)
# genera_pagina(gendef.PAG_EMOJIS)

# Puñetitas varias
# * No he tenido en cuenta si hay un carácter simple que no se ve en Windows pero sí está en gendef.TWEmoji
# * Parece que en temoji todo los caracteres simples se llaman solamente con el código, pero si son gendef.VST no se añade
# * Los caracteres 0023, 002A, etc. para que se vean se tiene que escribir con 20E3 al final, así que los he puesto en secuencias,
#   pero se supone que tiene versión texto y emoji, pero en Windows no se ven
# * El carácter 2122 (trade mark) está en TCF, pero si pongo TGH no sale bien, no sé por qué
# * El carácter  25FC no se ve igual si está en párrafo clase .si (sin span), que si tiene un span clase .ss. No lo entiendo.
# * El carácter 25FD y 25 FE son gendef.VST, pero para que enlace al respositorio tengo que poner gendef.VSE Creo que es un error de Twitter


# def genera_variantes(matriz, grupo, id)
# {
#     global rutaSVG, muestra

#     contador = len(matriz)

#     if contador > 0:
#         print "  <section id=\"id\">\n"
#         print "    <h2>grupo</h2>\n"
#         print "\n"

#         if contador == 1:
#             print "    <p>Se muestra aquí contador carácter de variación</p>\n"
#         else:
#             print "    <p>Se muestran aquí contador caracteres de variación</p>\n"
#         }
#         print "\n"
#         foreach (matriz as origen:
#             print "    <div class=\"u-l\">\n"
#             triplete = [origen, origen, origen]
#             triplete[1][0][] = "0FE0E"
#             triplete[2][0][] = "0FE0F"
#             foreach (triplete as c:
#                 print "      <div class=\"u\">\n"
#                 print "        <p class=\"uc\">"
#                 foreach (c[0] as tmp:
#                     print "U+" . strtoupper(dechex(hexdec(tmp))) . " "
#                 }
#                 print "</p>\n"
#                 print "        <p class=\"si\">"
#                 foreach (c[0] as tmp:
#                     print "&#x" . strtoupper(dechex(hexdec(tmp))) . ";"
#                 }
#                 print "</p>\n"
#                 print "        <p class=\"en\"><strong>"
#                 foreach (c[0] as tmp:
#                     print "&amp;#x" . dechex(hexdec(tmp)) . ";"
#                 }
#                 print "</strong></p>\n"
#                 print "        <p class=\"en\"><strong>"
#                 foreach (c[0] as tmp:
#                     print "&amp;#" . hexdec(tmp) . ";"
#                 }
#                 print "</strong></p>\n"
#                 print "        <p class=\"no\">c[7]</p>\n"
#                 print "      </div>\n"
#                 print "\n"
#             }
#             print "    </div>\n"
#         }
#         print "  </section>\n"
#         print "\n"
#     }
# }

# def genera_tabla_colores_piel(matriz, grupo, id, pdf, cuenta, inicial, final, fuentes)
# {
#     global rutaSVG

#     print "  <section id=\"id\">\n"
#     print "    <h2>grupo</h2>\n"
#     print "\n"

#     if cuenta:
#         contador = 0
#         foreach (matriz as c:
#             contador++
#         }
#         if contador == 1:
#             print "    <p>Se muestra aquí contador carácter "
#         else:
#             print "    <p>Se muestran aquí contador caracteres "
#         }
#         print "Unicode que al secuenciarse con los cinco modificadores Fitzpatrick (U+1F3FB a U+1F3FF) dan lugar cada uno a cinco nuevos emojis con distintos colores de piel.</p>\n"
#         print "\n"
#         print "    <p>Los caracteres se muestran únicamente con la fuente gendef.TWEmoji y el resultado depende del sistema operativo y del navegador empleado.</p>\n"
#         print "\n"
#     }

#     print "    <table class=\"u\">\n"
#     print "      <col>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <colgroup span=\"2\" class=\"borde-lateral\"></colgroup>\n"
#     print "      <col>\n"
#     print "      <tr class=\"fila-estrecha\">\n"
#     print "        <th rowspan=\"2\">Códigos</th>\n"
#     print "        <th colspan=\"2\" rowspan=\"2\">Sin color de piel</th>\n"
#     print "        <th colspan=\"10\">Con color de piel</th>\n"
#     print "        <th rowspan=\"2\">Nombres</th>\n"
#     print "      </tr>\n"
#     print "      <tr class=\"fila-estrecha\">\n"
#     print "        <th colspan=\"2\">&amp;#x1F3FB</th>\n"
#     print "        <th colspan=\"2\">&amp;#x1F3FC</th>\n"
#     print "        <th colspan=\"2\">&amp;#x1F3FD</th>\n"
#     print "        <th colspan=\"2\">&amp;#x1F3FE</th>\n"
#     print "        <th colspan=\"2\">&amp;#x1F3FF</th>\n"
#     print "      </tr>\n"
#     foreach (matriz as c:
#         print "      <tr>\n"
#         print "        <th>"
#         cad1 = cad2 = cad3 = ""
#         foreach (c[0] as c2:
#             tmp = strtolower(c2)
#             while (tmp[0] == "0":
#                 tmp = substr(tmp, 1)
#             }
#             cad1 .= "U+" . c2 . " "
#             cad2 .= tmp . "-"
#             cad3 .=  "&#x" . strtoupper(dechex(hexdec(c2))) . ";"
#             print "&amp;#x" . strtoupper(dechex(hexdec(c2))) . "<wbr>"
#         }
#         print "</th>\n"
#         cad2 = substr(cad2, 0, strlen(cad2) - 1) # quito el guion final que sobra
#         print "        <td class=\"ss\">cad3</td>\n"
#         if c[6] == "TW":
#             print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#         else:
#             print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#         }
#         # CUIDADO: Hay varios casos especiales en los que el Fitzpatrick sustituye al segundo carácter de la secuencia
#         cad2 = str_replace("26f9-fe0f-", "26f9-", cad2)
#         cad2 = str_replace("1f3cb-fe0f-", "1f3cb-", cad2)
#         cad2 = str_replace("1f3cc-fe0f-", "1f3cc-", cad2)
#         cad2 = str_replace("1f46e-fe0f-", "1f46e-", cad2)
#         cad2 = str_replace("1f574-fe0f-", "1f574-", cad2)
#         cad2 = str_replace("1f575-fe0f-", "1f575-", cad2)
#         pos = strpos(cad2, "-", 2)
#         if pos == 0:
#             cad2 .= "-1f3fb"
#         else:
#             cad2 = substr_replace(cad2, "1f3fb-", pos + 1, 0)
#         }
#         pos = strpos(cad3, "", 4)
#         cad3 = substr_replace(cad3, "&#x1F3FB", pos + 1, 0)
#         print "        <td class=\"ss\">cad3</td>\n"
#         if in_array("te", fuentes):
#             if c[6] == "TW":
#                 print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             else:
#                 print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             }
#         }
#         cad2 = str_replace("1f3fb", "1f3fc", cad2)
#         cad3 = str_replace("&#x1F3FB", "&#x1F3FC", cad3)
#         print "        <td class=\"ss\">cad3</td>\n"
#         if in_array("te", fuentes):
#             if c[6] == "TW":
#                 print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             else:
#                 print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             }
#         }
#         cad2 = str_replace("1f3fc", "1f3fd", cad2)
#         cad3 = str_replace("&#x1F3FC", "&#x1F3FD", cad3)
#         print "        <td class=\"ss\">cad3</td>\n"
#         if in_array("te", fuentes):
#             if c[6] == "TW":
#                 print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             else:
#                 print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             }
#         }
#         cad2 = str_replace("1f3fd", "1f3fe", cad2)
#         cad3 = str_replace("&#x1F3FD", "&#x1F3FE", cad3)
#         print "        <td class=\"ss\">cad3</td>\n"
#         if in_array("te", fuentes):
#             if c[6] == "TW":
#                 print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             else:
#                 print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             }
#         }
#         cad2 = str_replace("1f3fe", "1f3ff", cad2)
#         cad3 = str_replace("&#x1F3FE", "&#x1F3FF", cad3)
#         print "        <td class=\"ss\">cad3</td>\n"
#         if in_array("te", fuentes):
#             if c[6] == "TW":
#                 print "        <td class=\"gendef.TWE\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             else:
#                 print "        <td class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></td>\n"
#             }
#         }
#         print "        <td class=\"no\">c[7]</td>\n"

#         # print "        <td><span class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></span></td>\n"
#         # cad2 = str_replace("1f3fb", "1f3fc", cad2)
#         # cad3 = str_replace("&#x1F3FB", "&#x1F3FC", cad3)
#         # print "        <td><span class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></span></td>\n"
#         # cad2 = str_replace("1f3fc", "1f3fd", cad2)
#         # cad3 = str_replace("&#x1F3FC", "&#x1F3FD", cad3)
#         # print "        <td><span class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></span></td>\n"
#         # cad2 = str_replace("1f3fd", "1f3fe", cad2)
#         # cad3 = str_replace("&#x1F3FD", "&#x1F3FE", cad3)
#         # print "        <td><span class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></span></td>\n"
#         # cad2 = str_replace("1f3fe", "1f3ff", cad2)
#         # cad3 = str_replace("&#x1F3FE", "&#x1F3FF", cad3)
#         # print "        <td><span class=\"te\"><a href=\"rutaSVG/cad2.svg\">cad3</a></span></td>\n"
#         # print "        <td>" . strtoupper(c[7]) . " </td>\n"

#         print "      </tr>\n"
#     }
#     print "    </table>\n"
#     print "  </section>\n"
#     print "\n"
# }

# def genera_tablas(grupos)
# {
#     print "  <ul>\n"
#     foreach (grupos as g:
#         print "    <li><a href=\"#g[2]\">g[1]</a></li>\n"
#     }
#     print "  </ul>\n"
#     print "\n"

#     foreach (grupos as g:
#         genera_tabla_colores_piel(g[0], g[1], g[2], g[3], g[4], g[5], g[7], g[7])
#     }
# }
