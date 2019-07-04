

# Crea directorios de DESTINO
# En la primera versión, la estructira de directorios copiaba la estructura del
# directorio sitio-plantilla con idea de crear los ficheros a partir de los que
# hubiera ahí, pero al final  creo los ficheros directamente, así que también he
# acabado creando directamente los directorios
# print("Creando directorios de destino")
# for i in pathlib.Path(ORIGEN).rglob(f"*"):
#     directorio = str(i.parent)
#     directorio = directorio.replace(ORIGEN, DESTINO)
#     p = pathlib.Path(directorio)
#     if not p.exists():
#         print(f"  {directorio}")
#         p.mkdir(parents=True, exist_ok=True)
# print("Directorios creados.")
# print()


