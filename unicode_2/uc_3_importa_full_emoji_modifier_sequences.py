# Este programa importa el ficheros html
# - Full Emoji Modifier Sequences, v14.0.html

import ucdef
import sys

full_emoji_modifier_sequences = []


def busca(aguja, pajar, posicion):
    encontrado = False
    n = len(pajar)
    i = 0
    # print("probando", lista[i][0], codigos)
    while not encontrado and i < n:
        # print(lista[i][0], codigos)
        if pajar[i][posicion] == aguja:
            encontrado = True
        i += 1
        # input()
    if encontrado:
        return i - 1
    else:
        return -1


def importa_fichero_full_emoji_modifier_sequences():
    global full_emoji_modifier_sequences
    print(f"TRATANDO {ucdef.FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST}")
    print(f"  importando ...")
    importado = []
    with open(
        ucdef.FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST,
        mode="r",
        encoding="utf-8",
    ) as f:
        for line in f:
            importado += [line]

        # Borro todo lo que hay antes de la tabla
        localiza = 0
        while importado[localiza][:6] != "<table":
            localiza += 1
        del importado[:localiza]

        # Borro todo lo que hay después de la tabla
        localiza = 0
        while importado[localiza][:16] != "</tbody></table>":
            localiza += 1
        del importado[localiza + 1 :]

        # Resulta que hay algunas casillas con el nombre del emoji que están pegadas a la casilla anterior, no en una línea separada, así que primero las tengo que dividir
        for i in range(len(importado) - 1, -1, -1):
            corta = importado[i].find('</td><td class="name">')
            if corta != -1:
                importado[i + 1 : i + 1] = [importado[i][: corta + 5]]
                importado[i + 2 : i + 2] = [importado[i][corta + 5 :]]

        # Borro todas las líneas que no me interesan
        for i in range(len(importado) - 1, -1, -1):
            if importado[i][:19] == '<th class="cchars">':
                del importado[i]
            elif importado[i][:23] == '<tr><th class="rchars">':
                del importado[i]
            elif importado[i][:19] == '<th class="rchars">':
                del importado[i]
            elif importado[i][:20] == '<th><a target="text"':
                del importado[i]
            elif importado[i][:20] == '<td class="andr alt"':
                del importado[i]
            elif importado[i][:21] == '<td class="andr miss"':
                del importado[i]
            elif importado[i][:25] == '<td class="andr alt miss"':
                del importado[i]
            elif importado[i][:16] == '<td class="andr"':
                del importado[i]
            elif importado[i][:20] == '<th class="cchars">':
                del importado[i]

        # elemento_names = []
        # Borro los enlaces
        for i in range(len(importado) - 1, -1, -1):
            # inicio_codigo = importado[i].find('"code"')
            # if inicio_codigo != -1:
            #     inicio_name = importado[i].find('name="')
            #     if inicio_name != -1:
            #         fin_name = importado[i][inicio_name + 6 :].find('"')
            #         elemento_names +=[ [i, importado[i][inicio_name + 6 : inicio_name + 6 + fin_name]] ]
            corta1 = importado[i].find("<a")
            corta2 = importado[i][corta1:].find(">")
            if corta1 != -1:
                importado[i] = (
                    importado[i][:corta1] + importado[i][corta1 + corta2 + 1 :]
                )
            corta = importado[i].find("</a>")
            if corta != -1:
                importado[i] = importado[i][:corta] + importado[i][corta + 4 :]

        # Borro el carácter ⊛ que hay al principio del nombre de 37 emojis
        for i in range(len(importado) - 1, -1, -1):
            corta = importado[i].find("⊛ ")
            if corta != -1:
                importado[i] = importado[i][:corta] + importado[i][corta + 2 :]

        # for i in range(10):
        #     print(importado[i])
        # print("  Líneas del fichero: ", len(importado))

        # Proceso el resultado
        grupo = ""
        subgrupo = ""
        elemento = []
        for i in range(len(importado)):
            inicio_grupo = importado[i].find('class="bighead"')
            if inicio_grupo != -1:
                fin_grupo = importado[i][inicio_grupo + 16 :].find("</th>")
                grupo = importado[i][inicio_grupo + 16 : inicio_grupo + 16 + fin_grupo]
            inicio_subgrupo = importado[i].find('class="mediumhead"')
            if inicio_subgrupo != -1:
                fin_subgrupo = importado[i][inicio_subgrupo + 19 :].find("</th>")
                subgrupo = importado[i][
                    inicio_subgrupo + 19 : inicio_subgrupo + 19 + fin_subgrupo
                ]
            inicio_contador = importado[i].find('"rchars"')
            if inicio_contador != -1:
                fin_contador = importado[i][inicio_contador + 9 :].find("</td>")
                elemento += [
                    importado[i][
                        inicio_contador + 9 : inicio_contador + 9 + fin_contador
                    ],
                    grupo,
                    subgrupo,
                ]
            inicio_codigo = importado[i].find('"code"')
            if inicio_codigo != -1:
                fin_codigo = importado[i][inicio_codigo + 7 :].find("</td>")
                elemento += [
                    importado[i][inicio_codigo + 7 : inicio_codigo + 7 + fin_codigo]
                ]
                # falta añadir atributo name que igual me sirve para twemoji
                # pero es más difícil de lo que parece porque el name está en un enlace y los borro antes
                # he probado a hacerlo y no funciona, así que no pierdo más tiempo
                # posicion = busca(i, elemento_names, 0)
                # if posicion != -1:
                #     print(posicion)
                #     elemento += [elemento_names[posicion][1]]
                # else:
                #     elemento += ""

            inicio_caracter = importado[i].find('"chars"')
            if inicio_caracter != -1:
                fin_caracter = importado[i][inicio_caracter + 8 :].find("</td>")
                elemento += [
                    importado[i][
                        inicio_caracter + 8 : inicio_caracter + 8 + fin_caracter
                    ]
                ]
            inicio_nombre = importado[i].find('"name"')
            if inicio_nombre != -1:
                fin_nombre = importado[i][inicio_nombre + 7 :].find("</td>")
                elemento += [
                    importado[i][inicio_nombre + 7 : inicio_nombre + 7 + fin_nombre]
                ]

                full_emoji_modifier_sequences += [elemento]
                elemento = []
        # Divido la secuencia en una lista de caracteres
        for i in range(len(full_emoji_modifier_sequences)):
            es_secuencia = full_emoji_modifier_sequences[i][3].find(" ")
            if es_secuencia != -1:
                tmp = full_emoji_modifier_sequences[i][3].split(" ")
                for j in range(len(tmp)):
                    tmp[j] = tmp[j][2:]
                full_emoji_modifier_sequences[i][3] = tmp
            else:
                full_emoji_modifier_sequences[i][3] = [
                    full_emoji_modifier_sequences[i][3][2:]
                ]


def exporta_listas():
    global full_emoji_modifier_sequences
    destino = ucdef.FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST_LISTA
    print(f"CREANDO {destino}")
    print(f"  Hay {len(full_emoji_modifier_sequences)} emojis")
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda Full emoji list
        t += "full_emoji_modifier_sequences = [\n"
        for i in full_emoji_modifier_sequences:
            t += f"  {i},\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)

    print("Programa terminado.")


def main():
    importa_fichero_full_emoji_modifier_sequences()
    exporta_listas()


if __name__ == "__main__":
    main()
