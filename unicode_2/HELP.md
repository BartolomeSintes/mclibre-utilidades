# AYUDA

## 2022-04-06

El 2022-03-31 publicaron Twemoji 14. He querido actualizar la página de Twemoji de los apuntes y ya no me acordaba de cómo funciona ;-(, así que voy a escribir aquí una chuleta.

- En ucdef.py está donde están los emojis de twemoji:
DIRECTORIO_TWEMOJI = "D:\\Descargas\\TWEMOJI\\twemoji-13-1-0-svg-210528\\assets\\svg"
y el fichero en el que se guarda esa información
FICHERO_MANUAL_1 = UNICODE_FUSIONADOS_DIR + "unicode_txt_manual_1.py"
- En uc_92_grupos_manual_1.py la función incluye_emojis() crea el fichero FICHERO_MANUAL_1

- He cambiado el camino a
DIRECTORIO_TWEMOJI = "D:\\Descargas\\TWEMOJI\\twemoji-14-0-2-220331\\assets\\svg"
y he ejecutado uc_92_grupos_manual_1.py. Comparando con el fichero que generó a partir de twemoji 13 ha añadido un montón de svgs. Twemoji 14 tiene 112 svgs más que el 13 y al comparar los ficheros unicode_txt_manual_1.py con KDiff dice que hay 112 cambios, así que concuerda.
Ha creado también dos ficheros html-manual-1.html y html-manual-2.html donde se ven todos los emojis y se ve que no ha quedado ninguno por clasificar.

- Para generar la página web de los apuntes en ucdef.py está el nombre del fichero
FICHERO_SITIO_TWEMOJI = "html-unicode-twemoji.html"
que se usa en uc_11_generador.py
He ejecutado uc_11_generador.py y ha salido bien. De paso he detectado algunas erratas que había corregido al pasar el diccionario por los apuntes. He corregido las plantillas.
La página html-unicode-twemoji.html se genera con 112 dibujos más: 57 son caracteres y el resto secuencias (por cierto que me he dado cuenta que no cuenta el número de secuencias que hay en cada apartado, pero sí cuando son apartados de caracteres). Se genera un apartado nuevo: colores de piel (8).

Ha costado menos de lo que esperaba
