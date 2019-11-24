# GENERADOR EJERCICIOS HTMLCSS

Esta aplicación genera ejercicios de html/css.

Partiendo de una página completa con todo tipo de elementos y propiedades, va eliminando los elementos hasta dejar un fichero con sólo texto.

El archivo de configuración ejericcios.json contiene toda la información necesaria:

-   steps: las etiquetas html y las propiedades css están agrupadas por temas (steps). En cada uno se definen las cosas obligatorias (compulsory), optativas (optional) y no utilizadas (unused).

-   step sets: define grupos de temas ordenados. El orden es el orden en que se irán eliminando las etiquetas (se eliminan en orden inverso al que aparecen).

-   exercises: define los páginas completas (nombre, nombre del directorio, ficheros html, css, img y webfonts que lo forman)

-   exercise sets: define grupos de ejercicios para ser tratados de una tacada. Para cada ejercicio incluido en el grupo, se indica si quieren utilizar sólo los elementos obligatorios o también los optativos y los pasos a incluir.

Al ejecutar el programa, muestra los exercise sets definidos y pide elegir uno. Los procesa creando una carpeta para cada ejercicio que contiene las carpetas de los steps elegidos y una carpeta con la plantilla final (comprime la plantilla)

