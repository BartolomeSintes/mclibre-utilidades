import unicode_codigos
import unicode_combinaciones

import gendef


def filtra_grupo(caracteres, inicial, final, pagina):
    resultado = []
    for c in caracteres:
        if int(c[gendef.UCO][0], 16) >= int(inicial, 16) and int(
            c[gendef.UCO][0], 16
        ) <= int(final, 16):
            resultado += [c]

    resultado2 = []
    for c in resultado:
        # Esto filtra los caracteres que simplemente no quiero ver en ningún caso
        if pagina == gendef.PAG_SIMBOLOS:
            if c[gendef.VS] != "" or c[gendef.TWE] == "":
                resultado2 += [c]
        elif pagina == gendef.PAG_EMOJIS:
            if c[gendef.VS] != "" or c[gendef.TWE] == "TWE":
                resultado2 += [c]
    return resultado2


grupos = {
    # Secuencias de Variación
    "Variación": [
        [
            unicode_combinaciones.variacion,
            "Secuencias de variación",
            "variacion",
            "",
            1,
            "00000",
            "1FAFF",
            gendef.FITZPATRICK_NO,
            "",
        ],
    ],
    gendef.PAG_SIMBOLOS: [
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "0000", "007F", gendef.PAG_SIMBOLOS
            ),
            "Controles y Latin básico",
            "controles-latin",
            "U00000-c0-controls-and-basic-latin.pdf",
            1,
            "0000",
            "007F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "0080", "00FF", gendef.PAG_SIMBOLOS
            ),
            "Suplemento controles y Latin-1",
            "controles-sup",
            "U00080-c1-controls-and-latin-1-supplement.pdf",
            1,
            "0080",
            "00FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2000", "206F", gendef.PAG_SIMBOLOS
            ),
            "Puntuación",
            "puntuacion",
            "U02000-general-punctuation.pdf",
            1,
            "2000",
            "206F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "20A0", "20BF", gendef.PAG_SIMBOLOS
            ),
            "Símbolos de monedas",
            "monedas",
            "U020A0-currency-symbols.pdf",
            1,
            "20A0",
            "20BF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2100", "214F", gendef.PAG_SIMBOLOS
            ),
            "Símbolos con letras",
            "simbolos-letras",
            "U02100-letterlike-symbols.pdf",
            1,
            "2100",
            "214F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2190", "21FF", gendef.PAG_SIMBOLOS
            ),
            "Flechas",
            "flechas",
            "U02190-arrows.pdf",
            1,
            "2190",
            "21FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2300", "23FE", gendef.PAG_SIMBOLOS
            ),
            "Símbolos técnicos misceláneos",
            "tecnicos-misc",
            "U02300-miscellaneous-technical.pdf",
            1,
            "2300",
            "23FE",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2460", "24FF", gendef.PAG_SIMBOLOS
            ),
            "Símbolos alfanuméricos con círculo alrededor",
            "alfanum-circulo",
            "U02460-enclosed-alphanumerics.pdf",
            1,
            "2460",
            "24FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2500", "257F", gendef.PAG_SIMBOLOS
            ),
            "Cajas",
            "cajas",
            "U02500-box-drawing.pdf",
            1,
            "2500",
            "257F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "25A0", "25FF", gendef.PAG_SIMBOLOS
            ),
            "Formas geométricas",
            "formas-geometricas",
            "U025A0-geometric-shapes.pdf",
            1,
            "25A0",
            "25FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2600", "26FF", gendef.PAG_SIMBOLOS
            ),
            "Símbolos misceláneos",
            "simbolos-misc",
            "U02600-miscellaneous-symbols.pdf",
            1,
            "2600",
            "26FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2700", "27BF", gendef.PAG_SIMBOLOS
            ),
            "Dingbats",
            "dingbats",
            "U02700-dingbats.pdf",
            1,
            "2700",
            "27BF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2900", "297F", gendef.PAG_SIMBOLOS
            ),
            "Flechas suplementarias B",
            "flechas-suplementarias",
            "U02900-supplemental-arrows-b.pdf",
            1,
            "2900",
            "297F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2B00", "2BFF", gendef.PAG_SIMBOLOS
            ),
            "Símbolos y flechas misceláneos",
            "simbolos-flechas",
            "U02B00-miscellaneous-symbols-and-arrows.pdf",
            1,
            "2B00",
            "2BFF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "3000", "303F", gendef.PAG_SIMBOLOS
            ),
            "Símbolos y puntuación CJK",
            "cjk",
            "U03000-cjk-symbols-and-punctuation.pdf",
            1,
            "3000",
            "303F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "3200", "32FF", gendef.PAG_SIMBOLOS
            ),
            "Símbolos CJK con círculo alrededor",
            "cjk-circulo",
            "U03200-enclosed-cjk-letters-and-months.pdf",
            1,
            "3200",
            "32FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1D100",
                "1D1E8",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos musicales",
            "musica",
            "U1D100-musical-symbols.pdf",
            1,
            "1D100",
            "1D1E8",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F000",
                "1F02B",
                gendef.PAG_SIMBOLOS,
            ),
            "Fichas de Mahjong",
            "fichas-mahjong",
            "U1F000-mahjong-tiles.pdf",
            1,
            "1F000",
            "1F02B",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F030",
                "1F093",
                gendef.PAG_SIMBOLOS,
            ),
            "Fichas de dominó",
            "domino",
            "U1F030-domino-tiles.pdf",
            1,
            "1F030",
            "1F093",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F0A0",
                "1F0F5",
                gendef.PAG_SIMBOLOS,
            ),
            "Cartas",
            "cartas",
            "U1F0A0-playing-cards.pdf",
            1,
            "1F0A0",
            "1F0F5",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F100",
                "1F1FF",
                gendef.PAG_SIMBOLOS,
            ),
            "Suplemento alfanuméricos con círculo alrededor",
            "alfanum-circulo-sup",
            "U1F100-enclosed-alphanumeric-supplement.pdf",
            1,
            "1F100",
            "1F1FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F200",
                "1F2FF",
                gendef.PAG_SIMBOLOS,
            ),
            "Suplemento ideográfico con círculo alrededor",
            "ideografico-circulo-sup",
            "U1F200-enclosed-ideographic-supplement.pdf",
            1,
            "1F200",
            "1F2FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F650",
                "1F67F",
                gendef.PAG_SIMBOLOS,
            ),
            "Dingbats decorativos",
            "dingbats-decorativos",
            "U1F650-ornamental-dingbats.pdf",
            1,
            "1F650",
            "1F67F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F700",
                "1F773",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos alquímicos",
            "simbolos-alquimicos",
            "U1F700-alchemical-symbols.pdf",
            1,
            "1F700",
            "1F773",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F780",
                "1F7EB",
                gendef.PAG_SIMBOLOS,
            ),
            "Formas geométricas extendidas",
            "geometricas-extendidas",
            "U1F780-geometric-shapes-extended.pdf",
            1,
            "1F780",
            "1F7EB",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F300",
                "1F5FF",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos y pictogramas misceláneos",
            "simbolos-pict-misc",
            "U1F300-miscellaneous-symbols-and-pictographs.pdf",
            1,
            "1F300",
            "1F5FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F600",
                "1F64F",
                gendef.PAG_SIMBOLOS,
            ),
            "Emoticonos",
            "emoticonos",
            "U1F600-emoticons.pdf",
            1,
            "1F600",
            "1F64F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F680",
                "1F6FF",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos de transporte y mapas",
            "transporte",
            "U1F680-transport-and-map-symbols.pdf",
            1,
            "1F680",
            "1F6FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1F900",
                "1F9FF",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos y pictogramas misceláneos suplementarios",
            "simbolos-misc-supl",
            "U1F900-supplemental-symbols-and-pictographs.pdf",
            1,
            "1F900",
            "1F9FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode,
                "1FA70",
                "1FAFF",
                gendef.PAG_SIMBOLOS,
            ),
            "Símbolos y pictogramas extendidos A",
            "simbolos-ext-a",
            "U1FA70-symbols-and-pictographs-extended-a.pdf",
            1,
            "1FA70",
            "1FAFF",
            gendef.FITZPATRICK_NO,
            "",
        ],
    ],
    gendef.PAG_EMOJIS: [
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "0000", "007F", gendef.PAG_EMOJIS
            ),
            "Controles y Latin básico",
            "controles-latin",
            "U00000-c0-controls-and-basic-latin.pdf",
            1,
            "0000",
            "007F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "0080", "00FF", gendef.PAG_EMOJIS
            ),
            "Suplemento controles y Latin-1",
            "controles-sup",
            "U00080-c1-controls-and-latin-1-supplement.pdf",
            1,
            "0080",
            "00FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2000", "206F", gendef.PAG_EMOJIS
            ),
            "Puntuación",
            "puntuacion",
            "U02000-general-punctuation.pdf",
            1,
            "2000",
            "206F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "20A0", "20BF", gendef.PAG_EMOJIS
            ),
            "Símbolos de monedas",
            "monedas",
            "U020A0-currency-symbols.pdf",
            1,
            "20A0",
            "20BF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2100", "214F", gendef.PAG_EMOJIS
            ),
            "Símbolos con letras",
            "simbolos-letras",
            "U02100-letterlike-symbols.pdf",
            1,
            "2100",
            "214F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2190", "21FF", gendef.PAG_EMOJIS
            ),
            "Flechas",
            "flechas",
            "U02190-arrows.pdf",
            1,
            "2190",
            "21FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2300", "23FE", gendef.PAG_EMOJIS
            ),
            "Símbolos técnicos misceláneos",
            "tecnicos-misc",
            "U02300-miscellaneous-technical.pdf",
            1,
            "2300",
            "23FE",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2460", "24FF", gendef.PAG_EMOJIS
            ),
            "Símbolos alfanuméricos con círculo alrededor",
            "alfanum-circulo",
            "U02460-enclosed-alphanumerics.pdf",
            1,
            "2460",
            "24FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2500", "257F", gendef.PAG_EMOJIS
            ),
            "Cajas",
            "cajas",
            "U02500-box-drawing.pdf",
            1,
            "2500",
            "257F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "25A0", "25FF", gendef.PAG_EMOJIS
            ),
            "Formas geométricas",
            "formas-geometricas",
            "U025A0-geometric-shapes.pdf",
            1,
            "25A0",
            "25FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2600", "26FF", gendef.PAG_EMOJIS
            ),
            "Símbolos misceláneos",
            "simbolos-misc",
            "U02600-miscellaneous-symbols.pdf",
            1,
            "2600",
            "26FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2700", "27BF", gendef.PAG_EMOJIS
            ),
            "Dingbats",
            "dingbats",
            "U02700-dingbats.pdf",
            1,
            "2700",
            "27BF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2900", "297F", gendef.PAG_EMOJIS
            ),
            "Flechas suplementarias B",
            "flechas-suplementarias",
            "U02900-supplemental-arrows-b.pdf",
            1,
            "2900",
            "297F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "2B00", "2BFF", gendef.PAG_EMOJIS
            ),
            "Símbolos y flechas misceláneos",
            "simbolos-flechas",
            "U02B00-miscellaneous-symbols-and-arrows.pdf",
            1,
            "2B00",
            "2BFF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "3000", "303F", gendef.PAG_EMOJIS
            ),
            "Símbolos y puntuación CJK",
            "cjk",
            "U03000-cjk-symbols-and-punctuation.pdf",
            1,
            "3000",
            "303F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "3200", "32FF", gendef.PAG_EMOJIS
            ),
            "Símbolos CJK con círculo alrededor",
            "cjk-circulo",
            "U03200-enclosed-cjk-letters-and-months.pdf",
            1,
            "3200",
            "32FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1D100", "1D1E8", gendef.PAG_EMOJIS
            ),
            "Símbolos musicales",
            "musica",
            "U1D100-musical-symbols.pdf",
            1,
            "1D100",
            "1D1E8",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F000", "1F02B", gendef.PAG_EMOJIS
            ),
            "Fichas de Mahjong",
            "fichas-mahjong",
            "U1F000-mahjong-tiles.pdf",
            1,
            "1F000",
            "1F02B",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F030", "1F093", gendef.PAG_EMOJIS
            ),
            "Fichas de dominó",
            "domino",
            "U1F030-domino-tiles.pdf",
            1,
            "1F030",
            "1F093",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F0A0", "1F0F5", gendef.PAG_EMOJIS
            ),
            "Cartas",
            "cartas",
            "U1F0A0-playing-cards.pdf",
            1,
            "1F0A0",
            "1F0F5",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F100", "1F1FF", gendef.PAG_EMOJIS
            ),
            "Suplemento alfanuméricos con círculo alrededor",
            "alfanum-circulo-sup",
            "U1F100-enclosed-alphanumeric-supplement.pdf",
            1,
            "1F100",
            "1F1FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F200", "1F2FF", gendef.PAG_EMOJIS
            ),
            "Suplemento ideográfico con círculo alrededor",
            "ideografico-circulo-sup",
            "U1F200-enclosed-ideographic-supplement.pdf",
            1,
            "1F200",
            "1F2FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F650", "1F67F", gendef.PAG_EMOJIS
            ),
            "Dingbats decorativos",
            "dingbats-decorativos",
            "U1F650-ornamental-dingbats.pdf",
            1,
            "1F650",
            "1F67F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F700", "1F773", gendef.PAG_EMOJIS
            ),
            "Símbolos alquímicos",
            "simbolos-alquimicos",
            "U1F700-alchemical-symbols.pdf",
            1,
            "1F700",
            "1F773",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F780", "1F7EB", gendef.PAG_EMOJIS
            ),
            "Formas geométricas extendidas",
            "geometricas-extendidas",
            "U1F780-geometric-shapes-extended.pdf",
            1,
            "1F780",
            "1F7EB",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F300", "1F5FF", gendef.PAG_EMOJIS
            ),
            "Símbolos y pictogramas misceláneos",
            "simbolos-pict-misc",
            "U1F300-miscellaneous-symbols-and-pictographs.pdf",
            1,
            "1F300",
            "1F5FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F600", "1F64F", gendef.PAG_EMOJIS
            ),
            "Emoticonos",
            "emoticonos",
            "U1F600-emoticons.pdf",
            1,
            "1F600",
            "1F64F",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F680", "1F6FF", gendef.PAG_EMOJIS
            ),
            "Símbolos de transporte y mapas",
            "transporte",
            "U1F680-transport-and-map-symbols.pdf",
            1,
            "1F680",
            "1F6FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1F900", "1F9FF", gendef.PAG_EMOJIS
            ),
            "Símbolos y pictogramas misceláneos suplementarios",
            "simbolos-misc-supl",
            "U1F900-supplemental-symbols-and-pictographs.pdf",
            1,
            "1F900",
            "1F9FF",
            gendef.FITZPATRICK_NO,
            "",
        ],
        [
            filtra_grupo(
                unicode_codigos.caracteres_unicode, "1FA70", "1FAFF", gendef.PAG_EMOJIS
            ),
            "Símbolos y pictogramas extendidos A",
            "simbolos-ext-a",
            "U1FA70-symbols-and-pictographs-extended-a.pdf",
            1,
            "1FA70",
            "1FAFF",
            gendef.FITZPATRICK_NO,
            "",
        ],
    ],
    # Banderas
    gendef.PAG_BANDERAS: [
        [
            unicode_combinaciones.cu_otros,
            "Otras secuencias",
            "otras",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            "    <p>En este apartado se muestran las secuencias Unicode que no pertenecen a ninguna de las otras categorías.</p>\n\n",
        ],
        [
            unicode_combinaciones.cu_banderas_sub,
            "Banderas (subdivisiones)",
            "banderas-2",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas regionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#banderas-subdivisiones">apartado Banderas (secuencias) de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.cu_banderas,
            "Banderas",
            "banderas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode que corresponden a banderas nacionales. Estas secuencias se comentan en el <a href="html-unicode-secuencias.html#banderas">apartado Banderas de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
    ],
    # Géneros que funcionan en Windows y en Twemoji
    gendef.PAG_GENEROS: [
        [
            unicode_combinaciones.genero_1,
            "Género (1)",
            "genero-1",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con tres caracteres, combinado el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.genero_2,
            "Género (2)",
            "genero-2",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinado el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        # CUIDADO problematicas_piel_1 están también como genero_3_b porque al poner colores de piel no salen bien en Windows
        # Lo que me faltaría es ordenar los elementos, porque ahora se añaden al final
        # pero no tengo claro cómo ordenar matrices multidimensionales https://www.php.net/manual/es/def.array-multisort.php
        [
            unicode_combinaciones.genero_3 + unicode_combinaciones.genero_3_b,
            "Género (3)",
            "genero-3",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinado un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.genero_4,
            "Género (4)",
            "genero-4",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cinco caracteres, combinado un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        #  ["Colores de piel",                                     "colores-piel",    "", 0, "0261D", "1F9FF"],
        #  ["Otros",                                               "otros",           "", 4, "0002A", "1F4FF"],
    ],
    # Colores de piel que funcionan en Windows y en Twemoji
    gendef.PAG_FITZPATRICK: [
        [
            unicode_combinaciones.piel_1_texto,
            "Colores de piel modo texto",
            "colores-piel-texto",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_TEXTO,
            '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick de caracteres cuya representación predeterminada es en modo texto. Estas secuencias se forman con dos caracteres, combinado un caracter que prepresenta un individuo o una parte del cuerpo con uno de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.piel_1,
            "Colores de piel (1)",
            "colores-piel-1",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con dos o tres caracteres, combinado un caracter (o dos si se trata de un caracter cuya representación predeterminada es en modo texto) que prepresenta un individuo o una parte del cuerpo con uno de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.genero_1,
            "Colores de piel (2)",
            "colores-piel-2",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con cuatro caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de tres caracteres que representa un personaje femenino o masculino, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.genero_2,
            "Colores de piel (3)",
            "colores-piel-3",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de cuatro caracteres que representa un personaje femenino o masculino, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.genero_3,
            "Colores de piel (4)",
            "colores-piel-4",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con cinco caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de cuatro caracteres que representa un personaje femenino o masculino, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.piel_5,
            "Colores de piel (5)",
            "colores-piel-5",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI_3,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con seis caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de cinco caracteres que representa un personaje femenino o masculino, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
    ],
    # Parejas y familias
    gendef.PAG_PAREJAS: [
        [
            unicode_combinaciones.cu_familias,
            "Familias",
            "familias",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a familias formadas por uno o dos padres y uno o dos hijos. Estas secuencias se forman con tres, cinco o siete caracteres, combinado los caracteres de hombre, mujer, niña o niño, como se comenta en el <a href="html-unicode-secuencias.html#familias">apartado Familias de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.cu_parejas_1,
            "Parejas de enamorados",
            "parejas-1",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de enamorados. Estas secuencias se forman con seis caracteres, combinado los caracteres de hombre, mujer y corazón, como se comenta en el <a href="html-unicode-secuencias.html#enamorados">apartado Parejas de enamorados de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.cu_parejas_2,
            "Parejas de enamorados besándose",
            "parejas-2",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas de enamorados. Estas secuencias se forman con ocho caracteres, combinado los caracteres de hombre, mujer, corazón y beso, como se comenta en el <a href="html-unicode-secuencias.html#enamorados-besandose">apartado Parejas de enamorados besándose de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.cu_parejas_piel_1,
            "Parejas neutras y colores de piel",
            "parejas-piel-1",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas neutras (es decir, sin identificar claramente si son hombres o mujeres), con modificadores Fitzpatrick. Estas secuencias se forman con cinco o siete caracteres, combinado los caracteres de adultos y apretón de manos, además de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#parejas-neutras-colores-piel">apartado Parejas neutras (y colores de piel) de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
        [
            unicode_combinaciones.cu_parejas_piel_2,
            "Parejas con género y colores de piel",
            "parejas-piel-2",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran las secuencias Unicode ZWJ que corresponden a parejas con género (es decir, identificando si cada miembro de la pareja es hombre o mujer), con modificadores Fitzpatrick. Estas secuencias se forman con dos o siete caracteres, a partir de los caracteres de parejas o combinado los caracteres de hombre y mujer y apretón de manos, además de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#parejas-genero-colores-piel">apartado Parejas con género (y colores de piel) de la lección Secuencias Unicode</a>.</p>\n\n',
        ],
    ],
    # Secuencias que no van bien en Windows o en Twemoji
    gendef.PAG_PROBLEMAS: [
        [
            unicode_combinaciones.problematicas_otros,
            "Otras secuencias",
            "otras-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            "    <p>En este apartado se muestran las secuencias Unicode que no pertenecen a ninguna de las otras categorías. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n",
        ],
        # Géneros que NO funcionan en Windows o en Twemoji
        [
            unicode_combinaciones.problematicas_genero_1,
            "Género (1)",
            "genero-1-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con tres caracteres, combinado el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_genero_2,
            "Género (2)",
            "genero-2-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinado el carácter hombre o mujer con un objeto relacionado con la profesión, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_genero_3,
            "Género (3)",
            "genero-3-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cuatro caracteres, combinado un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_genero_4,
            "Género (4)",
            "genero-4-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_NO,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que corresponden a profesiones o actividades con personajes femeninos o masculinos. Estas secuencias se forman con cinco caracteres, combinado un carácter que normalmente ya representa a un individuo con el símbolo masculino o femenino, como se comenta en el <a href="html-unicode-secuencias.html#generos">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        # Colores de piel que NO funcionan en Windows o en Twemoji
        [
            unicode_combinaciones.problematicas_piel_1_texto,
            "Colores de piel modo texto",
            "colores-piel-texto-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_TEXTO,
            '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick de caracteres cuya representación predeterminada es en modo texto. Estas secuencias se forman con dos caracteres, combinado un caracter que prepresenta un individuo o una parte del cuerpo con uno de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_piel_1,
            "Colores de piel (1)",
            "colores-piel-1-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode con modificadores Fitzpatrick. Estas secuencias se forman con dos, combinado un caracter que prepresenta un individuo o una parte del cuerpo con uno de los modificadores Fitzpatrick, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_piel_2,
            "Colores de piel (2)",
            "colores-piel-2-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con cuatro o cinco caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de caracteres que representa un personaje femenino, masculino o neutro, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_piel_3,
            "Colores de piel (3)",
            "colores-piel-3-problemas", # como colores-piel-5
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI_3,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ con modificadores Fitzpatrick. Estas secuencias se forman con seis caracteres, añadiendo uno de los modificadores Fitzpatrick a la secuencia Unicode ZWJ de cinco caracteres que representa un personaje femenino o masculino, como se comenta en el <a href="html-unicode-secuencias.html#fitzpatrick">apartado Géneros de la lección Secuencias Unicode</a>. Actualmente (junio de 2020) estas secuencias no se ven correctamente en Windows 10.</p>\n\n',
        ],
        [
            unicode_combinaciones.problematicas_piel_4,
            "Colores de piel (4)",
            "colores-piel-4-problemas",
            "",
            0,
            "",
            "",
            gendef.FITZPATRICK_YES_EMOJI,
            '    <p>En este apartado se muestran secuencias Unicode ZWJ que actualmente (junio de 2020) no están definidas en Unicode aunque Windows 10 sí que las muestra. No se recomienda su uso.</p>\n\n',
        ],
    ],
}
