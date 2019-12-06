import json, pathlib
from datetime import date
import gconst, gweb, gjson


def main():
    gweb.guarda_index("mclibre")
    gweb.guarda_colecciones("mclibre")

    # Actualmente no incluyo la vista de las fichas
    # gweb.guarda_fichas()


if __name__ == "__main__":
    main()
