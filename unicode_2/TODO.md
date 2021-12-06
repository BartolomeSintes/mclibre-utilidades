# CARACTERES UNICODE 2 TODO

## VARIOS

- [2021-11-08] Podría descarga los ficheros de Unicode 13 y hacer los programas que comparen Unicode 13 con Unicode 14 y así voy preparando lo que me tocará hacer cuando se publique Unicode 15.

- [2021-11-19] Páginas que igual debería importar:
  - La lista completa está en https://unicode.org/emoji/charts/index.html
  - Emoji Ordering: https://unicode.org/emoji/charts/emoji-ordering.html

- [2021-11-20] Si me fallan los programas uc_1, uc_2 y uc_3 de importación, no puedo ejecutar de nuevo index.py porque no puede importar uc_4_fusiona porque los ficheros importados no existen. Me toca comentar las línes de uc_4 en index. No sé cómo se corregirá este problema (index podría crear esos ficheros vacíos si no existen, por ejemplo).

## IMPORTACIÓN DE FICHEROS

Después de importar los ficheros, debería crear una matriz unificada con todos los datos, comprobando que los datos teóricamente repetidos efectivamente son iguales.

Por otro lado tendría que tener una matriz manual con mis añadidos a cada uno de los códigos / secuencias:
- página en que las muestro,
- grupo,
- si se ven bien en Win10 (FF/Chrome), Android, Safari,
- si están en twemoji,
- comentarios a añadir en la ficha, etc

A partir de esos dos listas, crear las páginas de salida. En las fichas debería añadir un campo de comentario para explicar los problemas que tiene ese carácter, explicar que se muestra el duibujo.

Por otro lado, tengo que hacer una matriz para twemoji, con todos los dibujos existentes y un programa que compruebe a partir del zip de twemoji, los dibujos que hay.
Cuando el nombre del fichero se pueda derivar, crearlo con regla, pero recuerdo que había excepciones así que tendría que ponerlo.

## FUSIÓN DE FICHEROS IMPORTADOS

Al importar full_emoji_list falta añadir atributo name de td class code, que igual me sirve para twemoji.
Lo he intentado hacer, pero no me aclaraba, así que lo he dejado, porque total no son más que los caracteres unidos con guiones y lo puedo generar. Lo puedo volver a intentar más adelante por si acaso no es siempre así.

Comprobaciones a hacer

comparar grupo y subgrupo y cldr
los cdlr no coinciden

# Detalles

- El antiguo apartado Colores de piel (5), que era por ejemplo
U+26F9 U+FE0F U+1F3FB U+200D U+2640 U+FE0F &#x26f9;&#xfe0f;&#x1f3fb;&#x200d;&#x2640;&#xfe0f;
no están en fusionados_1
Lo que si que está en fusionados_1 es sin el segundo carácter
U+26F9 U+1F3FB U+200D U+2640 U+FE0F &#x26f9;&#x1f3fb;&#x200d;&#x2640;&#xfe0f;
Windows enseña los dos.

- El antiguo apartado Colores de piel modo texto, por ejemplo
U+261D U+FE0E U+1F3FB  &#x261d;&#xfe0e;&#x1f3fb;
no están en fusionados_1
Son sombreados en modo texto
Es cosa de Windows porque salen en Chrome.

# 2021-11-29
- uc_11_generador.py: Tendría que hacer una página que mostrara los simbolos que están en seleccion_simbolos.py pero no están en seleccion_simbolos_manual.py para mirarla el año que viene y decidir si vale la pena incluir algún carácter más (por ejemplo porque ya se ve, como pasa con los símbolos de ajedrez).
- El índice de las páginas está en la plantilla. Estaría bien que se creara automáticamente, pero tendría que añadir a uc_tablas_caracteres el texto que sale en el índice
- Tengo que completar uc_92 para que que añada en manual_1 para cada carácter la información que utilizo de fusionados_2 y de derived_name
- Tengo que completar uc_92 para que diga si el elemento está en twemoji (tendría que hacer un programa intermedio para generar una lista twemoji y luego fusionarla)
- Tengo que hacer un manual_2 con la información que añada yo: si se ve o no en Windows 10, en Windows 11, en Android, en iOS. Y luego están los que se ven en Firefox porque los saca de twemoji.
- Tengo que decidir cómo agrupo las secuencias en las páginas de géneros y colores. Lo más fácil es por forma de codificación y de cortas a largas.
- Tengo que decidir cómo ordeno los caracteres dentro de las secuencias. En principio por orden alfabético, pero en el caso de hombres y mujeres sería mejor que fueran seguidos (si el caracter hombre mujer va al principio, salen mal ordenados). Sería otra opción a añadir a la definición del grupo y hacer una función que ordenara de una forma u otra dependiendo de lo que se pusiera en el grupo (una lista con los números de carácter por los que ordena (el primero, el segundo, etc). No sé si eso sería suficiente para ordenar el grupo de Otras banderas.
- Tengo que añadir una página de restos.
- Tengo que decidir si hago una página con las que se ven en Windows, pero que no están definidas en Unicode. Creo que no, aunque podría mencionarlas.
- Tengo que añadir una página con todos los twemoji.
- Tengo que decidir si en los caracteres que no se ven en Windows (o en Android), pero sí que se ven en twemoji, les añado el twemoji para que se vea cómo es el dibujo.
- Tengo que añadir en los programas que fusionan/importan contadores que digan si quedan cosas pendientes de pasar.
