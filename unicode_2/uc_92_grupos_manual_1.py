# Este programa crea una página web con los grupos de emojis que hay definidos en manual_1
# Lo he hecho para mejorar uc_91_crea_manual_1 y que asigne automáticamente la mayor parte posible de los grupos

import os
import pathlib
import ucdef
import sys
from u14_ficheros_3_fusionados import unicode_txt_fusionados_2 as imp


def grupo(elemento):
    if len(elemento[0]) == 1:
        for grupo in ucdef.uc_tablas_caracteres[0]:
            if elemento[0][0] >= grupo[3] and elemento[0][0] <= grupo[4]:
                return grupo[1]
        if elemento[3][0][0] == "Emoji_Component":
            return "gr-componentes"
    elif len(elemento[0]) == 2:
        # XXX FZ
        if elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF":
            return "gr-colores-piel-1"
        elif elemento[0][0] >= "1F1E6" and elemento[0][0] <= "1F1FF" and elemento[0][1] >= "1F1E6" and elemento[0][1] <= "1F1FF":
            return "gr-banderas-paises"
    elif len(elemento[0]) == 3:
        # M/W ZWJ XXX
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D":
            return "gr-genero-1"
        # XXX ZWJ M/F
        elif elemento[0][1] == "200D" and (elemento[0][2] == "2640" or elemento[0][2] == "2642") :
            return "gr-genero-1"
    elif len(elemento[0]) == 4:
        # M/W ZWJ XXX VS16
        if (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and elemento[0][1] == "200D" and elemento[0][3] == "FE0F":
            return "gr-genero-2"
        # ZWJ M/F XXX VS16
        elif elemento[0][1] == "200D" and (elemento[0][2] == "2640" or elemento[0][2] == "2642") and elemento[0][3] == "FE0F":
            return "gr-genero-3"
        # M/W FZ ZWJ XXX
        elif (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D":
            return "gr-colores-piel-2"
        # XXX FZ ZWJ M/F
        elif (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642") :
            return "gr-colores-piel-5"
    elif len(elemento[0]) == 5:
        # ZWJ M/F XXX VS16
        if elemento[0][1] == "FE0F" and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642") and elemento[0][4] == "FE0F":
            return "gr-genero-4"
        # M/W FZ ZWJ XXX XXX
        elif (elemento[0][0] == "1F468" or elemento[0][0] == "1F469") and (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D":
            return "gr-colores-piel-3"
        # XXX FZ ZWJ M/F XXX
        elif (elemento[0][1] == "1F3FB" or elemento[0][1] == "1F3FC" or elemento[0][1] == "1F3FD" or elemento[0][1] == "1F3FE" or elemento[0][1] == "1F3FF") and elemento[0][2] == "200D" and (elemento[0][3] == "2640" or elemento[0][3] == "2642"):
            return "gr-colores-piel-4"
    return ""


def crea_manual_1():
    global manual_1
    manual_1 = []
    for i in imp.fusionados_2:
        manual_1 += [[i[0], grupo(i)]]
    cuenta_en_grupos = 0
    for i in manual_1:
        if i[1] != "":
            cuenta_en_grupos += 1
    print(f"  Hay {len(imp.fusionados_2)} elementos")
    print(f"  Ya clasificados en grupos: {cuenta_en_grupos}")
    print(f"  pendientes de clasificar: {len(imp.fusionados_2) - cuenta_en_grupos}")


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
            t += f'    "{i[1]}",\n'
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


def selecciona_grupo(nombre_grupo):
    # extrae y elimina de manual_1 los emojis de un grupo
    global manual_1
    grupo = []
    for i in range(len(manual_1) - 1, -1, -1):
        if manual_1[i][1] == nombre_grupo:
            grupo += [manual_1[i]]
            del manual_1[i]
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
        for grupo in ucdef.uc_tablas_caracteres[0]:
            extraido = selecciona_grupo(grupo[1])
        t += "<h2>Restos 1</h2>\n"
        t += f"  <p>\n"
        for i in manual_1:
            if len(i[0]) == 1:
                t += f"    {genera_entidad_numerica(i[0])}\n"
                t += f"    {i[0]}<br>\n"
        t += "  </p>\n"
        t += "<h2>Restos secuencias</h2>\n"
        t += f"  <p>\n"
        for i in manual_1:
            if len(i[0]) > 1:
                t += f"    {genera_entidad_numerica(i[0])}\n"
                t += f"    {i[0]}<br>\n"
        t += "  </p>\n"
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
