import pathlib, re

# para ejecutar esta aplicación,
# escriba en ORIGEN la raíz de los ficheros a analizar
# y ejecute la orden py diccionario.py

ORIGEN = "D:\\Barto\\logs\\logs.mclibre.org\\2019"

PROFES = [
    "amaliaalbero",
    "antoniojosefernandez",
    "cristinasanfrancisco",
    "daniel_tomas"
]
LIMPIA = [
    "/ HTTP",
    "/primaria",
    ".html",
    ".xhtml",
    ".pdf",
    ".php",
    ".xml",
    ".xsl",
    ".py",
    ".txt",
    ".odt",
    ".odp",
    ".ods",
    ".sxi",
    ".swf",
    ".mp3",
    ".mp4",
    ".exe",
    ".zip",
    ".7z",
    ".gz",
    ".tgz"
]
IMG = [".jpg", ".png", ".svg", ".gif", ".webp", ".ico", ".cur"]
OTROS = [".css", ".js", ".woff", ".otf", ".ttf", ".po", ".eot"]

BUSCA = [
    "solo-linux-01-es-201902.pdf",
    "solo-linux-02-es-201903.pdf",
    "solo-linux-03-es-201904.pdf",
    "solo-linux-04-es-201905.pdf",
    "solo-linux-05-es-201906.pdf",
    "solo-linux-06-es-201907.pdf",
    "solo-linux-07-es-201908.pdf",
]


def limpia_logs():
    print("Limpia logs")
    # Se queda con las líneas 200 GET que contienen las cadenas que hay en LIMPIA[]
    for source_file in pathlib.Path(ORIGEN).rglob(f"**/transfer*"):
        print(source_file)
        file_profes = str(source_file) + ".profes"
        file_clean = str(source_file) + ".clean"
        file_img = str(source_file) + ".img"
        file_otros = str(source_file) + ".otros"
        file_ok = str(source_file) + ".ok"
        file_dirty = str(source_file) + ".dirty"

        with open(source_file, "r", encoding="utf-8") as source, open(
            file_profes, "w", encoding="utf-8"
        ) as profes, open(file_clean, "w", encoding="utf-8") as clean, open(
            file_img, "w", encoding="utf-8"
        ) as img, open(
            file_otros, "w", encoding="utf-8"
        ) as otros, open(
            file_ok, "w", encoding="utf-8"
        ) as ok, open(
            file_dirty, "w", encoding="utf-8"
        ) as dirty:
            texto = source.readline()
            while texto:
                texto = source.readline()
                # print(texto)
                limpio = False
                for i in PROFES:
                    if i in texto and " 200 " in texto and "GET" in texto:
                        print(texto, end="", file=profes)
                        limpio = True
                if not (limpio):
                    for i in LIMPIA:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=clean)
                            limpio = True
                if not (limpio):
                    for i in IMG:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=img)
                            limpio = True
                if not (limpio):
                    for i in OTROS:
                        if i in texto and " 200 " in texto and "GET" in texto:
                            print(texto, end="", file=otros)
                            limpio = True
                if not (limpio):
                    if " 200 " in texto and "GET" in texto:
                        print(texto, end="", file=ok)
                        limpio = True
                if not (limpio):
                    print(texto, end="", file=dirty)


def analiza_logs():
    print("Analiza")

    contadores = []
    for i in range(len(BUSCA)):
        contadores += [0]

    for source_file in pathlib.Path(ORIGEN).rglob(f"**/transfer*.clean"):
        print(source_file)
        with open(source_file, "r", encoding="utf-8") as file:
            texto = file.readline()
            while texto:
                texto = file.readline()
                for i in range(len(BUSCA)):
                    if BUSCA[i] in texto:
                        contadores[i] += 1

    for i in range(len(BUSCA)):
        print(f"{BUSCA[i]}: {contadores[i]}")


def main():
    # limpia_logs()
    analiza_logs()



if __name__ == "__main__":
    main()
