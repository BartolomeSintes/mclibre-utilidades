FICHERO = "2021_aoc_2_input.txt"
# FICHERO = "2021_aoc_2_input_test.txt"


def parte_1():
    print()
    print(f"  PARTE 1")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        linea = f.readline().rstrip().split(" ")
        x = 0
        y = 0
        while linea != "":
            linea[1] = int(linea[1])
            # print(f"x{linea[0]}x => x{linea[1]}x")
            if linea[0] == "forward":
                x += linea[1]
            elif linea[0] == "down":
                y += linea[1]
            elif linea[0] == "up":
                y -= linea[1]
            else:
                print(f"Problema: {linea}")
            if y < 0:
                print(f"Problema: {y}")
            linea = f.readline().rstrip()
            if linea != "":
                linea = linea.split(" ")
        print(f"  Posición X = {x}, Y = {y}")
        print(f"  Respuesta: {x * y}")


def parte_2():
    print()
    print(f"  PARTE 2")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        linea = f.readline().rstrip().split(" ")
        x = 0
        y = 0
        a = 0
        while linea != "":
            linea[1] = int(linea[1])
            # print(f"x{linea[0]}x => x{linea[1]}x")
            if linea[0] == "forward":
                x += linea[1]
                y += linea[1] * a
            elif linea[0] == "down":
                a += linea[1]
            elif linea[0] == "up":
                a -= linea[1]
            else:
                print(f"Problema: {linea}")
            if y < 0:
                print(f"Problema: {y}")
            linea = f.readline().rstrip()
            if linea != "":
                linea = linea.split(" ")
        print(f"  Posición X = {x}, Y = {y}")
        print(f"  Respuesta: {x * y}")



def main():
    print("2021 ADVENT OF CODE DAY 2")
    parte_1()
    parte_2()
    print()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
