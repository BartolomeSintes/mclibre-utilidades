UCO = 0  # Código(s) Unicode
UNV = 1  # Versión Unicode en que se incluyó
VS = 2  # Si el código tiene versión emoji / texto: VST / VSE
WIN = 3  # Si se ve en windows: VACIO / WIN
VSW = 4  # Si Windows distingue entre emoji / texto: VACIO / VSW
SHO = 5  # Si se enseña o no
TWE = 6  # Si está en Twemoji
TWV = 7  # En qué versión se incluyó en Twemoji
TWO = 8  # Si está en la fuente Twemoji Color Font o en GitHub: TCF / TGH
DESC = 9  # Descripción

FITZPATRICK_NO = 0
FITZPATRICK_YES_EMOJI = 1    # El código Fitzpatrick va normalmente en segunda posición
FITZPATRICK_YES_EMOJI_3 = 3  # Pero en algunos casos va en tercera
FITZPATRICK_YES_TEXTO = 2

QUITA_FE0F_NO = 0
QUITA_FE0F_YES = 1

PAG_SIMBOLOS = "simbolos"
PAG_EMOJIS = "emojis"
PAG_BANDERAS = "banderas"
PAG_GENEROS = "generos"
PAG_FITZPATRICK = "fitzpatrick"
PAG_PAREJAS = "parejas"
PAG_PROBLEMAS = "problemas"
VARIACION = 2

FICHERO_SIMBOLOS = "html-unicode-simbolos.html"
FICHERO_EMOJIS = "html-unicode-dibujos.html"
FICHERO_BANDERAS = "html-unicode-secuencias-banderas.html"
FICHERO_GENEROS = "html-unicode-secuencias-generos.html"
FICHERO_FITZPATRICK = "html-unicode-secuencias-colores.html"
FICHERO_PAREJAS = "html-unicode-secuencias-parejas.html"
FICHERO_PROBLEMAS = "html-unicode-secuencias-problematicas.html"

fitzpatrick = [
    ["1F3FB", ": light skin tone"],
    ["1F3FC", ": medium-light skin tone"],
    ["1F3FD", ": medium skin tone"],
    ["1F3FE", ": medium-dark skin tone"],
    ["1F3FF", ": dark skin tone"],
]
