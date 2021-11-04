# CARACTERES UNICODE

Este repositorio contiene un programa para generar las páginas de los apuntes de html/css que muestran los caracteres gráficos de Unicode, incluidos los emojis.


## Errores

- Warnings del W3C Validator en la página de símbolos están relacionados con esto

    - carácter problemático: &#x1D15E;
      Text run is not in Unicode Normalization Form C.
      <https://stackoverflow.com/questions/5465170/text-run-is-not-in-unicode-normalization-form-c>

    - carácter problemático: &#x1D165;
      Text run starts with a composing character.
      <https://www.w3.org/Bugs/Public/show_bug.cgi?id=13502>


## Cosas por hacer

- El menú de enlaces de las páginas está incluido en la plantilla. Debería generarlos el programa para que sólo pusiera los necesarios.

- Hacer un svg con una ficha de ejemplo que explique qué es cada cosa de la ficha (con flechas señalando cada parte y texto explicando)

- El 23/06/20 pasé el validador a la página de dibujos Unicode y descubrí algo nuevo. El W3C validator da un warning con varios símbolos musiclaes: "text run is not in Unicode Normalization Form C" NFC. Parece que algunos símbolos se deberían poder hacer componiendo otros dos. Por ejemplo 1d15e se podría hacer escribiendo 1d157 + 1d165 (esta combinación aparece en el pdf de unicode como NFC). Pero he probado y en Windows no funciona (ver stack overflow 5465170). También me dio un warning en otros casos diciendo "Text run starts with a composing character" (1d166, 1d167, 1d168, 1d169, 1d16d). No sé si se refiere a que estos carácteres deberían aparecer solo en composiciones con otros, no sueltos.

- Hay bastantes banderas regionales definidas, pero no son RGI. Las únicas RGI son las del reino unido
    <https://emojipedia.org/flag-for-zurich-chzh/>
    <https://emojipedia.org/flag-for-baja-california-mxbcn/>
    <https://emojipedia.org/flag-for-normandie-frnor/>
    <https://emojipedia.org/flag-for-california-usca/>
    <https://emojipedia.org/flag-for-ontario-caon/>

- Si un grupo al filtrarlo se queda sin elementos lo sigue poniendo en la página

- Hacer iconos de incorrectos en sistemas operativos (W10, Android, iOS) para añadirlos en la ficha de los emojis

- En el caso de los caracteres con representaciones texto/emoji no sé cuál es la represenbación por defecto. La única página que veo sobre el tema es <https://unicode.org/emoji/charts/emoji-style.html> pero no me aclaro con ella. En Unicode 12 publicaron una lista <https://unicode.org/Public/emoji/12.0/emoji-variation-sequences.txt>, pero no dice cuál es el predeterminado. Y en Unicode 13 esa lista no existe. Por ejemplo, apunté que Battery o White flower no son emojis, pero Windows sí que los muestra como emojis, pero no sé de dónde saqué esa información.
En el caso de los caracteres con representaciones texto/emoji la representación predeterminada la tendría que mirar en <https://www.unicode.org/Public/13.0.0/ucd/emoji/emoji-data.txt>. pero es una página muy incómoda, se supone que primero listan todos los emojis y luego dicen los que tienen Emoji_Presentation por defecto. Según esa lista Battery y White Flower sí que sería emoji.
<https://dict.emojiall.com/es/property-emoji-presentation-list> tiene una lista que podría utilziar si me fío de ella. Según esa lista Battery y White Flower sí que sería emoji.

- Tengo descargados los svg de Twemoji 12 y 13. Tendgo que organizarlos por directorios que coincidan con los apartados que aparecen en los apuntes (fmailias, géneros, etc.). Tendría que tener en un directorio los de 12, en otro los de 13 separando los que coinciden con 12 y los distintos, y en otro los de 13 todos juntos para cuando toque compararlos con 14.

- Representación Texto / Emoji

  - No he conseguido aclararme cuál es la representación predeterminada cuando un caracter tiene representación texto/emoji. Puedo ver lo que hace Windows, pero no sé si es correcto.< Se supone que lo explican en <https://unicode.org/emoji/charts-13.0/emoji-style.html> pero yo no entiendo esa página. En <https://unicode.org/emoji/charts-12.1/emoji-variants.html> están todos los caracteres texto/emoji pero no dice cuál es el predeterminado. En <https://www.unicode.org/Public/13.0.0/ucd/emoji/emoji-data.txt> ponen Emoji_Presentation en algunos, pero no tengo claro si eso es que es la forma predeterminada.

  - Hay unos cuántos caracteres que parece que Windows no distingue entre texto y emoji aunque están en twemoji: A9, AE, 203C, 2122, 2194, 2195, 263A, 2640, 2642, 2660, 2663, 2665, 2666

  - En el caso de los palos de la baraja 2660 lo tengo puesto como emoji 2663, 2665 y 2666 como texto, pero no sé si es correcto.

- Parejas &gt; Colores de piel: No dice los colores de piel en la descripción de los dibujos (light-skin, etc.)

- En Windows se puede hacer una pareja de mujeres sin color de piel con 1F469 200D 1F91D 200D 1F469, pero yo creo que no es correcto, que la pareja de mujeres es 1F46D 1F3FB.

- No sé si los tipos de pelo (bald, curly, etc.) los debería contar en las secuencias. Ahora los tengo metidos como una combinación más en Género (1) o en Colores de piel (2).

- Texto/emoji, clolores de piel o banderas no usan ZWJ, pero cuando se combinan caracteres, sí que hay ZWJ. Eso no lo digo en los apuntes.

- No he contado que los emojis simples en 2020 cambian a neutros y que se introducen combinaciones con 1F9D1 (adulto sin género).

- Podría comentar Twemoji Color Font con Twemoji-colr para ver cuál me interesa más utilizar.

- Los caracteres o secuencias que no se ven en Windows deberían estar también en problemáticas todas, pero algunas están en las lecciones correspondientes (los caracteres), pero las secuencias no.

- La página de emojis está organizada por bloques Unicode, pero igual deberían estar organizadas por temas.

- Tendría que reorganizar las matrices de caracteres y secuencias.

  - quitar los campos que ahora no uso

  - si es VS, si se ven en W10, Android, iOS

  - si es emoji, el tema del emoji (animales, transporte, etc.)

  - si es secuencia, qué patrón sigue

  - si tiene fitzpatrick, posición código fp

  - si está en el twemoji, qué se quita en el enlace (el fe0f)

  - incluir en la matriz el ancho del cuadro de muestra

  - la idea sería que la generación de los cuadros de muestra fuera automática a partir de la matriz

- Si al filtrar un grupo, no queda ningún elemento, ahora añade en el índice el grupo

- Añadir a problemáticas las familias que se ven en Windows pero que no están en Unicode, diciendo que no hay que utilizarlas.

- Twemoji en algunos casos no incluye el fe0f en el nombre del caracter, pero en el resto los manitene. Los quita en los siguientes casos:

  - los emojis sueltos: xxx + fe0f

  - los colores de piel xxx + fe0f + fp

  - los colores de piel xxx + fe0f + fp + 200d + 2640/2 + fe0f (quita el primero pero no el segundo)
