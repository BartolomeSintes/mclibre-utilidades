# DICICONARIO

Esta aplicación genera la lista de palabras que hay en los ficheros de un directorio. Lo quiero utilizar básicamente como corrector ortográfico pero también para revisar las clases utilizadas

## Gestión de diccionarios

-   2019-06-05. Listar las palabras que aparecen en varios diccionarios (tener en cuenta mayúsculas).
-   2019-06-05. Listar palabras que aparecen en un diccionario en varias formas mayusculas/minúsculas.
-   2019-06-05. Al salir, esta aplicación debería ordenar los diccionarios.

## Cosas por hacer

-   2019-05-31. Podría contar el número de ficheros a revisar y su tamaño y que vaya sacando cuántos lleva (en porcentaje).
-   2019-06-01. Que no trate bloques de comentarios (con /* o con &lt;!--).
-   2019-06-01. htmlParser se cuelga con algunos ficheros svg, js, etc.
-   2019-06-01. Podría hacer una pasada quitando todas las etiquetas y comentarios (con /* o con &lt;!--) y otra pasada mirando los atributos title.
-   2019-06-03. Otro análisis para hacer sería ver dónde se utilizan mayúsculas (para corregir dos myúsculas iniciales, por ejemplo).
-   2019-06-03. No tengo claro que la expresión regular que he puesto para eliminar bloques script no falle si hay un &lt; dentro del bloque.
-   2019-06-04. Si hay una palabra entre comillas debería quitar las comillas pero dejar la palabra.
-   2019-06-04. Repasar manualmente los diccionarios para aclarar qué va en cada uno.
-   2019-06-07. Que siga pidiendo tecla mientras no sea una de la lista.
-   2019-06-08. Opción para hacer revisión de diccionarios y que diga qué palabras ha encontrado (porque haya mejorado la eliminación y alguna excepeción ya no sea necesario).
-   2019-06-08. Opción para hacer test de regexp y que saque sólo las coincidencias.
-   2019-09-26. Opción para guardar una excepción para un archivo concreto. Por ejemplo un nombre de directorio sin acento (por ejemplo paginas en los apuntes de PHP).
-   2019-09-26. Cuando hay varias palabras unidas por guiones bajos podría partirla y preguntar por cada una de las partes.
-   2019-10-03. Hacer que en algunas palabras compruebe mayúsculas/minúsculas (nombre de países, etc.).
-   2020-07-01. No haría falta reordenar los diccionarios si no ha añadido ninguna palabra.
-   2021-11-12. El programa podría buscar si hay dos palabras iguales seguidas, que suelen ser errores (una puede llevar mayúsculas y la otra no).
-   2021-11-12. El programa podría buscar si hay errores de concordancia (artículos singulas seguidos de palabra en plural o viceversa). Esto no debe ser fácil.
-   2021-12-20. Podría buscar si hay alguna mayúscula que no esté al principio de una frase (descartando las palabras que en el diccionario empiecen con mayúscula). O las frase que después de un punto no tengan mayúscula.
-   2022-04-04. Podría buscar si hay algún espacio antes de un signo de puntuación (comas, puntos, puntos y comas, cierre de paréntesis). O si no hay espacios antes de abrir paréntesis
-   2023-02-17. Podría poder decirle que no mirara en ciertos directorios (en php /tmp, por ejemplo)
