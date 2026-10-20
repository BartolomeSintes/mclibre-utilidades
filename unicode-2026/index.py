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
        print(" 11. Crea manual_1.py para Twemoji")
        print(" 12. Crea manual_1.py para Noto Emoji")
        print(" 13. Crea manual_1.py para Twemoji Jdecked")
        print(" 21. Crea manual_2.py (comentarios disponibilidad)")
        print(" 22. Genera páginas")
        print()
        eleccion = int(input("Elija una opción: "))
        print()
        if eleccion == 1:
            import uc_1_importa_unicode as uc_1

            uc_1.importa_unicode()
        elif eleccion == 2:
            import uc_2_importa_full_emoji_list as uc_2

            uc_2.main()
        elif eleccion == 3:
            import uc_3_importa_full_emoji_modifier_sequences as uc_3

            uc_3.main()
        elif eleccion == 4:
            import uc_4_fusiona_listas_unicode as uc_4

            uc_4.fusiona_listas_unicode()
        elif eleccion == 11:
            import uc_11_grupos_manual_1_twemoji as uc_11

            uc_11.main()
        elif eleccion == 12:
            import uc_12_grupos_manual_1_noto as uc_12

            uc_12.main()
        elif eleccion == 13:
            import uc_13_grupos_manual_twemoji_jdecked as uc_13

            uc_13.main()
        elif eleccion == 21:
            import uc_21_util as uc_21

            uc_21.main()
        elif eleccion == 22:
            import uc_22_generador as uc_22

            uc_22.main()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
