# Ficheros originales (descargados de la web de Unicode)
UNICODE_ORIGINALES_DIR = "u14_ficheros_1_originales/"
FICHERO_EMOJI_TEST = UNICODE_ORIGINALES_DIR + "u14-emoji-test.txt"
FICHERO_EMOJI_ZWJ_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-zwj-sequences.txt"
FICHERO_EMOJI_VARIATION_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-variation-sequences.txt"
FICHERO_EMOJI_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-sequences.txt"
FICHERO_EMOJI_DATA = UNICODE_ORIGINALES_DIR + "u14-emoji-data.txt"
FICHERO_EMOJI_FULL_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji List, v14.0.html"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji Modifier Sequences, v14.0.html"
FICHERO_DERIVED_NAME = UNICODE_ORIGINALES_DIR + "u14-DerivedName.txt"

# Ficheros importados (creados a partir de los ficheros originales)
UNICODE_IMPORTADOS_DIR = "u14_ficheros_2_importados/"
FICHERO_IMPORTADO = UNICODE_IMPORTADOS_DIR + "unicode_txt_importados.py"
FICHERO_EMOJI_FULL_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_list.py"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_modifier_sequences_list.py"
FICHERO_UNICODE = UNICODE_IMPORTADOS_DIR + "unicode_txt_derived_name.py"

# Ficheros fusionados (creados a partir de los ficheros importados)
UNICODE_FUSIONADOS_DIR = "u14_ficheros_3_fusionados/"
FICHERO_FUSIONADO_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_1.py"
FICHERO_FUSIONADO_2 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_2.py"
FICHERO_MANUAL_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_1.py"

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
PAG_PROBLEMAS = "problemas"
SELECCION_SIMBOLOS = "seleccion-simbolos"

FICHERO_SITIO_SIMBOLOS = "html-unicode-simbolos.html"
FICHERO_SITIO_EMOJIS = "html-unicode-dibujos.html"
FICHERO_SITIO_BANDERAS = "html-unicode-secuencias-banderas.html"
FICHERO_SITIO_GENEROS = "html-unicode-secuencias-generos.html"
FICHERO_SITIO_FITZPATRICK = "html-unicode-secuencias-colores.html"
FICHERO_SITIO_PAREJAS = "html-unicode-secuencias-parejas.html"
FICHERO_SITIO_PROBLEMAS = "html-unicode-secuencias-problematicas.html"
FICHERO_SELECCION_SIMBOLOS = "seleccion_simbolos.py"

# Unicode
uc_tipos = ["emoji", "emoji_modifier_sequence"]
uc_status = ["component", "fully-qualified", "minimally-qualified", "unqualified"]
uc_version = ["0.0", "0.6", "0.7", "1.0", "1.1", "2.0", "3.0", "3.1", "3.2", "4.0", "4.1", "5.0", "5.1", "5.2", "6.0", "7.0", "11.0", "12.0", "12.1", "13.0", "13.1", "14.0"]
uc_version_2 = ["1.1", "3.0", "3.2", "4.0", "4.1", "5.1", "5.2", "6.0", "7.0"]
uc_property = ["Emoji", "Emoji_Presentation", "Emoji_Modifier", "Emoji_Modifier_Base", "Emoji_Component", "Extended_Pictographic", "Extended_Pictographic"]
uc_style = ["emoji style", "text style"]
uc_type_sequence = ["RGI_Emoji_ZWJ_Sequence"]
uc_type = ["Basic_Emoji", "Emoji_Keycap_Sequence", "RGI_Emoji_Flag_Sequence", "RGI_Emoji_Tag_Sequence", "RGI_Emoji_Modifier_Sequence"]

uc_type_sequence_grupo =  ["Family", "Role", "Gendered", "Hair", "Other"]
uc_group = ["Smileys & Emotion", "People & Body", "Component", "Animals & Nature", "Food & Drink", "Travel & Places", "Activities", "Objects", "Symbols", "Flags"]
uc_subgroup = [
    "face-smiling", "face-affection", "face-tongue", "face-hand", "face-neutral-skeptical", "face-sleepy", "face-unwell", "face-hat", "face-glasses", "face-concerned", "face-negative", "face-costume", "cat-face", "monkey-face", "emotion",
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
    "gr-familias", "gr-parejas-corazon-1", "gr-parejas-beso-1", "gr-parejas-mano-piel-1", "gr-parejas-mano-piel-2", "gr-parejas-corazon-piel-1", "gr-parejas-corazon-piel-2", "gr-parejas-beso-piel-1", "gr-parejas-beso-piel-2",
    "gr-texto-emoji",
    "gr-keycap",
    "gr-restos",
]

uc_grupos_banderas = [
    [ "gr-banderas-regiones",
      "Banderas (subdivisiones regionales)",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas regionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#banderas-subdivisiones">apartado Banderas (subdivisiones regionales) de la lección Secuencias Unicode</a>.</p>\n',
    ],
    [ "gr-banderas-otras",
      "Otras banderas",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas que no pertenecen a ninguna de las otras categorías. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#otras">apartado Otras de la lección Secuencias Unicode</a>.</p>\n',
    ],
    [ "gr-banderas-paises",
      "Banderas",
      '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas nacionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#banderas">apartado Banderas de la lección Secuencias Unicode</a>.</p>\n',
    ],
]

uc_grupos_generos = [
    ["gr-genero-1", "Género (1)",
    '',
    ],
    ["gr-genero-2", "Género (2)",
    '',
    ],
    ["gr-genero-3", "Género (3)",
    '',
    ],
    ["gr-genero-4", "Género (4)",
    '',
    ],
    ["gr-genero-5", "Género (5)",
    '',
    ],
    ["gr-genero-6", "Género (6)",
    '',
    ],
    ["gr-genero-7", "Género (7)",
    '',
    ],
    ["gr-genero-8", "Género (8)",
    '',
    ],
]

uc_grupos_fitzpatrick = [
    ["gr-colores-piel-1", "Colores de piel (1)",
    '',
    ],
    ["gr-colores-piel-2", "Colores de piel (2)",
    '',
    ],
    ["gr-colores-piel-3", "Colores de piel (3)",
    '',
    ],
    ["gr-colores-piel-4", "Colores de piel (4)",
    '',
    ],
    ["gr-colores-piel-5", "Colores de piel (5)",
    '',
    ],
    ["gr-colores-piel-6", "Colores de piel (6)",
    '',
    ],
    ["gr-colores-piel-7", "Colores de piel (7)",
    '',
    ],
    ["gr-colores-piel-8", "Colores de piel (8)",
    '',
    ],
]

uc_grupos_parejas = [
    ["gr-familias-1", "Familias de 2 miembros",
    '',
    ],
    ["gr-familias-2", "Familias de 3 miembros",
    '',
    ],
    ["gr-familias-3", "Familias de 4 miembros",
    '',
    ],
    ["gr-parejas-mano-piel-1", "Parejas masculinas/femeninas de la mano, con el mismo tono de piel",
    '',
    ],
    ["gr-parejas-mano-piel-2", "Parejas masculinas/femeninas de la mano, con dos tonos de piel",
    '',
    ],
    ["gr-parejas-mano-piel-3", "Parejas neutras de la mano, con dos tonos de piel",
    '',
    ],
    ["gr-parejas-corazon-1", "Rostros masculinos/femeninos de enamorados",
    '',
    ],
    ["gr-parejas-corazon-piel-1", "Rostros masculinos/femeninos de enamorados, con dos tonos de piel (1)",
    '',
    ],
    ["gr-parejas-corazon-piel-2", "Rostros masculinos/femeninos de enamorados, con dos tonos de piel (2)",
    '',
    ],
    ["gr-parejas-corazon-piel-3", "Rostros neutros de enamorados, con dos tonos de piel (1)",
    '',
    ],
    ["gr-parejas-corazon-piel-4", "Rostros neutros de enamorados, con dos tonos de piel (2)",
    '',
    ],
    ["gr-parejas-beso-1", "Rostros masculinos/femeninos de enamorados besándose",
    '',
    ],
    ["gr-parejas-beso-piel-1", "Rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (1)",
    '',
    ],
    ["gr-parejas-beso-piel-2", "Rostros masculinos/femeninos de enamorados besándose, con dos tonos de piel (2)",
    '',
    ],
    ["gr-parejas-beso-piel-3", "Rostros neutros de enamorados besándose, con dos tonos de piel (1)",
    '',
    ],
    ["gr-parejas-beso-piel-4", "Rostros neutros de enamorados besándose, con tonos de piel (2)",
    '',
    ],
]
uc_grupos_2b = [
    ["gr-componentes",
    ],
    ["gr-texto-emoji",
    ],
    ["gr-keycap",
    ],
    ["gr-restos",
    ]
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
        "1F773",
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
