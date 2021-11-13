import uc_1_importa_unicode as uc_1
import uc_2_fusiona_listas_unicode as uc_2


def main():
    print("GENERADOR DE PÁGINAS PARA APUTNES HTML/CSS SOBRE EMOJIS")
    print()
    eleccion = -1
    while eleccion != 0:
        print("Acciones disponibles")
        print("  0. Salir")
        print("  1. Importar ficheros unicode")
        print("  2. Fusionar listas unicode")
        print()
        eleccion = int(input("Elija una opción: "))
        print()
        if eleccion == 1:
            uc_1.importa_unicode()
        elif eleccion == 2:
            uc_2.fusiona_listas_unicode()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
