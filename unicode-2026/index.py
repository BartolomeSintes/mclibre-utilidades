import uc_1_importa_unicode as uc_1
import uc_2_importa_full_emoji_list as uc_2
import uc_3_importa_full_emoji_modifier_sequences as uc_3
import uc_4_fusiona_listas_unicode as uc_4


def main():
    print("GENERADOR DE PÁGINAS PARA APUNTES HTML/CSS SOBRE EMOJIS")
    print()
    eleccion = -1
    while eleccion != 0:
        print("Acciones disponibles")
        print("  0. Salir")
        print("  1. Importar ficheros unicode txt")
        print("  2. Importar fichero unicode full emoji list html")
        print("  3. Importar fichero unicode full emoji modifier sequences html")
        print("  4. Fusionar listas unicode")
        print()
        eleccion = int(input("Elija una opción: "))
        print()
        if eleccion == 1:
            uc_1.importa_unicode()
        elif eleccion == 2:
            uc_2.main()
        elif eleccion == 3:
            uc_3.main()
        elif eleccion == 4:
            uc_4.fusiona_listas_unicode()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
