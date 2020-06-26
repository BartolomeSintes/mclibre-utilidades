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


def genera_enlace_tgh(c, quita_fe0f):
    resp = '<a href="' + RUTAS_SVG + "/"
    for i in range(len(c)):
        if quita_fe0f == gendef.QUITA_FE0F_NO or i != 1 or c[i] != "0FE0F":
            resp += f"{int(c[i], 16):x}-"
    resp = resp[:-1]  # Quita el ultimo guion
    resp += '.svg">'
    return resp


def genera_caracter(c, fuente, quita_fe0f):
    # fuente puede ser vacío, SS, TCF, TGH, SYM,
    resp = ""
    span = enlace = False
    if fuente == "SS":
        resp = '          <span class="ss">'
        span = True
    elif fuente == "SYM":
        resp = '          <span class="sy">'
        span = True
    elif fuente == "TGH":
        resp = '          <span class="twe">'
        if c[gendef.TWE] != "":
            resp += genera_enlace_tgh(c[gendef.UCO], quita_fe0f)
            enlace = True
        span = True
    elif fuente == "TCF":
        resp = '          <span class="te">'
        if c[gendef.TWE] != "":
            resp += genera_enlace_tgh(c[gendef.UCO], quita_fe0f)
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
        resp += "</span>"
    resp += "\n"
    return resp


def genera_ficha(simbolos, quita_fe0f):
    # simbolos es una matriz de parejas [c, fuente]
    # c ya incluye gendef.VS o Fitzpatrick
    # fuente puede ser SS, TCF, TGH, SYM,
    # print("genera_ficha:", end="")
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
    t += '        <p class="si">\n'
    # Este if era para que si sólo hay un símbolo no ponga class="SS", pero me da igual que lo ponga
    # if len(simbolos) == 1 and simbolos[0][1] == "SS":
    #     simbolos[0][1] = ""
    for simbolo in simbolos:
        c = simbolo[0]
        f = simbolo[1]
        # print(c, f)
        t += genera_caracter(c, f, quita_fe0f)
    t += "        </p>\n"
    # Entidad numérica hexadecimal
    t += '        <p class="en">\n'
    t += "          Hex: <strong>"
    for tmp in simbolos[0][0][gendef.UCO]:
        t += f"&amp;#x{int(tmp, 16):x};"
    t += "</strong><br>\n"
    # Entidad numérica adecimal
    t += "          Dec: <strong>"
    for tmp in simbolos[0][0][gendef.UCO]:
        t += f"&amp;#{int(tmp, 16)};"
    t += "</strong>\n"
    t += "        </p>\n"
    # Descripción
    t += f'        <p class="no">{c[gendef.DESC]}</p>\n'
    t += "      </div>\n"
    t += "\n"
    return t


def prepara_ficha(c, fuentes, pagina, quita_fe0f):
    # simbolos es una matriz de [c, gendef.VS, fp, fuente]
    # c es el código Unicode con toda la información
    # gendef.VSte es qué se hace con gendef.VS: Vacío / gendef.VSE / gendef.VST
    # fp es qué hace con FP: Vacío / pone uno en concreto o pone todos
    # fuente puede ser SS, SYM, TGH, TCF o mixto SS-TCF-TGH-SYM, SS-TGH, SS-SYM, SS-TGH-
    # print("prepara_ficha: ", c, fuentes, pagina)
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
        else:
            if tmp != []:
                datos += [tmp]
    return genera_ficha(datos, quita_fe0f)
    # if segundo == "TGH" or c[gendef.WIN] == "" andc[gendef.TWO] == "TGH" andc[gendef.VS] != "gendef.VST":
    #     print genera_caracter(c[gendef.UCO], "TGH")
    # elif segundo == "TCF" or segundo = "" andc[gendef.WIN] == "" andc[gendef.TWO] == "TCF" andc[gendef.VS] != "gendef.VST":
    #     print genera_caracter(c[gendef.UCO], "TCF")


def genera_grupo(
    matriz,
    grupo,
    identificador,
    pdf,
    cuenta,
    inicial,
    final,
    fitzpatrick,
    comentario,
    fuentes,
    pagina,
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

        if comentario:
            t += comentario

        t += '    <div class="u-l">\n'
        if fitzpatrick != gendef.FITZPATRICK_NO:
            for c in matriz:
                for piel in gendef.fitzpatrick:
                    # en las secuencias el código Fitzpatrick va el segundo
                    c2 = copy.deepcopy(c)
                    c2[gendef.UCO][1:1] += [piel[0]]
                    c2[gendef.DESC] += piel[1]
                    if (
                        c[gendef.VS] == "VST"
                        and fitzpatrick == gendef.FITZPATRICK_YES_TEXTO
                    ):
                        fuentes2 = copy.deepcopy(fuentes)
                        fuentes2.remove("TCF-TGH")
                        t += prepara_ficha(c2, fuentes2, pagina, gendef.QUITA_FE0F_NO)
                    elif (
                        c[gendef.VS] == "VST"
                        and fitzpatrick == gendef.FITZPATRICK_YES_EMOJI
                    ):
                        c2 = copy.deepcopy(c)
                        c2[gendef.UCO][1:1] += ["0FE0F", piel[0]]
                        c2[gendef.DESC] += piel[1]
                        t += prepara_ficha(c2, fuentes, pagina, gendef.QUITA_FE0F_YES)
                    elif (
                        c[gendef.VS] == "VST"
                        and fitzpatrick == gendef.FITZPATRICK_YES_EMOJI_3
                    ):
                        c2 = copy.deepcopy(c)
                        c2[gendef.UCO][2:2] += [piel[0]]
                        c2[gendef.DESC] += piel[1]
                        t += prepara_ficha(c2, fuentes, pagina, gendef.QUITA_FE0F_YES)
                    elif fitzpatrick == gendef.FITZPATRICK_YES_EMOJI:
                        c2 = copy.deepcopy(c)
                        c2[gendef.UCO][1:1] += [piel[0]]
                        c2[gendef.DESC] += piel[1]
                        t += prepara_ficha(c2, fuentes, pagina, gendef.QUITA_FE0F_YES)
                    else:
                        t += prepara_ficha(c2, fuentes, pagina, gendef.QUITA_FE0F_YES)
                    # en los caracteres con modo emoji, el código Fitzpatrick va el tecero
        else:
            for c in matriz:
                # El criterio para quitar los FE0F en enlace a githuba es que sean fitzpatrick
                # pero el eye in speech bubble es una excepción así que lo he puesto aquí
                if c[0] == ["1F441", "FE0F", "0200D", "1F5E8", "FE0F"]:
                    t += prepara_ficha(c, fuentes, pagina, gendef.QUITA_FE0F_YES)
                else:
                    t += prepara_ficha(c, fuentes, pagina, gendef.QUITA_FE0F_NO)
        t += "    </div>\n"
        t += "  </section>\n"
        t += "\n"
    return t


def genera_grupos(pagina, fuentes):
    t = ""

    # Como están ya incluidos en la plantilla, no genero el índice
    # aunque estaría bien generarlos y quitarlos de la plantilla
    # t += "  <ul>\n"
    # for g in unicode_grupos.grupos[pagina]:
    #     t += f'    <li><a href="#{g[2]}">{g[1]}</a></li>\n'
    # t += "  </ul>\n"
    # t += "\n"

    for g in unicode_grupos.grupos[pagina]:
        # ELIMINA LOS SHOW_NO
        g[0] = [valor for valor in g[0] if valor[gendef.SHO] == "SHOW-YES"]
        t += genera_grupo(
            g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8], fuentes, pagina
        )

    return t

def genera_pagina(pagina):
    if pagina == gendef.PAG_SIMBOLOS:
        return genera_grupos(gendef.PAG_SIMBOLOS, ["SS-VST", "SYM"])
    elif pagina == gendef.PAG_EMOJIS:
        return genera_grupos(gendef.PAG_EMOJIS, ["SS-VSE", "TCF-TGH"])
    elif pagina == gendef.PAG_BANDERAS:
        return genera_grupos(gendef.PAG_BANDERAS, ["SS", "TCF-TGH"])
    elif pagina == gendef.PAG_GENEROS:
        return genera_grupos(gendef.PAG_GENEROS, ["SS", "TCF-TGH"])
    elif pagina == gendef.PAG_FITZPATRICK:
        return genera_grupos(gendef.PAG_FITZPATRICK, ["SS", "TCF-TGH"])
    elif pagina == gendef.PAG_PAREJAS:
        return genera_grupos(gendef.PAG_PAREJAS, ["SS", "TCF-TGH"])
    elif pagina == gendef.PAG_PROBLEMAS:
        return genera_grupos(gendef.PAG_PROBLEMAS, ["SS", "TCF-TGH"])


# Puñetitas varias
# * No he tenido en cuenta si hay un carácter simple que no se ve en Windows pero sí está en gendef.TWEmoji
# * Parece que en temoji todo los caracteres simples se llaman solamente con el código, pero si son gendef.VST no se añade
# * Los caracteres 0023, 002A, etc. para que se vean se tiene que escribir con 20E3 al final, así que los he puesto en secuencias,
#   pero se supone que tiene versión texto y emoji, pero en Windows no se ven
# * El carácter 2122 (trade mark) está en TCF, pero si pongo TGH no sale bien, no sé por qué
# * El carácter  25FC no se ve igual si está en párrafo clase .si (sin span), que si tiene un span clase .ss. No lo entiendo.
# * El carácter 25FD y 25 FE son gendef.VST, pero para que enlace al respositorio tengo que poner gendef.VSE Creo que es un error de Twitter

# genera_variantes(variacion, "Secuencias de variación", "variacion")

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
