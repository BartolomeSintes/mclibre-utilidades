# Estructura de la lista fusionados_1

fusionados = [
  [
    # c[0]
    # full_emoji_list + Full_emoji_modifier_sequences_list
    # ['1F600'],
    # c[0][0] Código

    # c[1]
    # full_emoji_list + Full_emoji_modifier_sequences_list
    # ['emoji', '1', 'Smileys & Emotion', 'face-smiling', '😀', 'grinning face'],
    # + c[1][0]: tipo: emoji / emoji_modifier_sequences
    # + c[1][1]: Número de orden: en cada fichero hay un número, así que están duplicados CUIDADO
    # - c[1][2]: Grupo => es siempre como c[2][4]
    # - c[1][3]: Subgrupo => es siempre como c[2][5]
    # - c[1][4]: Carácter => es siempre como c[2][1]
    # - c[1][5]: CLDR short name => es siempre como c[2][3]

    # c[2]
    # emoji_test
    ['fully-qualified', '😀', '1.0', 'grinning face', 'Smileys & Emotion', 'face-smiling'],
    # + c[2][0]: Status: component / fully-qualified / minimally-qualified / unqualified
    # + c[2][1]: Carácter
    # + c[2][2]: Número que creo que es la versión de Unicode
    # + c[2][3]: CLDR short name
    # + c[2][4]: Grupo
    # + c[2][5]: Subgrupo

    # c[3]
    # emoji_data
    # En este fichero están agrupados varios seguidos, así que hay campos que no puedo sacar todos los campos
    # [['Extended_Pictographic'], '1.0'],
    # + c[3][0]: Propiedades (puede haber varias): Emoji / Emoji_Presentation / Emoji_Modifier / Emoji_Modifier_Base / Emoji_Component / Extended_Pictographic / Extended_Pictographic
    # + c[3][1]: Número => es como c[2][2] pero como hay registros que no tienen c[2] no lo puedo quitar

    # c[4]
    # emoji_variation_sequences
    # [], # ['emoji style', '7.0', 'speaking head in silhouette'],
    # + c[4][0]: Style: text style / emoji style
    # + c[4][1]: Número que no tengo claro qué es, es un subconjunto de las versiones de Unicode
    # + c[4][2]: CLDR short name CREO QUE NO LO PUEDO QUITAR PORQUE CUANDO ESTÁ, NO ESTÁ C[2][3]

    # c[5]
    # emoji_zwj_sequences
    # [], # ['RGI_Emoji_ZWJ_Sequence', 'woman surfing: medium-light skin tone', '4.0', 'ðŸ„ðŸ¼\u200dâ™€ï¸', 'Gendered'],
    # type_field: RGI_Emoji_ZWJ_Sequence
    # - c[5][1]: CLDR short name => es siempre como c[2][3]
    # - c[5][2]: Versión de Unicode  => es siempre como c[2][2]
    # - c[5][3]: Carácter => es siempre como c[2][1]
    # Grupo: Family / Role / Gendered / Hair / Other

    # c[6]
    # emoji_sequences
    # En este fichero cada línea agrupados varios caracteres, así que no puedo sacar mucha información
    ['Basic_Emoji', '1.0'],
    # type_field: Basic_Emoji / Emoji_Keycap_Sequence / RGI_Emoji_Flag_Sequence / RGI_Emoji_Tag_Sequence / RGI_Emoji_Modifier_Sequence
    # - c[6][1]: Versión de Unicode  => es siempre como c[2][2]
  ],
]
