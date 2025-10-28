# Procedimiento 2025

## Cosas pendientes

-   Tendría que tener una página de todos los símbolos que no tengo incluidos en la página de símbolos para que si se ven en Windows 11 o en Linux, incluirlos.

-   Renombrar los programas para que esté más claro el orden de ejecución. Tendría que hacer que estuvieran todos accesibles desde index.py.

-   El año pasado pensé que en vez de ordenar géneros y colores por longitud, podría organizarlos por combinación (poniendo primero las combinaciones sin selectores de presentación y luego los que sí), pero no termino de tener claro que valga la pena.

-   No entiendo por qué, en la página html-unicode-simbolos.html los apartados de emoticonos y de transporte y mapas no salen en su sitio. Se supone que salen por orden numérico, pero salen después de las formas geométricas extendidas. El resto salen bien.

-   Chrome tanto en W10 como en W11 saca algunas imágenes mal. Por ejemplo, en la página de símbolos, el U+26F9 (person with ball) la saca como emoji, no como texto. hay bastantes más. Tendría que confirmar que efectivamente el predeterminado es el modo texto. Y algunos no los saca, como U+23FE (power sleep symbol).

-   El grupo de Símbolos informáticos antiguos Chrome no los enseña en Windows 11, pero Firefox sí. En Windows 10 no los enseña ninguno de los dos.

-   Otra cosa rara En la página de géneros la secuencias U+1F3CB U+200D U+2640 U+FE0F (woman lifting weights) se ve en Chrome, pero no en Firefox. Hay más como woman detective y man detective.

-   En la página de Twemoji salen algunas caracteres y secuencias en las que no se ve el dibujo, lo que es absurdo. U+26F7 U+1F3FB, U+E50A, etc. Ya ocurría el año pasado. Las imágenes existen en el repositorio, pero o bien no están en la fuente que saca del CDN o bien Windows no se aclara sacando el carácter de la fuente. La solución podría ser hacer una lista de caracteres para los que debería mostrar la imagen en vez de la entidad numérica, que Windows parece no saber resolver auqnue el dibujo está en el repositorio.

## Procedimiento para añadir otra fuente de dibujos SVG

-   [2024-10-29] Añado el fork de Twemoji hecho por jdecked https://github.com/jdecked/twemoji

-   descargo el zip del repositorio y lo descomprimo en D:\Descargas

-   en udcdef.py duplico las referencias a TWEMOJI_ORIGINAL como TWEMOJI_JDECKED

-   creo uc_94 a partir de uc_92 para que cree el fichero unicode_txt_manual_1_twemoji_jdecked.py

-   en uc_11_generador.py añado una función para la página twemoji_jdecked

-   creo la plantilla html html-unicode-twemoji-jdecked

-   cuando paso el sitio a los apuntes de html, html-unicode-twemoji-jdecked.html lo renombro a html-unicode-twemoji.html

## Procedimiento a seguir para actualizar a nueva versión de Unicode

-   Hago una copia de unicode-2024 que he llamado unicode-2025

-   Descargo los ficheros (Firefox &gt; Guardar como):
    - https://www.unicode.org/emoji/charts/full-emoji-list.html
    - https://www.unicode.org/emoji/charts/full-emoji-modifiers.html
    - https://unicode.org/Public/17.0.0/emoji/emoji-sequences.txt
    - https://unicode.org/Public/17.0.0/emoji/emoji-test.txt
    - https://unicode.org/Public/17.0.0/emoji/emoji-zwj-sequences.txt
    - https://unicode.org/Public/17.0.0/ucd/emoji/emoji-data.txt
    - https://unicode.org/Public/17.0.0/ucd/emoji/emoji-variation-sequences.txt
    - https://unicode.org/Public/17.0.0/ucd/extracted/DerivedName.txt

    - Número de emojis (salen al hacer index.py opciones 2 y 3)
        | Fichero              | 15.0 | 15.1 | 16.0 | 17.0 |
        | full-emoji-list      | 1874 | 1902 | 1910 | 1918 |
        | full-emoji-modifiers | 1790 | 1880 | 1880 | 2035 |

-   En ucdef.py cambio las referencias a 16.0 por 17.0 y añado 17 en las listas uc_version, etc.
    Añado varias páginas de códigos. Reviso uc_tablas_caracteres, no sé por qué en algunos casos el rango que indico es el último dibujo y en otros, el último sitio disponible (sin ocupar). No lo unifico, pero el año que viene lo podría unificar al último hueco aunque esté sin ocupar (FF o lo que sea).
    Descargo Noto emoji main de https://github.com/googlefonts/noto-emoji
    Descargo Twemoji jdecked de https://github.com/jdecked/twemoji/releases
    No descargo Twemoji porque no se ha actualizado

-   Ejecuto index.py
    -   No hay que borrar los ficheros en ficheros_2_importados o ficheros_3_fusionados
    -   He cambiado ' por " en Full Emoji List, v16.0.htm y Full Emoji Modifier Sequences, v17.0.htm.
    -   He cambiado extensión FICHERO_EMOJI_FULL_LIST y FICHERO_FULL_EMOJI_MODIFIER_SEQUENCES_LIST de htmn a html.
    -   Ejecuto 1. OK
    -   Ejecuto 2 y 3. OK.
    -   Ejecuto 4.
        La primera vez que lo ejecuto salen errores raros del estilo
        -   Comprobando valores en lista fusionada ...
        -   hola 3790 3790 3790 [['1F6F3', 'FE0E'], [], [], [], ['text style', '7.0', 'passenger ship'], [], []]
        -   OK:c[1][2] es como c[2][4]
        -   ERROR: campos distintos: person walking facing right: light skin tone
        -   person walking facing right
        -   PROBLEMA: caracteres distintos
        -   ['1F6B6', '1F3FB', '200D', '27A1', 'FE0F'] person walking facing right person walking facing right: light skin tone

        El año pasado escribí con estos errores:
        -   Entiendo que en el primer sitio no está el tono de piel, pero como no entiendo qué hace el programa no sé cómo corregirlo.
        -   No sé ni lo que quiere decir este error

        Al final me dice:
        -   Comprobando tipos de registros ...
        -   ERROR: Tipo distinto a los esperados
        -   ['1FAEA']
        -   []
        -   ['fully-qualified', '\U0001faea', '17.0', 'distorted face', 'Smileys & Emotion', 'face-concerned']
        -   [['Emoji', 'Emoji_Presentation', 'Extended_Pictographic'], '17.0']
        -   []
        -   []
        -   ['Basic_Emoji', '17.0']
        y no me sale la lista OK. parece como si fuera un tipo (el número de cosas que hay en cada []) distinto.
        Pero la segunda vez que ejecuto 4 no sale ese error y dice
        OK: 5897 = 1193 + 207 + 1614 + 939 + 207 + 1065 + 137 + 535
        Dice bastante menos que el año pasado que decía OK: 6329 = 1186 + 207 + 1468 + 929 + 207 + 1045 + 752 + 535
        Lo ejecuto una tercera vez y sale un error como la primera pero con otro emoji. Lo ejecuto una cuarta y sale OK como la segunda (y genera los mismos ficheros).
        Así que me conformo con lo que sale.

    -   Actualizo SVGs de Noto (el 16/09/2025 han publicado la versión Unicode 17.0). Descargo el repositorio completo https://github.com/googlefonts/noto-emoji y copio la carpeta svg en D:\Descargas\GOOGLE NOTO. En la carpeta svg hay un fichero LICENSE que tengo que borrar, porque en esa carpeta solo tiene que haber ficheros .svg.
    -   Ejecuto uc_92_grupos_manual_1.py para Twemoji
        Salen avisos, pero como Twemoji no ha cambiado no hago nada.
        CUIDADO: HAY 44 DIBUJOS DE TWEMOJI QUE NO CORRESPONDEN A SECUENCIAS
        CUIDADO: HAY 63 EN VARIOS GRUPOS
    -   Ejecuto uc_93_grupos_manual_1.py para Noto
        Salen 2 avisos:
            CUIDADO: HAY 0 DIBUJOS DE NOTO
                     QUE NO CORRESPONDEN A SECUENCIAS
            CUIDADO: HAY 63 EN VARIOS GRUPOS
        Los 63 son de varios tipos.
        No hago nada con los 63 que seguramente son los mismos del año pasado.
    -   Ejecuto uc_94_grupos_manual_1.py para Twemoji jdecked
        Hay 5897 elementos. Ya clasificados en grupos: 5897 Pendientes de clasificar: 0 Pertenecientes a varios grupos:
        63
        CUIDADO: HAY 44 DIBUJOS DE TWEMOJI QUE NO CORRESPONDEN A SECUENCIAS
        CUIDADO: HAY 63 EN VARIOS GRUPOS
    -   Comparo los archivos de /sitio del año pasado con lo que tengo colgado en los apuntes, por si he cambiado algo en el html general (el head, etc.). Este año no hay cambios (pero cuidado porque la página que cuelgo como twemoji realmente es la de jdecked).
    -   Buscar y sustituir "tabla de códigos de caracteres Unicode 16.0" por "tabla de códigos de caracteres Unicode 17.0" (en uc_11 y plantillas, hacer búsqueda en todo el directorio)
    -   En ucdef.py cambio uc_versiones_marcadas para incluir las versiones para las que quiero que ponga estrellitas en la ficha del emoji. En 2023 puse desde Unicode 13 (que son las que no se ven en Windows 10). Este año lo he dejado igual.
    -   No sé cómo lo he hecho otros años, pero este año lo he hecho así:
        -   Ejecuto uc_11_generador.py y me genera las páginas. Las primeras veces la página Twemoji cascaba por un ídice fuera de rango, pero tras varias iteraciones de corregir otros fallos ha dejado de salir el error.
        -   Después de ejecutar por primera vez uc_11_generador.py, copio el archivo seleccion_simbolos.py y lo pego como seleccion_simbolos_manual.py
        -   Si hay grupos completos que no se ven, los quito de seleccion_simbolos_manual.py
        -   Si hay caracteres que son espacios o dibujos sin ningún interés, los quito de seleccion_simbolos_manual.py
        -   Miro las páginas en W10 y W11 y añado en util.py los códigos para que ponga los letreros "No disponible en Windows 10" o "No disponible en Windows 11". Parece que los de Unicode 15.1 ya se ven todos.
        -   Ejecuto util.py.
        -   Repito hasta que veo que está bien.

## Restos Procedimiento 2023

- Voy borrando los puntos de este apartado a medida que los voy pasando al apartado del 2024

- Un lío que he arreglado en 2023-11-18 es que en los caracteres enmarcados (teclas), modo texto, no ponía los mensajes No disponible en W10/W11. No parecía fácil de arreglar porque en el código de la secuencia aparece U+23, pero tengo que conservar U+0023 (porque en twemoji en el nombre del fichero svg pone 23 pero en noto pone 0023). Al final como lo he resuelto es añadiendo en tmp.py tanto la versión U+23 como la versión U+0023. Así sí que pone los mensajes.

* Procedimiento a seguir para actualizar a nueva versión de Unicode

- ATENCIÓN. Me mosquea que al hacer uc_11 diga "Dibujos no existentes en Unicode:" 15 en noto y 30 en twemoji, pero no sé si es grave o no.

- ATENCIÓN. Cuando he llegado al final me he dado cuenta de que en ficheros_3_fusionados/html_manual_2.html salían 8 emojis pendientes de incluir. Resulta que son 8 símbolos alquímicos que incluyeron en Unicode 15. Resulta que en ucdef.py la lista uc_tablas_caracteres tiene los límites de valores y en alquímicos llegaba hasta "1F773", en vez de "1F77F". He repetido el proceso desde el principio y al hacer uc_92 y uc_93 ya no me dice Pendientes de clasificar: 8. Pero además también he tenido que añadirlos en
- ATENCIÓN. Me mosquea que al hacer uc_92 o uc_93 diga "Pertenecientes a varios grupos: 63", pero no sé si es grave o no.

- ATENCIÓN. 1. Si me olvido de poner la coma entre valores, se unen dos cadenas consecutivas y no salen los mensajes No disponible en W10/11. 2. Si se cuela un espacio dentro de la cadena tampoco sale. 3. Añadir a mano los códigos es una lata. Lo hago copiando de la página web final, pero es un coñazo. Debería añadir directamente los nuevos emojis de ese año.

