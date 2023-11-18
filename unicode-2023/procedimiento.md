
- Un lío que he arreglado en 2023-11-18 es que en los caracteres enmarcados (teclas), modo texto, no ponía los mensajes No disponible en W10/W11. No es fácil de arreglar porque en el código de la secuencia aparece U+23, pero tengo que conservar U+0023 (porque en twemoji en el nombre del fichero svg pone 23 pero en noto pone 0023). Al final como lo he resuelto es añadiendo en tmp.py tanto la versión U+23 como la versión U+0023. Así sí que pone los mensajes.

- Hago una copia de unicode_2 que he llamado unicode-2023

- Descargo los ficheros (Firefox &gt; Guardar como):
    - https://www.unicode.org/emoji/charts/full-emoji-list.html
    - https://www.unicode.org/emoji/charts/full-emoji-modifiers.html
    - https://unicode.org/Public/emoji/15.1/emoji-sequences.txt
    - https://unicode.org/Public/emoji/15.1/emoji-test.txt
    - https://unicode.org/Public/emoji/15.1/emoji-zwj-sequences.txt
    - https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-data.txt
    - https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-variation-sequences.txt
    - https://www.unicode.org/Public/15.1.0/ucd/extracted/DerivedName.txt
    ATENCIÓN. Los dos ficheros html son enormes y tardan en descargarse. Asegurarse de que se han descargado del todo antes de gurdarlos. En full-emoji-list 15 había 1874 emojis, en 15.1 hay 1902. En full-emoji-modifiers 15 había 1790 secuencias, en 15.1 hay 1880.

- En ucdef.py cambio las referencias a 15 por 15.1 y añado 15.1 en las listas uc_version, etc.
    ATENCIÓN. He corregido la lista uc_versiones_years en la que unos años estaban como números y otros como cadenas y además en el caso de 15 ponía 15, no 2022 (así que el title de la estrellita no ponía bien el año). Cuando la versión es X.1, el índice está puesto entre comillas. La verdad es que no sé si es necesario o no poner comillas si el índice no es entero.

- Ejecuto index.py
    - Ejecuto 1. OK
    - Ejecuto 2 y 3. OK. El número de celdas en la tabla no es el mismo, este año han quitado muchas imágenes de muestra, así que en fichero inicial es bastante más pqueño, pero el programa funciona OK
```
// Versión 15 emoji list
<tr><td class="rchars">1</td>
<td class="code"><a href="#1f600" name="1f600">U+1F600</a></td>
<td class="chars">😀</td>
<td class="andr alt"><img alt="😀" class="imga" src=""></td>
<td class="andr"><img alt="😀" class="imga" src=""></td>
<td class="andr alt"><img alt="😀" class="imga" src=""></td>
<td class="andr"><img alt="😀" class="imga" src=""></td>
<td class="andr alt"><img alt="😀" class="imga" src=""></td>
<td class="andr"><img alt="😀" class="imga" src=""></td>
<td class="andr alt"><img alt="😀" class="imga" src=""></td>
<td class="andr"><img alt="😀" class="imgs" src=""></td>
<td class="andr alt miss">—</td>
<td class="andr miss">—</td>
<td class="andr alt miss">—</td>
<td class="name">grinning face</td>
</tr>
// Versión 15.1 emoji list
<tr><td class="rchars">1</td>
<td class="code"><a href="#1f600" name="1f600">U+1F600</a></td>
<td class="chars">😀</td>
<td class="andr alt"><img alt="😀" class="imga" src=""></td>
<td class="andr"><img alt="😀" class="imgs" src=""></td>
<td class="andr alt miss">—</td>
<td class="andr miss">—</td>
<td class="andr alt miss">—</td>
<td class="name">grinning face</td>
</tr>
```
    - Ejecuto 4. pasa algo raro. La primera vez que lo ejecuto me dice varios errores (ERROR: campos distintos: person-symbol family, ERROR: c[1][3] NO es como c[2][5], ERROR: campos distintos: flag: Türkiye flag: Turkey, ERROR: c[1][5] NO es como c[2][3] y también Comprobando tipos de registros ... ERROR: Tipo distinto a los esperados ['1F642', '200D', '2194', 'FE0F'] [] ['fully-qualified', '🙂\u200d↔️', '15.1', 'head shaking horizontally', 'Smileys & Emotion', 'face-neutral-skeptical'] [] [] ['RGI_Emoji_ZWJ_Sequence', 'head shaking horizontally', '15.1', '🙂\u200d↔️', 'Other'] []). Para entender mejor el error he añadido {candidato} al mensaje de error en uc_4_ pero cuando lo he vuelto a ejecutar, me ha dicho que todo estaba bien. No lo entiendo, pero ocurre siempre. Si no existen los ficheros de salida, muestra los errores, pero si lo vuelvo a ejecutar, dice que todo está bien.
        NOTA. En 2022, al ejecutar index > 4 Fusionar listas Unicode me dice "subgrupo no esperado". Tengo que añadir en ucdef.py uc_subgroup el subgrupo "heart". Miro en full-emoji-list.html para ver en qué posición va. Una vez añadido, fusiona OK.
        ATENCION. Comparando los ficheros unicode_txt_fusionados_1 y 2 con los del año pasado parece que añade los nuevos, pero algunos de los que pone (como heavy plus sign y heavy minus sign y otros) no estaban el año pasado, aunque al final sí que aparecen en la página de emojis. No investigo más.
        ATENCION. En la función comprueba_fusion_1_2() había un montón de comprobaciones comentadas (9). las he descomentado, pero no ha salido ningún aviso. No sé qué es lo que hacen o si sirven para algo.

- Actualizo SVGs de Noto (el 17/11/2023 han publicado la versión Unicode 15.1). Descargo el repositorio completo y copio la carpeta svg en D:\Descargas\GOOGLE NOTO. En la carpeta svg hay un fichero LICENSE que tengo que borrar, porque en esa carpeta solo tiene que haber ficheros .svg.
- Ejecuto uc_92_grupos_manual_1.py para Twemoji
- Ejecuto uc_93_grupos_manual_1.py para Noto

- El fichero unicode_txt_manual_2.py se crea con util.py.
    NOTA. En 2023 he hecho que util.py cree drectamente unicode_txt_manual_2.py. El año pasado tenía que copiar a mano la salida de util.py.

- Ejecuto util.py pero me genera el mismo fichero que el año pasado porque tengo que añadir a mano en el programa los dibujos que no se ven.

- Comparo los archivos de /sitio del año pasado con lo que tengo colgado en los apuntes, por si he cambiado algo. En 2023 por ejemplo, tuve que cambiar el enlace a la licencia CC. Actualizar los archivos de /sitio-plantilla

- Buscar y sustituir "tabla de códigos de caracteres Unicode 15.0" por "tabla de códigos de caracteres Unicode 15.0" (en uc_11 y plantillas, hacer búsqeda en todo el directorio)

- En ucdef.py cambio uc_versiones_marcadas para incluir las versiones para las que quiero que ponga estrellitas en la ficha del emoji. En 2023 he puesto desde Unicode 13.
- Ejecuto uc_11_generador.py y me genera las páginas.
- ATENCIÓN. Me mosquea que al hacer uc_11 diga "Dibujos no existentes en Unicode:" 15 en noto y 30 en twemoji, pero no sé si es grave o no.

- ATENCIÓN. Cuando he llegado al final me he dado cuenta de que en ficheros_3_fusionados/html_manual_2.html salían 8 emojis pendientes de incluir. Resulta que son 8 símbolos alquímicos que incluyeron en Unicode 15. Resulta que en ucdef.py la lista uc_tablas_caracteres tiene los límites de valores y en alquímicos llegaba hasta "1F773", en vez de "1F77F". He repetido el proceso desde el principio y al hacer uc_92 y uc_93 ya no me dice Pendientes de clasificar: 8. Pero además también he tenido que añadirlos en
- ATENCIÓN. Me mosquea que al hacer uc_92 o uc_93 diga "Pertenecientes a varios grupos: 63", pero no sé si es grave o no.


- Compruebo que los nuevos emojis no se ven en W10 ni W11 y los añado en util.py. Ejecuto util.py. Ejecuto uc_11_generador.py y me genera las páginas.
- Reviso para ver si alguno de los que no se veían el año pasado ya se ven en Windows 11. Parece que los de Unicode 15 ya se ven.
- ATENCIÓN. 1. Si me olvido de poner la coma entre valores, se unen dos cadenas consecutivas y no salen los mensajes No disponible en W10/11. 2. Si se cuela un espacio dentro de la cadena tampoco sale. 3. Añadir a mano los códigos es una lata. Lo hago copiando de la página web final, pero es un coñazo. Debería añadir directamente los nuevos emojis de ese año.

