import pathlib, re

ORIGEN_PHP = "C:\\Users\\BLJ\\Documents\\_MCLibre.org\\Actual\\consultar\\php"

ORIGEN = ORIGEN_PHP


EXTENSIONES = ["html", "php"]

def main():
    print("Análisis")

    patrones = [r"<link ", r"<link rel=\\\"st", "<link rel=\"st", r"<link [^r]"]

    patrones = [r'css" title="mcli', r'css" title="Col', r'css" title="[^mC]']

    patrones = [r'css\\\" title=\\\"mcli', r'css\\\" title=\\\"Col', r'css\\\" title=\\\"[^mC]']

    patrones = [r'<br />', r"<br[^ ]"]
    patrones = [r'<meta']
    patrones = [r'title="mclibre" />', r'title=\\\"mclibre\\\" />', r'title="Color" />', r'title=\\\"Color\\\" />', ]
    patrones = [r'css" />', r'css\\\" />', r'highlight-php\.css" />', r'highlight-php\.css\\\" />', ]
    patrones = [r'[^ s]/>', r'[^ s]/&gt;']
    # Estas dos búsquedas no me coinciden
    patrones = [r"<link", r'<link rel="icon', r'<link rel="sty', r'<link rel=\\\"icon', r'<link rel=\\\"sty', ]
    patrones = [r'\.css" title="', r'\.css\\\" title=\\\"', r'highlight-php\.css" />', r'\.css"[^ /]', r'\.css\\\"[^ /]']


    muestra_filename = [False, False, False, False, False, False]
    for busca in range(len(patrones)):
        print()
        print(f"patrón: {patrones[busca]}")
        contador_ficheros_total = 0
        contador_encontrados_total = 0
        for extension in EXTENSIONES:
            contador_ficheros = 0
            contador_encontrados = 0
            for filename in pathlib.Path(ORIGEN).rglob(f"**/*.{extension}"):
                # print()
                # print(f"{contador}: {filename}")
                with open(filename, "r", encoding="utf-8") as fichero:
                    texto = fichero.read()
                    # busca
                    x = len(re.findall(patrones[busca], texto))
                    if x > 0:
                        contador_encontrados += x
                        contador_ficheros += 1
                        if muestra_filename[busca]:
                            print(filename)
            print(f"    {extension}: {contador_encontrados} en {contador_ficheros} ficheros")
            contador_ficheros_total += contador_ficheros
            contador_encontrados_total += contador_encontrados
        print(f"  Total {contador_encontrados_total} en {contador_ficheros_total} ficheros")

if __name__ == "__main__":
    main()
