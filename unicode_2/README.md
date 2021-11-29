# CARACTERES UNICODE 2 README

En noviembre de 2021 me he dado cuenta de que no puedo mantener a mano los ficheros de emojis, así que he decidido hacer programas que me filtren los ficheros publicados por Unicode con la información sobre emoji y trabajar a partir de ellos.

## COSAS A TENER EN CUENTA EL AÑO QUE VIENE

- Al importar DerivedName hay líneas que resumen muchos carácteres (ideográficos). Lo que he he hecho ha sido ignorar esas líneas al importar el fichero. Tendría que comprobar manualmente que esas líneas efectivamente las quiero ignorar.

## FICHEROS PUBLCIADOS POR UNICODE

Por un lado hay cinco ficheros .txt publicados en dos directorios distintos
- https://unicode.org/Public/emoji/14.0/
    - [emoji-sequences.txt](https://unicode.org/Public/emoji/14.0/emoji-sequences.txt)
    - [emoji-test.txt](https://unicode.org/Public/emoji/14.0/emoji-test.txt)
    - [emoji-zwj-sequences.txt](https://unicode.org/Public/emoji/14.0/emoji-zwj-sequences.txt)
- https://www.unicode.org/Public/14.0.0/ucd/emoji/
    - [emoji-data.txt](https://www.unicode.org/Public/14.0.0/ucd/emoji/emoji-data.txt)
    - [emoji-variation-sequences.txt](https://www.unicode.org/Public/14.0.0/ucd/emoji/emoji-variation-sequences.txt)

Por otro lado, hay dos páginas web con listas completas:
- [Full Emoji Modifier Sequences, v14.0.html](https://www.unicode.org/emoji/charts/full-emoji-modifiers.html)
- [Full Emoji List, v14.0.html](https://www.unicode.org/emoji/charts/full-emoji-list.html)

Por otro lado, hay un fichero con todos los códigos Unicode individuales:
- [DerivedName.txt](https://www.unicode.org/Public/14.0.0/ucd/extracted/DerivedName.txt)

## IMPORTACIÓN DE LOS FICHEROS

- Full Emoji List, v14.0.html y Full Emoji Modifier Sequences, v14.0.html
  Como estas páginas la guardo con el navegador, el final de líneas es CR/LF, así que con Notepad++ lo cambio a LF
  Por suerte, los dos programas que importan estas páginas son idénticos.
- emoji-test.txt
  Este fichero no da problemas
- emoji-data.txt
  Este fichero es un horror
  Para empezar incluye símbolos gráficos que no son emojis (al menos el nombre está en mayúsculas)
  Además incluye caracteres reservados
  Pero lo peor es que agrupa caracteres consecutivos, porque hay caracteres reservados junto con caracteres válidos, por ejemplo, 1F1AD..1F1E5 MASK WORK SYMBOL..<reserved-1F1E5>

## PRESENTACIONES TEXTO/EMOJI

Creo que ya sé cómo saber cuál es la presentación predeterminada de los caracteres que tienen dos presentaciones (texto y emoji).

- En [TR51](http://www.unicode.org/reports/tr51/#Emoji_Presentation) dicen que los que son por defecto emojis son los que tienen la propiedad Emoji_Presentation y los que no la tienen son por defecto texto.
- En el fichero [emoji-data.txt](https://www.unicode.org/Public/14.0.0/ucd/emoji/emoji-data.txt) es donde ponen las propiedades.
- Así que lo que hago para cada carácter es mirar en el fichero unicode_txt_importados.py
    - primero miro si el carácter está en la lista emoji_variation_sequences:
        - Si está, es emoji-texto o texto-emoji. Para distignuir cada caso, miro después en la lista emoji_data:
            - Si el carácter tiene incluidas las propiedades "Emoji" y "Emoji_Presentation", entonces es emoji-texto
            - Si el carácter no tiene incluidas las propiedades "Emoji" y "Emoji_Presentation", entonces es texto-emoji
        - Si no está, es emoji o texto. Para distignuir cada caso, miro después en la lista emoji_data:
            - Si el carácter tiene incluida la propiedad "Emoji", entonces es emoji
            - Si el carácter no tiene incluida la propiedad "Emoji", entonces es texto


