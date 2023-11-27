# Ficheros originales (descargados de la web de Unicode)
UNICODE_ORIGINALES_DIR = "ficheros_1_originales/"
FICHERO_EMOJI_TEST = UNICODE_ORIGINALES_DIR + "u15-1-emoji-test.txt"
FICHERO_EMOJI_ZWJ_SEQUENCES = UNICODE_ORIGINALES_DIR + "u15-1-emoji-zwj-sequences.txt"
FICHERO_EMOJI_VARIATION_SEQUENCES = UNICODE_ORIGINALES_DIR + "u15-1-emoji-variation-sequences.txt"
FICHERO_EMOJI_SEQUENCES = UNICODE_ORIGINALES_DIR + "u15-1-emoji-sequences.txt"
FICHERO_EMOJI_DATA = UNICODE_ORIGINALES_DIR + "u15-1-emoji-data.txt"
FICHERO_EMOJI_FULL_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji List, v15.1.htm"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji Modifier Sequences, v15.1.htm"
FICHERO_DERIVED_NAME = UNICODE_ORIGINALES_DIR + "u15-1-DerivedName.txt"

# Ficheros importados (creados a partir de los ficheros originales)
UNICODE_IMPORTADOS_DIR = "ficheros_2_importados/"
FICHERO_IMPORTADO = UNICODE_IMPORTADOS_DIR + "unicode_txt_importados.py"
FICHERO_EMOJI_FULL_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_list.py"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_modifier_sequences_list.py"
FICHERO_UNICODE = UNICODE_IMPORTADOS_DIR + "unicode_txt_derived_name.py"

# Ficheros fusionados (creados a partir de los ficheros importados)
UNICODE_FUSIONADOS_DIR = "ficheros_3_fusionados/"
FICHERO_FUSIONADO_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_1.py"
FICHERO_FUSIONADO_2 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_2.py"
FICHERO_MANUAL_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_1.py"
FICHERO_MANUAL_1_NOTO = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_1_noto.py"
FICHERO_MANUAL_2 = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_2.py"

# Ficheros simplificados
FICHERO_ORDENADO = "unicode_txt_ordenado.py"

PAGINA_MANUAL_1 = UNICODE_FUSIONADOS_DIR + "html-manual-1.html"
PAGINA_MANUAL_2 = UNICODE_FUSIONADOS_DIR + "html-manual-2.html"

# Ficheros del sitio creado
PAG_SIMBOLOS = "simbolos"
PAG_EMOJIS = "emojis"
PAG_BANDERAS = "banderas"
PAG_GENEROS = "generos"
PAG_FITZPATRICK = "fitzpatrick"
PAG_PAREJAS = "parejas"
PAG_SENTIDO = "sentido"
PAG_OTRAS = "otras"
PAG_TWEMOJI = "twemoji"
PAG_NOTO = "noto"
PAG_PROBLEMAS = "problemas"
SELECCION_SIMBOLOS = "seleccion-simbolos"

FICHERO_SITIO_SIMBOLOS = "html-unicode-simbolos.html"
FICHERO_SITIO_EMOJIS = "html-unicode-dibujos.html"
FICHERO_SITIO_BANDERAS = "html-unicode-secuencias-banderas.html"
FICHERO_SITIO_GENEROS = "html-unicode-secuencias-generos.html"
FICHERO_SITIO_FITZPATRICK = "html-unicode-secuencias-colores.html"
FICHERO_SITIO_PAREJAS = "html-unicode-secuencias-parejas.html"
FICHERO_SITIO_SENTIDO = "html-unicode-secuencias-sentido.html"
FICHERO_SITIO_OTRAS = "html-unicode-secuencias-otras.html"
FICHERO_SITIO_TWEMOJI = "html-unicode-twemoji.html"
FICHERO_SITIO_NOTO = "html-unicode-noto.html"
FICHERO_SITIO_PROBLEMAS = "html-unicode-secuencias-problematicas.html"
FICHERO_SELECCION_SIMBOLOS = "seleccion_simbolos.py"

ORDENA_ESPECIAL_NO = 0
ORDENA_ESPECIAL_1 = 1 # Para ordenar poniendo seguidos 1F468/1F469
ORDENA_ESPECIAL_2 = 2 # Para ordenar poniendo seguidos 1F3FB/1F3FC/1F3FD/1F3FE/1F3FF
ORDENA_ESPECIAL_3 = 3 # Para ordenar banderas

# Twemoji
DIRECTORIO_TWEMOJI = "D:\\Descargas\\TWEMOJI\\twemoji-14-0-2-220331\\assets\\svg"

# Noto
DIRECTORIO_NOTO = "D:\\Descargas\\GOOGLE NOTO\\noto-emoji-main-2023-11-17\\svg"

# Unicode
uc_tipos = ["emoji", "emoji_modifier_sequence"]
uc_status = ["component", "fully-qualified", "minimally-qualified", "unqualified"]
uc_version = ["0.0", "0.6", "0.7", "1.0", "1.1", "2.0", "3.0", "3.1", "3.2", "4.0", "4.1", "5.0", "5.1", "5.2", "6.0", "7.0", "11.0", "12.0", "12.1", "13.0", "13.1", "14.0", "15.0", "15.1"]
uc_version_2 = ["1.1", "3.0", "3.2", "4.0", "4.1", "5.1", "5.2", "6.0", "7.0"]
uc_importacion_1 = ["0.6", "0.7", "1.0", "2.0", "3.0", "4.0", "5.0", "11.0", "12.0", "12.1", "13.0", "13.1", "14.0", "15.0", "15.1"]
uc_importacion_2 = ["0.0", "0.6", "0.7", "1.0", "2.0", "3.0", "4.0", "5.0", "11.0", "12.0", "12.1", "13.0", "13.1", "14.0", "15.0", "15.1"]
uc_importacion_3 = ["2.0", "4.0", "5.0", "11.0", "12.0", "12.1", "13.0", "13.1", "14.0", "15.0", "15.1"]
uc_importacion_4 = ["0.6", "0.7", "1.0", "2.0", "3.0", "4.0", "5.0", "11.0", "12.0", "13.0", "13.1", "14.0", "15.0", "15.1"]
# uc_versiones_marcadas = ["6.1", "6.2", "6.3", "7.0", "8.0", "9.0", "10.0", "11.0", "12.0", "13.0", "13.1", "14.0", "15.0", "15.1"]
uc_versiones_marcadas = ["13.0", "13.1", "14.0", "15.0", "15.1"]
uc_versiones_years = {  "6.1": 2012, "6.2": 2012, "6.3": 2013, 7: 2014, 8: 2015, 9:2016, 10: 2017, 11: 2018, 12: 2019, "12.1": 2019, 13: 2020, "13.1": 2020, 14: 2021, 15: 2022, "15.1": 2023 }
uc_property = ["Emoji", "Emoji_Presentation", "Emoji_Modifier", "Emoji_Modifier_Base", "Emoji_Component", "Extended_Pictographic", "Extended_Pictographic"]
uc_style = ["emoji style", "text style"]
uc_type_sequence = ["RGI_Emoji_ZWJ_Sequence"]
uc_type = ["Basic_Emoji", "Emoji_Keycap_Sequence", "RGI_Emoji_Flag_Sequence", "RGI_Emoji_Tag_Sequence", "RGI_Emoji_Modifier_Sequence"]

uc_type_sequence_grupo =  ["Family", "Role", "Gendered", "Hair", "Other"]
uc_group = ["Smileys & Emotion", "People & Body", "Component", "Animals & Nature", "Food & Drink", "Travel & Places", "Activities", "Objects", "Symbols", "Flags"]
uc_subgroup = [
    "face-smiling", "face-affection", "face-tongue", "face-hand", "face-neutral-skeptical", "face-sleepy", "face-unwell", "face-hat", "face-glasses", "face-concerned", "face-negative", "face-costume", "cat-face", "monkey-face", "heart", "emotion",
    "hand-fingers-open", "hand-fingers-partial", "hand-single-finger", "hand-fingers-closed", "hands", "hand-prop", "body-parts", "person", "person-gesture", "person-role", "person-fantasy", "person-activity", "person-sport", "person-resting", "family", "person-symbol",
    "skin-tone", "hair-style",
    "animal-mammal", "animal-bird", "animal-amphibian", "animal-reptile", "animal-marine", "animal-bug", "plant-flower", "plant-other",
    "food-fruit", "food-vegetable", "food-prepared", "food-asian", "food-marine", "food-sweet", "drink", "dishware",
    "place-map", "place-geographic", "place-building", "place-religious", "place-other", "transport-ground", "transport-water", "transport-air", "hotel", "time", "sky & weather",
    "event", "award-medal", "sport", "game", "arts & crafts",
    "clothing", "sound", "music", "musical-instrument", "phone", "computer", "light & video", "book-paper", "money", "mail", "writing", "office", "lock", "tool", "science", "medical", "household", "other-object",
    "transport-sign", "warning", "arrow", "religion", "zodiac", "av-symbol", "gender", "math", "punctuation", "currency", "other-symbol", "keycap", "alphanum", "geometric",
    "flag", "country-flag", "subdivision-flag"
]

uc_grupos_2 = [
    "gr-componentes",
    "gr-banderas-paises", "gr-banderas-regiones", "gr-banderas-otras",
    "gr-genero-1", "gr-genero-2", "gr-genero-3", "gr-genero-4", "gr-genero-5", "gr-genero-6", "genero-7",
    "gr-colores-piel-1", "gr-colores-piel-2", "gr-colores-piel-3", "gr-colores-piel-4", "gr-colores-piel-5", "gr-colores-piel-6","gr-colores-piel-7", "gr-colores-piel-8",
    "gr-familias", "gr-parejas-corazon-1", "gr-parejas-corazon-2", "gr-parejas-beso-1", "gr-parejas-beso-2", "gr-parejas-mano-piel-1", "gr-parejas-mano-piel-2", "gr-parejas-corazon-piel-1", "gr-parejas-corazon-piel-2", "gr-parejas-beso-piel-1", "gr-parejas-beso-piel-2",
    "gr-texto-emoji",
    "gr-keycap",
    "gr-restos",
]

uc_grupos_banderas = [
    [ "gr-banderas-regiones",
      "Banderas (subdivisiones regionales)",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas regionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#gr-banderas-regiones">apartado Banderas (subdivisiones regionales) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    [ "gr-banderas-otras",
      "Otras banderas",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas que no pertenecen a ninguna de las otras categorías. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#gr-banderas-otras">apartado Otras de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    [ "gr-banderas-paises",
      "Banderas nacionales",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas nacionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#gr-banderas-paises">apartado Banderas de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
]

uc_grupos_generos = [
    ["gr-genero-1", "Géneros (1)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con tres caracteres, combinando el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-1">apartado Géneros (1) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_1
    ],
    ["gr-genero-2", "Géneros (2)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con tres caracteres, combinando un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-2">apartado Géneros (2) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-3", "Géneros (3)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes neutros (ni femeninos ni masculinos). Estas secuencias se forman con tres caracteres, combinando el <i>emoji</i> que representa a un adulto con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-3">apartado Géneros (3) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-4", "Géneros (4)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinando el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-4">apartado Géneros (4) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-5", "Géneros (5)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinando un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-5">apartado Géneros (5) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-6", "Géneros (6)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinando un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-6">apartado Géneros (6) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-7", "Géneros (7)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes neutros (ni femeninos ni masculinos). Estas secuencias se forman con cuatro caracteres, combinando el <i>emoji</i> que representa a un adulto con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-7">apartado Géneros (7) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-genero-8", "Géneros (8)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cinco caracteres, combinando un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-8">apartado Géneros (8) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
]

uc_grupos_fitzpatrick = [
    ["gr-colores-piel-1", "Colores de piel (1)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con dos caracteres, combinando un caracter que representa un individuo o una parte del cuerpo con uno de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-1">apartado Colores de piel (1) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-colores-piel-2", "Colores de piel (2)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cuatro caracteres, combinando el carácter hombre o mujer con uno de los modificadores Fitzpatrick y con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-2">apartado Colores de piel (2) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-3", "Colores de piel (3)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cuatro caracteres, combinando un carácter que normalmente ya representa a un individuo con uno de los modificadores Fitzpatrick y con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-3">apartado Colores de piel (3) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-4", "Colores de piel (4)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cuatro caracteres, combinando el <i>emoji</i> que representa a un adulto con uno de los modificadores Fitzpatrick y con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-4">apartado Colores de piel (4) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-5", "Colores de piel (5)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, combinando el carácter hombre o mujer con uno de los modificadores Fitzpatrick y con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-5">apartado Colores de piel (5) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-6", "Colores de piel (6)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, combinando un carácter que normalmente ya representa a un individuo con uno de los modificadores Fitzpatrick y con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-6">apartado Colores de piel (6) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-7", "Colores de piel (7)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, combinando el <i>emoji</i> que representa a un adulto con uno de los modificadores Fitzpatrick y con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-7">apartado Colores de piel (7) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_2
    ],
    ["gr-colores-piel-8", "Colores de piel (8)",
    '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, combinando los emojis que representan una mano izquierda y una mano derecha con dos modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#gr-colores-piel-8">apartado Colores de piel (8) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
]

uc_grupos_parejas = [
    ["gr-familias-4", "Familias genéricas",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a familias genéricas formadas por tres o cuatro miembros: uno o dos adultos y uno o dos niños. Estas secuencias se forman con cinco o siete caracteres, combinando los caracteres de adulto y niño, como se comenta en el <a href="html-unicode-secuencias.html#familias">apartado Familias de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
     ],
    ["gr-familias-1", "Familias de 2 miembros",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a familias formadas por dos miembros: un padre o una madre y un hijo o una hija. Estas secuencias se forman con tres caracteres, combinando los caracteres de hombre, mujer, niña o niño, como se comenta en el <a href="html-unicode-secuencias.html#familias">apartado Familias de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-familias-2", "Familias de 3 miembros",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a familias formadas por tres miembros: uno o dos progenitores y uno o dos hijos. Estas secuencias se forman con cinco caracteres, combinando los caracteres de hombre, mujer, niña o niño, como se comenta en el <a href="html-unicode-secuencias.html#familias">apartado Familias de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-familias-3", "Familias de 4 miembros",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a familias formadas por cuatro miembros: dos progenitores y dos hijos. Estas secuencias se forman con siete caracteres, combinando los caracteres de hombre, mujer, niña o niño, como se comenta en el <a href="html-unicode-secuencias.html#familias">apartado Familias de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-mano-piel-1", "Parejas masculinas/femeninas cogidas de la mano, con el mismo tono de piel",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas con género (es decir, identificando si cada miembro de la pareja es hombre o mujer), con modificadores Fitzpatrick común (los dos personajes tienen el mismo color de piel). Estas secuencias se forman con dos caracteres, combinando los caracteres de parejas y los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-mano-piel-1">apartado Parejas masculinas/femeninas cogidas de la mano, con el mismo tono de piel, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-mano-piel-2", "Parejas masculinas/femeninas cogidas de la mano, con dos tonos de piel",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas con género (es decir, identificando si cada miembro de la pareja es hombre o mujer), con modificadores Fitzpatrick distintos (los dos personajes tienen distinto color de piel). Estas secuencias se forman con siete caracteres, combinando los caracteres hombre y/o mujer y los modificadores Fitzpatrick con el carácter apretón de manos, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-mano-piel-2">apartado Parejas masculinas/femeninas cogidas de la mano, con dos tonos de piel, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-mano-piel-3", "Parejas neutras cogidas de la mano, con dos tonos de piel",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas neutras (con personajes ni femeninos ni masculinos), con modificadores Fitzpatrick. Estas secuencias se forman con siete caracteres, combinando combinando dos emojis que representan a adultos con los modificadores Fitzpatrick y con el carácter apretón de manos, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-mano-piel-3">apartado Parejas neutras cogidas de la mano, con dos tonos de piel, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-1", "Parejas de rostros masculinos/femeninos de enamorados (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados. Estas secuencias se forman con cinco caracteres, combinando los caracteres de hombre y/o mujer, con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-1">apartado Parejas de rostros masculinos/femeninos de enamorados (1) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-2", "Parejas de rostros masculinos/femeninos de enamorados (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados. Estas secuencias se forman con seis caracteres, combinando los caracteres de hombre y/o mujer, con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-2">apartado Parejas de rostros masculinos/femeninos de enamorados (2) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-piel-1", "Parejas de rostros masculinos/femeninos de enamorados, con dos tonos de piel (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados, con modificadores Fitzpatrick. Estas secuencias se forman con siete caracteres, combinando los caracteres de hombre y/o mujer, con modificadores Fitzpatrick y con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-piel-1">apartado Parejas de rostros masculinos/femeninos de enamorados, con dos tonos de piel (1) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-piel-2", "Parejas de rostros masculinos/femeninos de enamorados, con dos tonos de piel (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados, con modificadores Fitzpatrick. Estas secuencias se forman con ocho caracteres, combinando los caracteres de hombre y/o mujer, con modificadores Fitzpatrick y con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-piel-2">apartado Parejas de rostros masculinos/femeninos de enamorados, con dos tonos de piel (2) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-piel-3", "Parejas de rostros neutros de enamorados, con dos tonos de piel (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas neutras (con personajes ni femeninos ni masculinos), con modificadores Fitzpatrick distintos (los dos personajes tienen distinto color de piel). Estas secuencias se forman con siete caracteres, combinando combinando dos emojis que representan a adultos con los modificadores Fitzpatrick y con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-piel-3">apartado Parejas de rostros neutros de enamorados, con dos tonos de piel (1), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-corazon-piel-4", "Parejas de rostros neutros de enamorados, con dos tonos de piel (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas neutras (con personajes ni femeninos ni masculinos), con modificadores Fitzpatrick distintos (los dos personajes tienen distinto color de piel). Estas secuencias se forman con ocho caracteres, combinando combinando dos emojis que representan a adultos con los modificadores Fitzpatrick y con el carácter corazón, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-corazon-piel-4">apartado Parejas de rostros neutros de enamorados, con dos tonos de piel (2), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-1", "Parejas de rostros masculinos/femeninos de enamorados besándose (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados besándose. Estas secuencias se forman con siete caracteres, combinando los caracteres de hombre y/o mujer, con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-1">apartado Parejas de rostros masculinos/femeninos de enamorados besándose (1), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-2", "Parejas de rostros masculinos/femeninos de enamorados besándose (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados besándose. Estas secuencias se forman con siete caracteres, combinando los caracteres de hombre y/o mujer, con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-2">apartado Parejas de rostros masculinos/femeninos de enamorados besándose (2), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-piel-1", "Parejas de rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados besándose, con modificadores Fitzpatrick. Estas secuencias se forman con nueve caracteres, combinando los caracteres de hombre y/o mujer, con modificadores Fitzpatrick y con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-piel-1">apartado Parejas de rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (1), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-piel-2", "Parejas de rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de rostros de enamorados besándose, con modificadores Fitzpatrick. Estas secuencias se forman con diez caracteres, combinando los caracteres de hombre y/o mujer, con modificadores Fitzpatrick y con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-piel-2">apartado Parejas de rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (2), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-piel-3", "Parejas de rostros neutros de enamorados besándose, con dos tonos de piel (1)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a rostros de personajes neutros (ni femeninos ni masculinos), con modificadores Fitzpatrick distintos (los dos personajes tienen distinto color de piel). Estas secuencias se forman con nueve caracteres, combinando combinando dos emojis que representan a adultos con los modificadores Fitzpatrick y con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-piel-3">apartado Parejas de rostros neutros de enamorados besándose, con dos tonos de piel (1), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-parejas-beso-piel-4", "Parejas de rostros neutros de enamorados besándose, con dos tonos de piel (2)",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a rostros de personajes neutros (ni femeninos ni masculinos), con modificadores Fitzpatrick distintos (los dos personajes tienen distinto color de piel). Estas secuencias se forman con diez caracteres, combinando combinando dos emojis que representan a adultos con los modificadores Fitzpatrick y con los caracteres corazón y marca de labios, como se comenta en el <a href="html-unicode-secuencias.html#gr-parejas-beso-piel-4">apartado Parejas de rostros neutros de enamorados besándose, con dos tonos de piel (2), de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
]

uc_grupos_sentido = [
    ["gr-sentido-1", "Sentido (1)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con seis o siete caracteres, combinando el carácter hombre o mujer con un objeto relacionado con la profesión, además del código Fitzpatrick y el identificador de dirección para dirigir al personaje hacia la derecha, como se comenta en el <a href="html-unicode-secuencias.html#gr-genero-1">apartado Géneros (1) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-sentido-2", "Sentido (2)",
    '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con seis o siete  caracteres, combinando un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, además del código Fitzpatrick y el identificador de dirección para dirigir al personaje hacia la derecha, como se comenta en el <a href="html-unicode-secuencias.html#gr-sentido-2">apartado Sentido (2) de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
]

uc_grupos_otras = [
    # ["gr-componentes", "Componentes",
    # "", ORDENA_ESPECIAL_NO
    # ],
    # ["gr-texto-emoji", "Texto-emoji",
    #  "", ORDENA_ESPECIAL_NO
    # ],
    ["gr-keycap-1", "Caracteres enmarcados (teclas), modo texto",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a teclas de un teclado de ordenador, en modo texto. Estas secuencias se forman con dos caracteres, combinando algunos caracteres con el componente de borde de tecla, como se comenta en el <a href="html-unicode-secuencias.html#gr-keycap-1">apartado Caracteres enmarcados (teclas), modo texto, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-keycap-2", "Caracteres enmarcados (teclas), modo <i>emoji</i>",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a teclas de un teclado de ordenador, en modo <i>emoji</i>. Estas secuencias se forman con tres caracteres, combinando algunos caracteres con el componente de borde de tecla, como se comenta en el <a href="html-unicode-secuencias.html#gr-keycap-1">apartado Caracteres enmarcados (teclas), modo <i>emoji</i>, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ],
    ["gr-restos", "Otras secuencias",
    '    <p>En este apartado se muestran las secuencias Unicode ZWJ que no corresponden a ninguna de las agrupaciones comentadas en esta página o en el las otras páginas dedicadas a secuencias Unicode. Estas secuencias se forman combinando varios caracteres, como se comenta en el <a href="html-unicode-secuencias.html#gr-restos">apartado Otras secuencias, de la lección Secuencias Unicode</a>.</p>\n', ORDENA_ESPECIAL_NO
    ]
]

uc_grupos_twemoji = uc_grupos_noto = [
    # Este grupo es para que en la página de Twemoji incluya los componentes, aunque hay componentes que no están en ese pdf, pero el encabezado está pensado para enlazar un solo pdf.
    ["Componentes", "gr-componentes",        "U1F100-enclosed-alphanumeric-supplement.pdf",
        "1F100",
        "1F1FF",

    ],
]

uc_tablas_caracteres = [
    [
        "Controles y Latin básico",
        "gr-controles-latin",
        "U00000-c0-controls-and-basic-latin.pdf",
        "0000",
        "007F",
    ],
    [
        "Suplemento controles y Latin-1",
        "gr-controles-sup",
        "U00080-c1-controls-and-latin-1-supplement.pdf",
        "0080",
        "00FF",
    ],
    [
        "Puntuación",
        "gr-puntuacion",
        "U02000-general-punctuation.pdf",
        "2000",
        "206F",
    ],
    [
        "Símbolos de monedas",
        "gr-monedas",
        "U020A0-currency-symbols.pdf",
        "20A0",
        "20C0",
    ],
    [
        "Símbolos con letras",
        "gr-simbolos-letras",
        "U02100-letterlike-symbols.pdf",
        "2100",
        "214F",
    ],
    [
        "Flechas",
        "gr-flechas",
        "U02190-arrows.pdf",
        "2190",
        "21FF",
    ],
    [
        "Símbolos técnicos misceláneos",
        "gr-tecnicos-misc",
        "U02300-miscellaneous-technical.pdf",
        "2300",
        "23FE",
    ],
    [
        "Símbolos alfanuméricos con círculo alrededor",
        "gr-alfanum-circulo",
        "U02460-enclosed-alphanumerics.pdf",
        "2460",
        "24FF",
    ],
    [
        "Cajas",
        "gr-cajas",
        "U02500-box-drawing.pdf",
        "2500",
        "257F",
    ],
    [
        "Formas geométricas",
        "gr-formas-geometricas",
        "U025A0-geometric-shapes.pdf",
        "25A0",
        "25FF",
    ],
    [
        "Símbolos misceláneos",
        "gr-simbolos-misc",
        "U02600-miscellaneous-symbols.pdf",
        "2600",
        "26FF",
    ],
    [
        "Dingbats",
        "gr-dingbats",
        "U02700-dingbats.pdf",
        "2700",
        "27BF",
    ],
    [
        "Flechas suplementarias B",
        "gr-flechas-suplementarias",
        "U02900-supplemental-arrows-b.pdf",
        "2900",
        "297F",
    ],
    [
        "Símbolos y flechas misceláneos",
        "gr-simbolos-flechas",
        "U02B00-miscellaneous-symbols-and-arrows.pdf",
        "2B00",
        "2BFF",
    ],
    [
        "Símbolos y puntuación CJK",
        "gr-cjk",
        "U03000-cjk-symbols-and-punctuation.pdf",
        "3000",
        "303F",
    ],
    [
        "Símbolos CJK con círculo alrededor",
        "gr-cjk-circulo",
        "U03200-enclosed-cjk-letters-and-months.pdf",
        "3200",
        "32FF",
    ],
    [
        "Símbolos musicales",
        "gr-musica",
        "U1D100-musical-symbols.pdf",
        "1D100",
        "1D1FF",
    ],
    [
        "Fichas de Mahjong",
        "gr-fichas-mahjong",
        "U1F000-mahjong-tiles.pdf",
        "1F000",
        "1F02B",
    ],
    [
        "Fichas de dominó",
        "gr-domino",
        "U1F030-domino-tiles.pdf",
        "1F030",
        "1F093",
    ],
    [
        "Cartas",
        "gr-cartas",
        "U1F0A0-playing-cards.pdf",
        "1F0A0",
        "1F0F5",
    ],
    [
        "Suplemento alfanuméricos con círculo alrededor",
        "gr-alfanum-circulo-sup",
        "U1F100-enclosed-alphanumeric-supplement.pdf",
        "1F100",
        "1F1FF",
    ],
    [
        "Suplemento ideográfico con círculo alrededor",
        "gr-ideografico-circulo-sup",
        "U1F200-enclosed-ideographic-supplement.pdf",
        "1F200",
        "1F2FF",
    ],
    [
        "Dingbats decorativos",
        "gr-dingbats-decorativos",
        "U1F650-ornamental-dingbats.pdf",
        "1F650",
        "1F67F",
    ],
    [
        "Símbolos alquímicos",
        "gr-simbolos-alquimicos",
        "U1F700-alchemical-symbols.pdf",
        "1F700",
        "1F77F",
    ],
    [
        "Formas geométricas extendidas",
        "gr-geometricas-extendidas",
        "U1F780-geometric-shapes-extended.pdf",
        "1F780",
        "1F7F0",
    ],
    [
        "Símbolos y pictogramas misceláneos",
        "gr-simbolos-pict-misc",
        "U1F300-miscellaneous-symbols-and-pictographs.pdf",
        "1F300",
        "1F5FF",
    ],
    [
        "Emoticonos",
        "gr-emoticonos",
        "U1F600-emoticons.pdf",
        "1F600",
        "1F64F",
    ],
    [
        "Símbolos de transporte y mapas",
        "gr-transporte",
        "U1F680-transport-and-map-symbols.pdf",
        "1F680",
        "1F6FF",
    ],
    [
        "Símbolos y pictogramas misceláneos suplementarios",
        "gr-simbolos-misc-supl",
        "U1F900-supplemental-symbols-and-pictographs.pdf",
        "1F900",
        "1F9FF",
    ],
    [
        "Símbolos de ajedrez",
        "gr-ajedrez",
        "U1FA00-chess-symbols.pdf",
        "1FA00",
        "1FA6F",
    ],
    [
        "Símbolos y pictogramas extendidos A",
        "gr-simbolos-ext-a",
        "U1FA70-symbols-and-pictographs-extended-a.pdf",
        "1FA70",
        "1FAFF",
    ],
],

# Resto que se usa en uc_1_importa_unicode.py, pero el código está comentado, así que realmente no se usa
# emoji_data_componentes_auxiliar = [
#     "0023",
#     "002A",
#     "0030", "0031", "0032", "0033", "0034", "0035", "0036", "0037", "0038", "0039",
#     "200D",
#     "20E3",
#     "FE0F",
#     "1F1E6", "1F1E7", "1F1E8", "1F1E9", "1F1EA", "1F1EB", "1F1EC", "1F1ED", "1F1EE", "1F1EF", "1F1F0", "1F1F1", "1F1F2", "1F1F3", "1F1F4", "1F1F5", "1F1F6", "1F1F7", "1F1F8", "1F1F9", "1F1FA", "1F1FB", "1F1FC", "1F1FD", "1F1FE", "1F1FF",
#     "1F9B0", "1F9B1", "1F9B2", "1F9B3",
#     "E0020", "E0021", "E0022", "E0023", "E0024", "E0025", "E0026", "E0027", "E0028", "E0029", "E002A", "E002B", "E002C", "E002D", "E002E", "E002F", "E0030", "E0031", "E0032", "E0033", "E0034", "E0035", "E0036", "E0037", "E0038", "E0039", "E003A", "E003B", "E003C", "E003D", "E003E", "E003F", "E0040", "E0041", "E0042", "E0043", "E0044", "E0045", "E0046", "E0047", "E0048", "E0049", "E004A", "E004B", "E004C", "E004D", "E004E", "E004F", "E0050", "E0051", "E0052", "E0053", "E0054", "E0055", "E0056", "E0057", "E0058", "E0059", "E005A", "E005B", "E005C", "E005D", "E005E", "E005F", "E0060", "E0061", "E0062", "E0063", "E0064", "E0065", "E0066", "E0067", "E0068", "E0069", "E006A", "E006B", "E006C", "E006D", "E006E", "E006F", "E0070", "E0071", "E0072", "E0073", "E0074", "E0075", "E0076", "E0077", "E0078", "E0079", "E007A", "E007B", "E007C", "E007D", "E007E", "E007F",
# ]
