# AYUDA

## 2022-10-16

- He generado la página de emojis que están en la fuente Google Noto, que está más actualizada que Twemoji.

- He creado un programa uc_93 que es una copia del uc_92 pero modificado para Noto en vez de Twemoji.

## 2022-10-14

- He añadido en uc_11_generador que añada estrellitas en los cuadros de emojis incluidos en las últimas versiones de unicode (los que se indiquen en uc_versiones_years). Es un apaño porque los ficheros a partir de los que hago las páginas no contiene toda la información, así que me toca volver a buscar la versión. Tendría que reescribir el programa para que empezara creando un fichero con toda la información, y a partir de ella que creara las páginas. Otro año será.

## 2022-10-12

En 2022-09-13 publicaron Unicode 15. Quiero actualizar las páginas de los apuntes.

- Hago una copia de unicode_2 y le he llamado unicode_3

- Descargo los cinco ficheros:
    - https://unicode.org/Public/emoji/15.0/emoji-sequences.txt
    - https://unicode.org/Public/emoji/15.0/emoji-test.txt
    - https://unicode.org/Public/emoji/15.0/emoji-zwj-sequences.txt
    - https://www.unicode.org/Public/15.0.0/ucd/emoji/emoji-data.txt
    - https://www.unicode.org/Public/15.0.0/ucd/emoji/emoji-variation-sequences.txt
    - https://www.unicode.org/emoji/charts/full-emoji-list.html
    - https://www.unicode.org/Public/15.0.0/ucd/extracted/DerivedName.txt

- En ucdef.py cambio las referencias a 14 por 15 y añado 15.0 en lista uc_version

- Ejecuto index.py
    - Ejecuto 1, 2, 3 y 4
    - Al ejecutar index > 4 Fusionar listas Unicode me dice "subgrupo no esperado". Tengo que añadir en ucdef.py uc_subgroup el subgrupo "heart". Miro en full-emoji-list.html para ver en qué posición va. Una vez añadido, fusiona OK.

- Ejecuto uc_92_grupos_manual_1.py

- El fichero unicode_txt_manual_2.py se crea con util.py. util.py crea el fichero tmp_seleccion.py y hay que copiarlo en unicode_txt_manual_2.py. La verdad es que podría crearlo directamente.

- Ejecuto util.py pero me genera el mismo fichero que el año pasado porque tengo que añadir a mano en el programa los dibujos que no se ven.

- Ejecuto uc_11_generador.py y me genera las páginas.

- Compruebo que los nuevos emojis no se ven en W10 ni W11 y los añado en util.py. Ejecuto util.py. Copio a mano el contenido de tmp_seleccion.py en unicode_txt_manual_2.py. Ejecuto uc_11_generador.py y me genera las páginas.


## 2022-04-06

El 2022-03-31 publicaron Twemoji 14. He querido actualizar la página de Twemoji de los apuntes y ya no me acordaba de cómo funciona ;-(, así que voy a escribir aquí una chuleta.

- En ucdef.py está donde están los emojis de twemoji:
DIRECTORIO_TWEMOJI_ORIGINAL = "D:\\Descargas\\TWEMOJI\\twemoji-13-1-0-svg-210528\\assets\\svg"
y el fichero en el que se guarda esa información
FICHERO_MANUAL_1_TWEMOJI_ORIGINAL = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_1.py"
- En uc_92_grupos_manual_1.py la función incluye_emojis() crea el fichero FICHERO_MANUAL_1_TWEMOJI_ORIGINAL

- He cambiado el camino a
DIRECTORIO_TWEMOJI_ORIGINAL = "D:\\Descargas\\TWEMOJI\\twemoji-14-0-2-220331\\assets\\svg"
y he ejecutado uc_92_grupos_manual_1.py. Comparando con el fichero que generó a partir de twemoji 13 ha añadido un montón de svgs. Twemoji 14 tiene 112 svgs más que el 13 y al comparar los ficheros unicode_txt_manual_1.py con KDiff dice que hay 112 cambios, así que concuerda.
Ha creado también dos ficheros html-manual-1.html y html-manual-2.html donde se ven todos los emojis y se ve que no ha quedado ninguno por clasificar.

- Para generar la página web de los apuntes en ucdef.py está el nombre del fichero
FICHERO_SITIO_TWEMOJI_ORIGINAL = "html-unicode-twemoji.html"
que se usa en uc_11_generador.py
He ejecutado uc_11_generador.py y ha salido bien. De paso he detectado algunas erratas que había corregido al pasar el diccionario por los apuntes. He corregido las plantillas.
La página html-unicode-twemoji.html se genera con 112 dibujos más: 57 son caracteres y el resto secuencias (por cierto que me he dado cuenta que no cuenta el número de secuencias que hay en cada apartado, pero sí cuando son apartados de caracteres). Se genera un apartado nuevo: colores de piel (8).

Ha costado menos de lo que esperaba
