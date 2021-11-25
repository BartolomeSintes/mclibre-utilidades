# CARACTERES UNICODE 2 README

En noviembre de 2021 me he dado cuenta de que no puedo mantener a mano los ficheros de emojis, así que he decidido hacer programas que me filtren los ficheros publicados por Unicode con la información sobre emoji y trabajar a partir de ellos.

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

##
