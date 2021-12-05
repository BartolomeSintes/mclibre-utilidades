FICHERO = "2021_aoc_3_input.txt"
# FICHERO = "2021_aoc_3_input_test.txt"


def parte_1():
    print()
    print(f"  PARTE 1")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        linea = f.readline().rstrip()
        total = 0
        bits = []
        for i in range(len(linea)):
            bits += [0]
        while linea != "":
            total += 1
            for i in range(len(linea)):
                bits[i] = bits[i] + int(linea[i])
            linea = f.readline().rstrip()
        print(f"  Líneas: {total}")
        print(f"  Bits: {bits}")
        gamma = epsilon = 0
        for i in range(len(bits)):
            if bits[i] > total - bits[i]:
                gamma += 2 ** (len(bits) - i - 1)
            else:
                epsilon += 2 ** (len(bits) - i - 1)

        print(f"  Gamma: {gamma} - Epsilon: {epsilon}")
        print(f"  Resultado: {gamma * epsilon}")

def parte_2():
    print()
    print(f"  PARTE 2")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        linea = f.readline().rstrip()
        longitud = len(linea)
        valores = []
        while linea != "":
            valores += [linea]
            linea = f.readline().rstrip()
        i = 0
        while i < longitud and len(valores) > 1:
            bit_i = 0
            for j in valores:
                bit_i += int(j[i])
            # print(len(valores), bit_i)
            if bit_i >= len(valores) - bit_i:
                for k in range(len(valores) -1, -1, -1):
                    if not int(valores[k][i]):
                        # print("borro 0")
                        del valores[k]
            else:
                for k in range(len(valores) -1, -1, -1):
                    if int(valores[k][i]):
                        # print("borro 1")
                        del valores[k]
            i += 1
        oxydec = 0
        if len(valores) == 1:
            oxygen = valores[0]
            for i in range(len(oxygen)):
                oxydec += int(oxygen[i]) * 2 ** (len(oxygen) - i - 1)
            print(f"  oxygen generator rating: {oxygen} = {oxydec}")
        else:
            print (f"  Problema: valores restantes: {valores}")
    with open(FICHERO, mode="r", encoding="utf-8") as f:
        linea = f.readline().rstrip()
        longitud = len(linea)
        valores = []
        while linea != "":
            valores += [linea]
            linea = f.readline().rstrip()
        i = 0
        while i < longitud and len(valores) > 1:
            bit_i = 0
            for j in valores:
                bit_i += int(j[i])
            # print(len(valores), bit_i)
            if bit_i >= len(valores) - bit_i:
                for k in range(len(valores) -1, -1, -1):
                    if int(valores[k][i]):
                        # print("borro 1")
                        del valores[k]
            else:
                for k in range(len(valores) -1, -1, -1):
                    if not int(valores[k][i]):
                        # print("borro 0")
                        del valores[k]
            i += 1
        co2dec = 0
        if len(valores) == 1:
            co2 = valores[0]
            for i in range(len(co2)):
                co2dec += int(co2[i]) * 2 ** (len(co2) - i - 1)
            print(f"  CO2 scrubber rating: {co2} = {co2dec}")
        else:
            print (f"  Problema: valores restantes: {valores}")

        print()
        if oxydec > 0 and co2dec > 0:
            print(f"  Resultado: {oxydec * co2dec}")
        else:
            print("  Problema: No hay resultado")


def main():
    print("2021 ADVENT OF CODE DAY 3")
    parte_1()
    parte_2()
    print()
    print("Programa terminado")
    print()


if __name__ == "__main__":
    main()
