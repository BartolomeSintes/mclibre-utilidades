import pathlib, html.parser, re, codecs

RAICES = ["C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\htmlcss"]

EXTENSIONES = ["html", "css", "svg", "php", "py", "js", "md"]


def estadisticas(origen):
    print(f"Directorio raíz: {origen}")
    total = 0
    for _ in pathlib.Path(origen).glob(f"**/*.*"):
        total += 1
    print(f"Hay {total} ficheros en total.")

    total_analizadas = 0
    for extension in EXTENSIONES:
        contador = 0
        for _ in pathlib.Path(origen).glob(f"**/*.{extension}"):
            contador += 1
        total_analizadas += contador
    print(f"Se analizarán {total_analizadas} ficheros de las extensiones siguientes")

    for extension in EXTENSIONES:
        contador = 0
        for _ in pathlib.Path(origen).glob(f"**/*.{extension}"):
            contador += 1
        if contador:
            print(f"{extension}: {contador} - ", end="")
    print()
    print()


def main():

    print("ELIMINAR UTF-8 BOM DE LOS FICHEROS")
    print("Se recomienda hacer una copia de seguridad antes de continuar.")
    if input("Pulse S para continuar: ") == "S":
        for origen in RAICES:
            print()
            estadisticas(origen)

            for extension in EXTENSIONES:
                contador = 0
                for filename in pathlib.Path(origen).rglob(f"**/*.{extension}"):
                    with open(filename, "rb") as fichero:
                        texto = fichero.read()
                        # detecta BOM
                        if texto.startswith(codecs.BOM_UTF8):
                            contador += 1
                            print()
                            print(filename)
                            texto = texto.replace(codecs.BOM_UTF8, b"")
                            with open(filename, "wb") as fichero2:
                                fichero2.write(texto)
                print(f"{extension} : BOM eliminado en {contador} ficheros.")
    print()
    print("Trabajo terminado.")


if __name__ == "__main__":
    main()
