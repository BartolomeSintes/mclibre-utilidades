# DICICONARIO

Esta aplicación genera la lista de palabras que hay en los ficheros de un directorio. Lo quiero utilizar básicamente como corrector ortográfico pero también para revisar las clases utilizadas


# Gestión de diccionarios
* 2019-06-05. Listar las palabras que aparecen en varios diccionarios (tener en cuenta mayúsculas).
* 2019-06-05. Listar palabras que aparecen en un diccionario en varias formas mayusculas/minúsculas.
* 2019-06-05. Al salir, esta aplicación debería ordenar los diccionarios.


## Cosas por hacer
* 2019-05-31. Podría contar el número de ficheros a revisar y su tamaño y que vaya sacando cuántos lleva (en porcentaje).
* 2019-06-01. Que no trate bloques de comentarios (con /* o con &lt;!--).
* 2019-06-01. htmlParser se cuelga con algunos ficheros svg, js, etc.
* 2019-06-01. Podría hacer una pasada quitando todas las etiquetas y comentarios (con /* o con &lt;!--) y otra pasada mirando los atributos title.
* 2019-06-03. Otro análisis para hacer sería ver dónde se utilizan mayúsculas (para corregir dos myúsculas iniciales, por ejemplo).
* 2019-06-03. No tengo claro que la expresión regular que he puesto para eliminar bloques script no falle si hay un &lt; dentro del bloque.

* 2019-06-04. Si hay una palabra entre comillas debería quitar las comillas pero dejar la palabra.
* 2019-06-04. Repasar manualmente los diccionarios para aclarar qué va en cada uno.
* 2019-06-07. Que siga pidiendo tecla mientras no sea una de la lista.
* 2019-06-08. Opción para hacer revisión de diccionarios y que diga qué palabras ha encontrado (porque haya mejorado la eliminación y alguna excepeción ya no sea necesario).
* 2019-06-08. Opción para hacer test de regexp y que saque sólo las coincidencias.
* 2019-09-26. Opción para guardar una excepción para un archivo concreto. Por ejemplo un nombre de directorio sin acento (por ejemplo paginas en los apuntes de PHP).
* 2019-09-26. Cuando hay varias palabras unidas por guinoes bajos podría partirla y preguntar por cada una de las partes.
* 2019-10-03. Hacer que en algunas palabras compruebe mayúsculas/minúsculas (nombre de países, etc.).
