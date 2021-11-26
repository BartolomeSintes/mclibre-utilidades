# Barto 9 de abril de 2020
# Este programa genera bonitas páginas Web

import json, pathlib, shutil, operator, time

SVG_ORIGEN = "plantilla-spain.svg"
HTML_ORIGEN = "plantilla-spain..html"

muertes_covid = {
    "muertes": [
        {
            "fecha": "2020-03-04",
            "Andalucía": 0,
            "Aragón": 0,
            "Asturias": 0,
            "Baleares": 0,
            "Canarias": 0,
            "Cantabria": 0,
            "Castilla - La Mancha": 0,
            "Castilla y León": 0,
            "Cataluña": 0,
            "Ceuta": 0,
            "Comunidad Valenciana": 1,
            "Extremadura": 0,
            "Galicia": 0,
            "Madrid": 0,
            "Melilla": 0,
            "Murcia": 0,
            "Navarra": 0,
            "País Vasco": 0,
            "La Rioja": 0,
            "España": 1,
        },
    ]
}

def mapa_spain():
    pass
