FICHERO = "2021_aoc_1_input.txt"
# FICHERO = "2021_aoc_1_input_test.txt"


def parte_1():
    print()
    print(f"  PARTE 1")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        line_1 = int(f.readline().rstrip())
        contador = 1
        contador_mayor = contador_menor = 0
        line_2 = int(f.readline().rstrip())
        while line_2:
            contador += 1
            if line_2 > line_1:
                contador_mayor += 1
            else:
                contador_menor += 1
            line_1 = line_2
            line_2 = f.readline().rstrip()
            if line_2 != "":
                line_2 = int(line_2)
        print()
        print(f"  {contador} valores: {contador_menor} menor / {contador_mayor} mayor = {contador_menor + contador_mayor} comparaciones")
        print()
        print(f"  Respuesta: {contador_mayor}")

def parte_2():
    print()
    print(f"  PARTE 2")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        line_1 = int(f.readline().rstrip())
        line_2 = int(f.readline().rstrip())
        line_3 = int(f.readline().rstrip())
        line_4 = int(f.readline().rstrip())
        contador = 3
        contador_mayor = contador_menor = 0
        while line_4:
            suma_1 = line_1 + line_2 + line_3
            suma_2 = line_2 + line_3 + line_4
            contador += 1
            if suma_2 > suma_1:
                contador_mayor += 1
            else:
                contador_menor += 1
            line_1, line_2, line_3 = line_2, line_3, line_4
            line_4 = f.readline().rstrip()
            if line_4 != "":
                line_4 = int(line_4)
        print()
        print(f"  {contador} valores: {contador_menor} menor / {contador_mayor} mayor = {contador_menor + contador_mayor} sumas comparadas")
        print()
        print(f"  Respuesta: {contador_mayor}")


def main():
    print("2021 ADVENT OF CODE DAY 1")
    parte_1()
    parte_2()
    print()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
