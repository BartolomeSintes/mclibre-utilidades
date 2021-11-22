# Ficheros originales (descargados de la web de Unicode)
UNICODE_ORIGINALES_DIR = "u14_ficheros_1_originales/"
FICHERO_EMOJI_TEST = UNICODE_ORIGINALES_DIR + "u14-emoji-test.txt"
FICHERO_EMOJI_ZWJ_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-zwj-sequences.txt"
FICHERO_EMOJI_VARIATION_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-variation-sequences.txt"
FICHERO_EMOJI_SEQUENCES = UNICODE_ORIGINALES_DIR + "u14-emoji-sequences.txt"
FICHERO_EMOJI_DATA = UNICODE_ORIGINALES_DIR + "u14-emoji-data.txt"
FICHERO_EMOJI_FULL_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji List, v14.0.html"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST = UNICODE_ORIGINALES_DIR + "Full Emoji Modifier Sequences, v14.0.html"

# Ficheros importados (creados a partir de los ficheros originales)
UNICODE_IMPORTADOS_DIR = "u14_ficheros_2_importados/"
FICHERO_IMPORTADO = UNICODE_IMPORTADOS_DIR + "unicode_txt_importados.py"
FICHERO_EMOJI_FULL_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_list.py"
FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST_LISTA = UNICODE_IMPORTADOS_DIR + "unicode_full_emoji_modifier_sequences_list.py"

# Ficheros fusionados (creados a partir de los ficheros importados)
UNICODE_FUSIONADOS_DIR = "u14_ficheros_3_fusionados/"
FICHERO_FUSIONADO_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_1.py"
FICHERO_FUSIONADO_2 = UNICODE_FUSIONADOS_DIR + "unicode_txt_fusionados_2.py"

# Ficheros simplificados
FICHERO_ORDENADO = "unicode_txt_ordenado.py"

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


# Resto que se usa en uc_1_importa_unicode.py, pero el código está comentado, así que realmente no se usa
emoji_data_componentes_auxiliar = [
    "0023",
    "002A",
    "0030", "0031", "0032", "0033", "0034", "0035", "0036", "0037", "0038", "0039",
    "200D",
    "20E3",
    "FE0F",
    "1F1E6", "1F1E7", "1F1E8", "1F1E9", "1F1EA", "1F1EB", "1F1EC", "1F1ED", "1F1EE", "1F1EF", "1F1F0", "1F1F1", "1F1F2", "1F1F3", "1F1F4", "1F1F5", "1F1F6", "1F1F7", "1F1F8", "1F1F9", "1F1FA", "1F1FB", "1F1FC", "1F1FD", "1F1FE", "1F1FF",
    "1F9B0", "1F9B1", "1F9B2", "1F9B3",
    "E0020", "E0021", "E0022", "E0023", "E0024", "E0025", "E0026", "E0027", "E0028", "E0029", "E002A", "E002B", "E002C", "E002D", "E002E", "E002F", "E0030", "E0031", "E0032", "E0033", "E0034", "E0035", "E0036", "E0037", "E0038", "E0039", "E003A", "E003B", "E003C", "E003D", "E003E", "E003F", "E0040", "E0041", "E0042", "E0043", "E0044", "E0045", "E0046", "E0047", "E0048", "E0049", "E004A", "E004B", "E004C", "E004D", "E004E", "E004F", "E0050", "E0051", "E0052", "E0053", "E0054", "E0055", "E0056", "E0057", "E0058", "E0059", "E005A", "E005B", "E005C", "E005D", "E005E", "E005F", "E0060", "E0061", "E0062", "E0063", "E0064", "E0065", "E0066", "E0067", "E0068", "E0069", "E006A", "E006B", "E006C", "E006D", "E006E", "E006F", "E0070", "E0071", "E0072", "E0073", "E0074", "E0075", "E0076", "E0077", "E0078", "E0079", "E007A", "E007B", "E007C", "E007D", "E007E", "E007F",
]
