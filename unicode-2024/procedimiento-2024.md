# Procedimiento 2024

## Cosas pendientes

-   Chrome tanto en W10 como en W11 saca algunas imágenes mal. Por ejemplo,m en la página de símbolos, el U+26F9 (person with ball) la saca como emoji, no como texto. hay bastantes más. Tendría que confirmar que efectivamente el predeterminado es el modo texto. Y algunos no los saca, como U+23FE (power sleep symbol).

-   El grupo de Símbolos informáticos antiguos Chrome no los enseña en Windows 11, pero Firefox sí. En Windows 10 no los enseña ninguno de los dos.

-   En la página de Twemoji salen algunas cosas que no se ve el dibujo, lo que es absurdo. U+26F7 U+1F3FB, U+E50A, etc. Ya ocurría el año pasado.

## Procedimiento a seguir para actualizar a nueva versión de Unicode

-   Hago una copia de unicode-2023 que he llamado unicode-2024

-   Descargo los ficheros (Firefox &gt; Guardar como):
    - https://www.unicode.org/emoji/charts/full-emoji-list.html
    - https://www.unicode.org/emoji/charts/full-emoji-modifiers.html
    - http://www.unicode.org/emoji/charts/emoji-sequences.html NO LO USO PARA NADA
    - https://unicode.org/Public/emoji/16.0/emoji-sequences.txt
    - https://unicode.org/Public/emoji/16.0/emoji-test.txt
    - https://unicode.org/Public/emoji/16.0/emoji-zwj-sequences.txt
    - https://www.unicode.org/Public/16.0.0/ucd/emoji/emoji-data.txt
    - https://www.unicode.org/Public/16.0.0/ucd/emoji/emoji-variation-sequences.txt
    - https://www.unicode.org/Public/16.0.0/ucd/extracted/DerivedName.txt

    - Número de emojis
        | Fichero              | 15.0 | 15.1 | 16.0 |
        | full-emoji-list      | 1874 | 1902 | 1910 |
        | full-emoji-modifiers | 1790 | 1880 | 1880 |

-   En ucdef.py cambio las referencias a 15.1 por 16.0 y añado 15.1 en las listas uc_version, etc.
    Añado varias páginas de códigos.

-   Ejecuto index.py
    -   No hay que borrar los ficheros en ficheros_2_importados o ficheros_3_fusionados
    -   He tenido que cambiar ' por " en Full Emoji List, v16.0.htm y Full Emoji Modifier Sequences, v16.0.htm. Los atributos el año pasado estaban delimitados por ' pero este año están con ".
    -   En uc_3_ he tenido que quitar dos &lt;/tbody&gt; que había en la búsqueda de la tabla dde caracteres para eliminar el texto posterior. Este año los ficheros Full Emoji List, v16.0.htm y Full Emoji Modifier Sequences, v16.0.htm no tiene tbody en las table.
    -   En unicode_txt_fusionados_1.py he tenido que cambiar mx claus por Mx Claus.
    -   Ejecuto 1. OK
    -   Ejecuto 2 y 3. OK.
    -   Ejecuto 4.
        Salen errores raros del estilo
        -   PROBLEMA: caracteres distintos ['1F6B6', '1F3FB', '200D', '2640', 'FE0F', '200D', '27A1', 'FE0F'] woman walking facing right woman walking facing right: light skin tone
            Entiendo que en el primer sitio no está el tono de piel, pero como no entiendo qué hace el programa no sé cómo corregirlo.
        -   hola 3790 3790 3700 [['1F6F3', 'FE0E'], [], [], [], ['text style', '7.0', 'passenger ship'], [], []] ERROR: c[1][5] NO es como c[2][3]
            No sé ni lo que quiere decir este error
        Pero como al final dice OK: 6329 = 1186 + 207 + 1468 + 929 + 207 + 1045 + 752 + 535 no hago nada.
        El año pasado también tenía errores raros, distintos a los de este año.
    -   Actualizo SVGs de Noto (el 06/10/2024 han publicado la versión Unicode 16.0). Descargo el repositorio completo https://github.com/googlefonts/noto-emoji y copio la carpeta svg en D:\Descargas\GOOGLE NOTO. En la carpeta svg hay un fichero LICENSE que tengo que borrar, porque en esa carpeta solo tiene que haber ficheros .svg.
    -   Ejecuto uc_92_grupos_manual_1.py para Twemoji
        Salen avisos, pero como Twemoji no ha cambiado no hago nada.
    -   Ejecuto uc_93_grupos_manual_1.py para Noto
        Salen 2 avisos:
            CUIDADO: HAY 15 DIBUJOS DE NOTO
                     QUE NO CORRESPONDEN A SECUENCIAS
            [['1F93C', '1F3FB'], 'emoji_u1f93c_1f3fb.svg']
            [['1F93C', '1F3FB', '200D', '2640'], 'emoji_u1f93c_1f3fb_200d_2640.svg']
            [['1F93C', '1F3FB', '200D', '2642'], 'emoji_u1f93c_1f3fb_200d_2642.svg']
            [['1F93C', '1F3FC'], 'emoji_u1f93c_1f3fc.svg']
            [['1F93C', '1F3FC', '200D', '2640'], 'emoji_u1f93c_1f3fc_200d_2640.svg']
            [['1F93C', '1F3FC', '200D', '2642'], 'emoji_u1f93c_1f3fc_200d_2642.svg']
            [['1F93C', '1F3FD'], 'emoji_u1f93c_1f3fd.svg']
            [['1F93C', '1F3FD', '200D', '2640'], 'emoji_u1f93c_1f3fd_200d_2640.svg']
            [['1F93C', '1F3FD', '200D', '2642'], 'emoji_u1f93c_1f3fd_200d_2642.svg']
            [['1F93C', '1F3FE'], 'emoji_u1f93c_1f3fe.svg']
            [['1F93C', '1F3FE', '200D', '2640'], 'emoji_u1f93c_1f3fe_200d_2640.svg']
            [['1F93C', '1F3FE', '200D', '2642'], 'emoji_u1f93c_1f3fe_200d_2642.svg']
            [['1F93C', '1F3FF'], 'emoji_u1f93c_1f3ff.svg']
            [['1F93C', '1F3FF', '200D', '2640'], 'emoji_u1f93c_1f3ff_200d_2640.svg']
            [['1F93C', '1F3FF', '200D', '2642'], 'emoji_u1f93c_1f3ff_200d_2642.svg']
            CUIDADO: HAY 63 EN VARIOS GRUPOS
        Los 15 dibujos que no corresponden a secuencias son parejas de luchadores.
        Los 63 son de varios tipos.
        No hago nada ni con unos ni con otros.
    -   Comparo los archivos de /sitio del año pasado con lo que tengo colgado en los apuntes, por si he cambiado algo en el html general (el head, etc.). Este año no hay cambios.
    -   Buscar y sustituir "tabla de códigos de caracteres Unicode 15.1" por "tabla de códigos de caracteres Unicode 16.0" (en uc_11 y plantillas, hacer búsqueda en todo el directorio)
    -   En ucdef.py cambio uc_versiones_marcadas para incluir las versiones para las que quiero que ponga estrellitas en la ficha del emoji. En 2023 puse desde Unicode 13.
    -   No sé cómo lo he hecho otros años, pero este año lo he hecho así:
        -   Copio el archivo seleccion_simbolos.py y lo pego como seleccion_simbolos_manual.py
        -   Ejecuto uc_11_generador.py y me genera las páginas. Las primeras veces la página Twemoji cascaba por un ídice fuera de rango, pero tras varias iteraciones de corregir otros fallos ha dejado de salir el error.
        -   Si hay grupos completos que no se ven, los quito de seleccion_simbolos_manual.py
        -   Si hay caracteres que son espacios o dibujos sin ningún interés, los quito de seleccion_simbolos_manual.py
        -   Miro las páginas en W10 y W11 y añado en util.py los códigos para que ponga los letreros "No disponible en Windows 10" o "No disponible en Windows 11".
        -   Repito hasta que veo que está bien.

## Restos Procedimiento 2023

- Voy borrando los puntos de este apartado a medida que los voy pasando al aparatado del 2024

- Un lío que he arreglado en 2023-11-18 es que en los caracteres enmarcados (teclas), modo texto, no ponía los mensajes No disponible en W10/W11. No parecía fácil de arreglar porque en el código de la secuencia aparece U+23, pero tengo que conservar U+0023 (porque en twemoji en el nombre del fichero svg pone 23 pero en noto pone 0023). Al final como lo he resuelto es añadiendo en tmp.py tanto la versión U+23 como la versión U+0023. Así sí que pone los mensajes.

* Procedimiento a seguir para actualizar a nueva versión de Unicode

- Ejecuto uc_11_generador.py y me genera las páginas.
- ATENCIÓN. Me mosquea que al hacer uc_11 diga "Dibujos no existentes en Unicode:" 15 en noto y 30 en twemoji, pero no sé si es grave o no.

- ATENCIÓN. Cuando he llegado al final me he dado cuenta de que en ficheros_3_fusionados/html_manual_2.html salían 8 emojis pendientes de incluir. Resulta que son 8 símbolos alquímicos que incluyeron en Unicode 15. Resulta que en ucdef.py la lista uc_tablas_caracteres tiene los límites de valores y en alquímicos llegaba hasta "1F773", en vez de "1F77F". He repetido el proceso desde el principio y al hacer uc_92 y uc_93 ya no me dice Pendientes de clasificar: 8. Pero además también he tenido que añadirlos en
- ATENCIÓN. Me mosquea que al hacer uc_92 o uc_93 diga "Pertenecientes a varios grupos: 63", pero no sé si es grave o no.

- Compruebo que los nuevos emojis no se ven en W10 ni W11 y los añado en util.py. Ejecuto util.py. Ejecuto uc_11_generador.py y me genera las páginas.
- Reviso para ver si alguno de los que no se veían el año pasado ya se ven en Windows 11. Parece que los de Unicode 15 ya se ven todos.
- ATENCIÓN. 1. Si me olvido de poner la coma entre valores, se unen dos cadenas consecutivas y no salen los mensajes No disponible en W10/11. 2. Si se cuela un espacio dentro de la cadena tampoco sale. 3. Añadir a mano los códigos es una lata. Lo hago copiando de la página web final, pero es un coñazo. Debería añadir directamente los nuevos emojis de ese año.

