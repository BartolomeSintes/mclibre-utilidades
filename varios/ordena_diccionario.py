import random

claves = ["a", "b", "c", "d"]

n = 10  # número de elementos
m = 100  # rango de valores

def ordena(lista, clave):
    cambios = True
    while cambios:
        cambios = False
        for i in range(len(lista) - 1):
            if lista[i][clave] > lista[i + 1][clave]:
                cambios = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


lista = []
for i in range(n):
    elemento = dict()
    for i in claves:
        elemento[i] = random.randrange(m)
    lista += [elemento]
for i in lista:
    print(i)

lista = ordena(lista, "b")
print()
for i in lista:
    print(i)


