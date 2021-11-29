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

ORIGEN = pathlib.Path("sitio-plantilla")
DESTINO = pathlib.Path("sitio")


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


def genera_pagina_caracteres(pagina):
    if pagina == ucdef.PAG_SIMBOLOS:
        t = ""
        for grupo in ucdef.uc_tablas_caracteres[0]:
            caracteres = []
            for c in imp.derived_name:
                if c[3] == grupo[1] and c[2] != "emoji":
                    caracteres += [c]
            caracteres.sort()
            contador = len(caracteres)
            print(grupo[1], contador)
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
                    if c[2] == "texto" or c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} "
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;{c[0]};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "emoji-texto":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} U+FE0E"
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0e;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amps;#xfe0e;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;{c[0]};&amp;#65038;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
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
                        t += f"          Dec:&nbsp;<strong>&amp;{c[0]};</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        t += "      </div>\n"
                        t += "\n"
                    elif c[2] == "texto-emoji":
                        t += '      <div class="u">\n'
                        t += '        <p class="uc">'
                        t += f"U+{int(c[0], 16):X} U+FE0F"
                        t += "</p>\n"
                        t += f'        <p class="si"> &#x{int(c[0], 16):X};&#xfe0f;</p>\n'
                        t += '        <p class="en">\n'
                        t += f"          Hex:&nbsp;<strong>&amp;#x{int(c[0], 16):x};&amps;#xfe0f;</strong><br>\n"
                        t += f"          Dec:&nbsp;<strong>&amp;{c[0]};&amp;#65039;</strong>\n"
                        t += "        </p>\n"
                        t += f'        <p class="no">{c[1]}</p>\n'
                        t += "      </div>\n"
                        t += "\n"
                t += "    </div>\n"
                t += "  </section>\n"
        t += "\n"
    return t


def genera_pagina_secuencias(pagina, grupos):
    t = ""
    for grupo in grupos:
        caracteres = []
        for c in imp3.manual_1:
            for cgrupo in c[1]:
                if cgrupo == grupo[0]:
                    caracteres += [c]
        caracteres.sort()
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
                t += f"&amp;{cn};"
                t += f"</strong>\n"
                t += "        </p>\n"
                c_nombre = ""
                for i in imp2.fusionados_2:
                    # print(i[0], "xxx", c[0])
                    if i[0] == c[0]:
                        c_nombre = i[2][3]
                t += f'        <p class="no">{c_nombre}</p>\n'
                t += "      </div>\n"
                t += "\n"
        t += "    </div>\n"
        t += "  </section>\n"
    t += "\n"
    return t


def main():
    print("GENERADOR DE PÁGINAS SIMBOLOS UNICODE PARA APUNTES HTMLS/CSS")

    # Comprueba que DESTINO no existe y lo borra si existe
    p = pathlib.Path(DESTINO)
    if p.exists():
        print()
        print(f"El directorio de destino /{DESTINO} ya existe.")
        print("El directorio de destino existente se borrará completamente.")
        respuesta = input("Confirme que desea crearlo de nuevo (S): ")
        if respuesta != "S":
            print("El sitio no se ha creado.")
            sys.exit(0)
        else:
            shutil.rmtree(p)

    directorio = DESTINO
    p = pathlib.Path(directorio)
    if not p.exists():
        print(f"  {directorio}")
        p.mkdir(parents=True, exist_ok=True)

    # Crea páginas
    print()
    print("Creando páginas")
    print()

    paginas = [
        [ucdef.PAG_SIMBOLOS, ucdef.FICHERO_SITIO_SIMBOLOS],
        [ucdef.PAG_EMOJIS, ucdef.FICHERO_SITIO_EMOJIS],
        [ucdef.PAG_BANDERAS, ucdef.FICHERO_SITIO_BANDERAS],
        [ucdef.PAG_GENEROS, ucdef.FICHERO_SITIO_GENEROS],
        [ucdef.PAG_FITZPATRICK, ucdef.FICHERO_SITIO_FITZPATRICK],
        [ucdef.PAG_PAREJAS, ucdef.FICHERO_SITIO_PAREJAS],
        # [ucdef.PAG_PROBLEMAS, ucdef.FICHERO_SITIO_PROBLEMAS],
    ]

    for pagina in paginas:
        fichero_origen = ORIGEN / pagina[1]
        fichero_destino = DESTINO / pagina[1]
        print(f"Creando {fichero_destino}")
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
        print()

        # webbrowser.open(fichero_destino)


if __name__ == "__main__":
    main()
