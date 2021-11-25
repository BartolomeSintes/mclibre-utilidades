import ucdef
import os
import pathlib
import sys
from u14_ficheros_3_fusionados import unicode_txt_fusionados_1 as imp

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


def ordena_1():
    # Ordena la lista fusioinados

    for i in range(len(imp.fusionados)):
        if len(imp.fusionados[i][1]) > 0 and len(imp.fusionados[i][2]) > 0:
            print(imp.fusionados[i][1])
            print(imp.fusionados[i][2])
            if imp.fusionados[i][1][3] != imp.fusionados[i][2][1]:
                print("Error")



def exporta_listas():
    destino = ucdef.FICHERO_ORDENADO
    print()
    print(f"  CREANDO {destino}")

    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda fusionados
        t += "unicode = [\n"
        for i in fusionados:
            t += f"  [{i[0]},\n"
            t += f"   {i[1]},\n"
            t += f"   {i[2]},\n"
            t += f"   {i[3]},\n"
            t += f"   {i[4]},\n"
            t += f"   {i[5]},\n"
            t += f"   {i[6]},\n"
            t += f"  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)


# def organiza_listas_unicode():
def main():
    print("2. ORGANIZANDO LISTA UNICODE")
    # Comprueba si el fichero de destino existe y pide confirmación para sobreescribirlo
    p = pathlib.Path(ucdef.FICHERO_ORDENADO)
    respuesta = "N"
    if p.exists():
        print(f"  El fichero de destino {ucdef.FICHERO_ORDENADO} ya existe.")
        respuesta = input("  Confirme que desea crearlo de nuevo (S): ")
        if respuesta == "S":
            os.remove(p)
        else:
            print("  El fichero no se ha creado.")
    if not p.exists():
        ordena_1()
        # exporta_listas()
    print()
    print("  Programa terminado.")
    print()


if __name__ == "__main__":
    main()
