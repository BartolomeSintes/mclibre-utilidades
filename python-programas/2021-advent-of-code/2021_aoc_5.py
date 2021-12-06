from copy import deepcopy

FICHERO = "2021_aoc_5_input.txt"
# FICHERO = "2021_aoc_5_input_test.txt"


def parte_1():
    print()
    print(f"  PARTE 1")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        # Lee coordenadas de las líneas
        texto = f.readlines()
        lineas = []
        for i in texto:
            if i.rstrip().lstrip().replace(" ", "") != "":
                linea = i.rstrip().lstrip().replace(" ", "").split("->")
                linea = linea[0].split(",") + linea[1].split(",")
                lineas += [linea]

        # Convierte coordenas a números
        for linea in lineas:
            linea[0] = int(linea[0])
            linea[1] = int(linea[1])
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])

        # Calcula máximo y mínimo en x e y
        max_x = max_y = 0
        for linea in lineas:
            if linea[0] > max_x:
                max_x = linea[0]
            if linea[1] > max_y:
                max_y = linea[1]
            if linea[2] > max_x:
                max_x = linea[2]
            if linea[3] > max_y:
                max_y = linea[3]
        print(f"    Tamaño cuadro: {max_x} x {max_y}")

        # Crea lista de puntos
        puntos = []
        for i in range(max_y + 1):
            linea = []
            for j in range(max_x + 1):
                linea += [0]
            puntos += [linea]

        # Marca puntos en la lista
        for y in range(len(lineas)):
            # print(lineas[y])
            if lineas[y][0] == lineas[y][2]:
                minimo = min(lineas[y][1], lineas[y][3])
                maximo = max(lineas[y][1], lineas[y][3])
                for y2 in range(minimo, maximo + 1):
                    # print("x:", lineas[y][0], y2)
                    puntos[y2][lineas[y][0]] += 1
            if lineas[y][1] == lineas[y][3]:
                minimo = min(lineas[y][0], lineas[y][2])
                maximo = max(lineas[y][0], lineas[y][2])
                for x2 in range(minimo, maximo + 1):
                    # print("y:", x2, lineas[y][1])
                    puntos[lineas[y][1]][x2] += 1

        # # Muestra lista de puntos
        # for linea in puntos:
        #     print("    ", end="")
        #     for punto in linea:
        #         print(punto, end=" ")
        #     print()

        # Cuenta dónde hay más de dos puntos
        cuenta = 0
        for y in range(len(puntos)):
            for x in range(len(puntos[y])):
                if puntos[y][x] >= 2:
                    cuenta += 1
        print(f"    Resultado: {cuenta}")


def parte_2():
    print()
    print(f"  PARTE 2")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        # Lee coordenadas de las líneas
        texto = f.readlines()
        lineas = []
        for i in texto:
            if i.rstrip().lstrip().replace(" ", "") != "":
                linea = i.rstrip().lstrip().replace(" ", "").split("->")
                linea = linea[0].split(",") + linea[1].split(",")
                lineas += [linea]

        # Convierte coordenas a números
        for linea in lineas:
            linea[0] = int(linea[0])
            linea[1] = int(linea[1])
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])

        # Calcula máximo y mínimo en x e y
        max_x = max_y = 0
        for linea in lineas:
            if linea[0] > max_x:
                max_x = linea[0]
            if linea[1] > max_y:
                max_y = linea[1]
            if linea[2] > max_x:
                max_x = linea[2]
            if linea[3] > max_y:
                max_y = linea[3]
        print(f"    Tamaño cuadro: {max_x} x {max_y}")

        # Crea lista de puntos
        puntos = []
        for i in range(max_y + 1):
            linea = []
            for j in range(max_x + 1):
                linea += [0]
            puntos += [linea]

        # Marca puntos en la lista
        for y in range(len(lineas)):
            # print(lineas[y])
            if lineas[y][0] == lineas[y][2]:
                minimo = min(lineas[y][1], lineas[y][3])
                maximo = max(lineas[y][1], lineas[y][3])
                for y2 in range(minimo, maximo + 1):
                    # print("x:", lineas[y][0], y2)
                    puntos[y2][lineas[y][0]] += 1
            elif lineas[y][1] == lineas[y][3]:
                minimo = min(lineas[y][0], lineas[y][2])
                maximo = max(lineas[y][0], lineas[y][2])
                for x2 in range(minimo, maximo + 1):
                    # print("y:", x2, lineas[y][1])
                    puntos[lineas[y][1]][x2] += 1
            else:
                if lineas[y][2] > lineas[y][0] and lineas[y][3] > lineas[y][1]:
                    for z in range(lineas[y][2] - lineas[y][0] + 1):
                        puntos[lineas[y][1]+z][lineas[y][0]+z] += 1
                elif lineas[y][2] > lineas[y][0] and lineas[y][3] < lineas[y][1]:
                    for z in range(lineas[y][2] - lineas[y][0] + 1):
                        puntos[lineas[y][1]-z][lineas[y][0]+z] += 1
                elif lineas[y][2] < lineas[y][0] and lineas[y][3] > lineas[y][1]:
                    for z in range(lineas[y][0] - lineas[y][2] + 1):
                        puntos[lineas[y][1]+z][lineas[y][0]-z] += 1
                elif lineas[y][2] < lineas[y][0] and lineas[y][3] < lineas[y][1]:
                    for z in range(lineas[y][0] - lineas[y][2] + 1):
                        puntos[lineas[y][1]-z][lineas[y][0]-z] += 1

        # Muestra lista de puntos
        # for linea in puntos:
        #     print("    ", end="")
        #     for punto in linea:
        #         if punto == 0:
        #             print(".", end=" ")
        #         else:
        #             print(punto, end=" ")
        #     print()

        # Cuenta dónde hay más de dos puntos
        cuenta = 0
        for y in range(len(puntos)):
            for x in range(len(puntos[y])):
                if puntos[y][x] >= 2:
                    cuenta += 1
        print(f"    Resultado: {cuenta}")


def main():
    print("2021 ADVENT OF CODE DAY 5")
    parte_1()
    parte_2()
    print()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
