import gweb


def main():
    gweb.guarda_index()
    gweb.guarda_colecciones("mclibre")

    # Listado cronológico
    gweb.guarda_fichas()


if __name__ == "__main__":
    main()
