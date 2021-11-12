import importa_unicode

print("GENERADOR DE PÁGINAS PARA APUTNES HTML/CSS SOBRE EMOJIS")
print()
eleccion = -1
while eleccion != 0:
    print("Acciones disponibles")
    print("  0. Salir")
    print("  1. Importar ficheros unicode")
    print()
    eleccion = int(input("Elija una opción: "))
    print()
    if eleccion == 1:
        importa_unicode.importa_unicode()
print("Programa terminado")
print()
