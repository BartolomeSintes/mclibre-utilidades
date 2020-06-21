import pathlib
from string import Template
import shutil
import sys
import webbrowser
import gendef
import genfun

ORIGEN = pathlib.Path("sitio-plantilla")
DESTINO = pathlib.Path("sitio")


def main():
    print("GENERADOR DE PÁGINAS SIMBOLOS UNICODE PARA APUTNES HTMLS/CSS")

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
        [gendef.PAG_SIMBOLOS, gendef.FICHERO_SIMBOLOS],
        [gendef.PAG_EMOJIS, gendef.FICHERO_EMOJIS]
    ]

    for pagina in paginas:
        fichero_origen = ORIGEN / pagina[1]
        fichero_destino = DESTINO / pagina[1]
        print(f"Creando {fichero_destino}")
        with open(fichero_origen, "r", encoding="utf-8") as fichero:
            texto = Template(fichero.read())

        resultado = texto.safe_substitute(contenido=genfun.genera_pagina(pagina[0]))

        with open(fichero_destino, "w", encoding="utf-8", newline="\n") as fichero:
            fichero.write(resultado)
        print()

        webbrowser.open(fichero_destino)


if __name__ == "__main__":
    main()
