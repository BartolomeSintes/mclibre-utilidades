def divide_cadena(origen, maximo):
    t = origen.split(" ")
    check = True
    for palabra in t:
        if len(palabra) > maximo:
            raise Exception(
                f'Problema: "{palabra}" es demasiado larga para ancho de línea {maximo}'
            )
    if check:
        t2 = []
        while len(t) > 0:
            u = ""
            while len(t) > 0 and len(u) + len(t[0]) <= maximo:
                u += t[0] + " "
                del t[0]
            t2 += [u]
        return t2


s = "Esto es una prueba de como se podría cortar una cadaena muy larga en trozos de un tamaño determinado, para poder generar los formularios."
longitud = 20

print(s)
for i in divide_cadena(s, longitud):
    print(i)
