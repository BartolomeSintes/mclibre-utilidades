import gweb


def main():
    restos = gweb.guarda_colecciones("mclibre")[1]
    # Listado cronológico
    gweb.guarda_fichas(restos)
    gweb.guarda_index(restos)


if __name__ == "__main__":
    main()
