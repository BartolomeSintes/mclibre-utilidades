import json


def ordena(json, criterio, orden):
    final = dict(json)
    final["legislacion"] = sorted(
        final["legislacion"], key=lambda x: x[criterio], reverse=orden
    )
    return final


def selecciona(lista, campo, valor):
    lista2 = lista[:]
    for elemento in lista2[:]:
        if elemento[campo] != valor:
            lista2.remove(elemento)
    return lista2


def selecciona_en_json(json, clave, valor):
    for i in json:
        if i[clave] == valor:
            return i


def cuenta_referencias_en_coleccion(json):
    cuenta = 0
    for aptdo in json["contenido"]:
        cuenta += len(aptdo["apartado"]["referencias"])
    return cuenta
