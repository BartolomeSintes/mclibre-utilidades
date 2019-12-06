# LEGISLACIÓN INFORMÁTICA

Este repositorio contiene una colección legislativa de interés para profesores y alumnos de Informática.

## Cosas para hacer

-   2019-11-26. Incluir toda la legislación de interés para profesores de informática ;-)

-   2019-11-26. Validar el fichero json para que no tenga errores (ids duplicados, fechas incorrectas, etc.). Mirar si sirve [json-schema.org](https://json-schema.org/)

-   2019-11-26. Incluir un buscador para facilitar la consulta.

-   2019-11-26. Indicar de alguna manera la legislación "repetitiva" (órdenes de inicio de curso, etc.)

-   2019-11-26. Definir fragmentos de legislación para referenciarlos en FAQs o resúmenes de legislación.

-   2019-11-29. Algún fichero sale de tamaño 0.0 (por ejemplo: boe/BOE-2003-1128-RD-catalogo-cualificaciones.pdf, boe/BOE-2004-295-RD-catalogo-cualificaciones.pdf). Averiguar por qué

-   2019-11-29. Poner un distintivo en las últimas referencias añadidas o modificadas. El criterio podría ser que la fecha de inserción o modificación fuera inferior a una cantidad de días.

-   2019-11-29. Hacer alguna herramienta que compruebe si hay legislación consolidada o si hay legislación consolidada posterior y poder actualizar la información.

-   2019-11-29. Cuando un documento modifica o sustituye a otro, se podría incluir la referencia.

-   2019-11-30. Cosas a validar: que el json tenga la estructura que toca, que no se repitan las claves, que en las claves esté el origen y el tipo de ley y las categorías que vayamos definiendo, que no haya ids repetidos, que no haya enlaces o nombres de ficheros repetidos, que algunos valores sean uno los que pueden ser (ámbito: España, Unión Europea, Comunidad Valenciana, etc.), que los ids sigan el patrón, que el enlace a original y consolidado lleve o no el /com final, que los nombres de los ficheros lleven o no consolidado, que las fechas "fecha" y "original" coincidan, que las fechas "consolidados" sean posteriores a "original"

-   2019-11-30. He tenido que repetir la fecha de la referencia, en "fecha" para que ordene por fecha, y en "versiones"-"original" para que cada versión tenga fecha. No me acaba de buscar. Quizás podría hacer una función que extrajera la fecha de "original", pero no tengo claro si lo admitiría como criterio de ordenación (la función podría podría añadir ese dato al json en memoria y luego ordenar por él).

-   2019-11-30. El texto consolidado de DOCV Decreto 87/2015 tiene varios anexos en pdf que en el original estaban incluidos en el pdf de la norma.

-   2009-12-06. En las fichas podría poner un emoji para identificar la categoría (legislación, seguridad, protección de datos, etc.), al lado de la banderita.

## Otros

-   2019-11-30. Para localizar el permalink en los docv, escribir en google DOCV permalink ELI y el nombre de la referencia.

-   2009-12-01. Comunidad Valenciana. El diario oficial se llamó DOCV entre 2007 y 2016 [ref](https://valenciaplaza.com/el-docv-recupera-la-denominacion-de-generalitat-valenciana-desde-manana). Hay que tener cuidado con los nombres de los ficheros.

## Por incluir

-   DOGV Decreto 108/2012, de 29 de junio, del Consell, por el que se regula la recolocación y
redistribución del personal docente con destino definitivo en los centros docentes públicos no
universitarios.

-   Orden de 29 de junio de 1992, de la Conselleria de Cultura, Educación y Ciencia, por la que
se aprueban las instrucciones que regulan la organización y el funcionamiento de los centros
docentes que impartan enseñanzas de segundo ciclo de Educación Infantil, Preescolar, Primaria,
General Básica, Educación Especial, Secundaria Obligatoria, Bachillerato y Formación Profesional,
sostenidos con fondos públicos y dependientes de la Conselleria de Cultura, Educación y Ciencia de
la Generalitat Valenciana. (En vigor parcialmente)

-   <http://www.informatica-juridica.com/legislacion/espana/>
