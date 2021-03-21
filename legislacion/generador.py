import gweb


def main():
    gweb.guarda_index()
    restos = gweb.guarda_colecciones("mclibre")[1]
    # Listado cronológico
    gweb.guarda_fichas(restos)


if __name__ == "__main__":
    main()
