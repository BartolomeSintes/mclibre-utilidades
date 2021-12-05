from copy import deepcopy

FICHERO = "2021_aoc_4_input.txt"
# FICHERO = "2021_aoc_4_input_test.txt"


def parte_1():
    print()
    print(f"  PARTE 1")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        # Lee números del bingo
        numeros = f.readline().rstrip().split(",")

        # Lee cartones
        texto = f.readlines()
        n_cartones = (len(texto) - 1) // 6
        cartones = []
        for i in range(n_cartones):
            carton = []
            for j in range(1, 6):
                carton += [texto[6 * i + j].rstrip().lstrip().replace("  ", " ").split(" ")]
            cartones += [carton]
        cartones_2 = deepcopy(cartones)

        # Tacha números de los cartones y comprueba si hay una fila vacía
        hay_bingo = numero_bingo = -1
        i = 0
        while hay_bingo == -1 and i < len(numeros):
            for carton in cartones:
                for linea in carton:
                    for j in range(len(linea) - 1, -1, -1):
                        if linea[j] == numeros[i]:
                            linea[j] = ""
            for n_cart in range(len(cartones)):
                for j in range(len(cartones[n_cart])):
                    if cartones[n_cart][j][0] == cartones[n_cart][j][1] == cartones[n_cart][j][2] == cartones[n_cart][j][3] == cartones[n_cart][j][4] == "":
                        hay_bingo = n_cart
                        numero_bingo = int(numeros[i])
                        print(f"    ¡BINGO! fila en cartón {hay_bingo} con el número {numero_bingo}")
                        print(f"    {cartones[hay_bingo]}")
            for n_cart in range(len(cartones)):
                for j in range(len(cartones[n_cart])):
                    if cartones[n_cart][0][j] == cartones[n_cart][1][j] == cartones[n_cart][2][j] == cartones[n_cart][3][j] == cartones[n_cart][4][j] == "":
                        hay_bingo = n_cart
                        numero_bingo = int(numeros[i])
                        print(f"    ¡BINGO! columna en cartón {hay_bingo} con el número {numero_bingo}")
                        print(f"    {cartones[hay_bingo]}")
            i += 1

        # Muestra el resultado
        if not hay_bingo:
            print("    No se ha cantado bingo")
        else:
            print(f"    Cartón de bingo: número {hay_bingo}")
            suma_carton_vacio = 0
            for linea in cartones[hay_bingo]:
                for numero in linea:
                    if numero != "":
                        suma_carton_vacio += int(numero)
            print(f"    Suma sin tachar: {suma_carton_vacio} - Número bingo: {numero_bingo}")
            print(f"    Respuesta: {suma_carton_vacio * numero_bingo}")

def parte_2():
    print()
    print(f"  PARTE 2")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        # Lee números del bingo
        numeros = f.readline().rstrip().split(",")

        # Lee cartones
        texto = f.readlines()
        n_cartones = (len(texto) - 1) // 6
        cartones = []
        for i in range(n_cartones):
            carton = []
            for j in range(1, 6):
                carton += [texto[6 * i + j].rstrip().lstrip().replace("  ", " ").split(" ")]
            cartones += [carton]
        cartones_2 = deepcopy(cartones)

        # Tacha números de los cartones y comprueba si hay una fila vacía
        numero_bingo = -1
        i = 0
        termina = False
        while not termina and i < len(numeros):
            hay_bingo = []
            termina = False
            for carton in cartones:
                for linea in carton:
                    for j in range(len(linea) - 1, -1, -1):
                        if linea[j] == numeros[i]:
                            linea[j] = ""
            for n_cart in range(len(cartones)):
                for j in range(len(cartones[n_cart])):
                    if cartones[n_cart][j][0] == cartones[n_cart][j][1] == cartones[n_cart][j][2] == cartones[n_cart][j][3] == cartones[n_cart][j][4] == "":
                        hay_bingo += [n_cart]
            for n_cart in range(len(cartones)):
                for j in range(len(cartones[n_cart])):
                    if cartones[n_cart][0][j] == cartones[n_cart][1][j] == cartones[n_cart][2][j] == cartones[n_cart][3][j] == cartones[n_cart][4][j] == "":
                        if n_cart not in hay_bingo:
                            hay_bingo += [n_cart]
            hay_bingo.sort()
            if hay_bingo != []:
                numero_bingo = int(numeros[i])
                print(f"    ¡BINGO! cartones rellenados: {numero_bingo} {hay_bingo}")
                if len(cartones) > 1:
                    for j in range(len(hay_bingo) -1, -1, -1):
                        del cartones[hay_bingo[j]]
                else:
                    termina = True
            i += 1

        # Muestra el resultado
        if len(cartones) != 1:
            print("    Problema, no queda solo un cartón")
        else:
            print(f"    Último número: {numero_bingo}")
            suma = 0
            for i in cartones[0]:
                for j in i:
                    if j != "":
                        suma += int(j)
            print(f"    Suma restantes: {suma}")
            print(f"    Resultado: {numero_bingo * suma}")


def main():
    print("2021 ADVENT OF CODE DAY 4")
    parte_1()
    parte_2()
    print()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
