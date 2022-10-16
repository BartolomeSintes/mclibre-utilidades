# Este programa crea un lista a partir de fusionados_2, dejando únicamente el campo [0],
# es decir, el código o secuencia Unicode

import os
import pathlib
import ucdef
import sys
from ficheros_3_fusionados import unicode_txt_fusionados_2 as imp

def grupo(codigo):
    for grupo in ucdef.uc_tablas_caracteres[0]:
        if int(codigo, 16) >= int(grupo[3], 16) and int(codigo, 16) <= int(grupo[4], 16):
            return grupo[1]
    return ""


def exporta_lista():
    destino = ucdef.FICHERO_MANUAL_1
    print(f"CREANDO {destino}")
    print(f"  Hay {len(imp.fusionados_2)} elementos")
    with open(destino, "w", encoding="utf-8", newline="\n") as fichero:
        t = ""
        # Guarda Full emoji list
        t += "manual_1 = [\n"
        for i in imp.fusionados_2:
            t += "  [\n"
            t += f"    {i[0]},\n"
            if len(i[0]) == 1:
                t += f"    \"{grupo(i[0][0])}\",\n"
            else:
                    t += f"    \"\",\n"
            t += "  ],\n"
        t += "]\n"
        t += "\n"
        fichero.write(t)

    print("Programa terminado.")


def main():

    # for grupo in ucdef.uc_tablas_caracteres[0]:
    #     print(grupo)
    #     print()
    # print("adios")
    # sys.exit()
    print("91. CREANDO FICHERO MANUAL VACÍO A PARTIR FUSIONADOS_2")
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


if __name__ == "__main__":
    main()
