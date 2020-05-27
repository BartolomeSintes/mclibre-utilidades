# LEGISLACIÓN INFORMÁTICA

Este repositorio contiene una colección legislativa de interés para profesores y alumnos de Informática.

## Errores

-   2020-05-20. Al final de Otros temas pone el borrador de ciberseguridad que no está en ningún apartado.

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

-   2019-12-06. En las fichas podría poner un emoji para identificar la categoría (legislación, seguridad, protección de datos, etc.), al lado de la banderita.

-   2019-12-06. Hacer un formulario para que me puedan enviar nuevas referencias

-   2019-12-08. Hacer que colecciones.json pueda definir subapartados.

-   2019-12-08. Hacer seguimiento de otras páginas para enterarme de novedades.

-   2019-12-08. Añadir enlace de descarga del repositorio completo. En algún momento podría preparar zips temáticos que estuvieran en mclibre (o publicarlas en github).

-   2019-12-10. Como en las revistas, la fecha del pie de página tendría que ser la fecha más tardía de las normas de la página.

-   2020-02-08. Chequear que id/origenurl coincide en docv o dogv, boe, etc.

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

-   DECRETO 39/1998, de 31 de marzo, del Gobierno Valenciano, de ordenación de la educación para la atención del alumnado con necesidades educativas especiales <https://www.dogv.gva.es/es/eli/es-vc/d/1998/03/31/39/> y todo lo que lo modifica

-   ORDEN 26/2016, de 13 de junio, de la Conselleria de Educación, Investigación, Cultura y Deporte, por la que se regula el programa de reutilización, reposición y renovación de libros de texto y material curricular, ... <https://www.dogv.gva.es/es/eli/es-vc/o/2016/06/13/26/>

-   <http://participacio.gva.es/es/web/delegacion-de-proteccion-de-datos-gva/criteris-i-recomanacions> Aunque no esté publicado en el DOGV, sería interesante incluir estas guías.

## Dónde mirar referencias

-   <http://bibliotecacefirevalencia.blogspot.com/search/label/Legislaci%C3%B3n>

-   <http://www.ceice.gva.es/es/web/centros-docentes/legislacion>

-   DOGV: [por materias](http://www.dogv.gva.es/es/legislacio-per-materies): -
    [Educación](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Educaci%C3%B3n&tit_materia=Educaci%C3%B3n) -
    [Accesibilidad](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Accesibilidad&tit_materia=Accesibilidad) -
    [Empleo y Formación Profesional](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Empleo%20y%20Formaci%C3%B3n%20profesional&tit_materia=Empleo%20y%20Formaci%C3%B3n%20profesional) -
    [Protección de datos](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Protecci%C3%B3n%20de%20datos&tit_materia=Protecci%C3%B3n%20de%20datos) -
    [Telecomunicaciones y nuevas tecnologías](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Telecomunicaciones%20y%20nuevas%20tecnolog%C3%ADas&tit_materia=Telecomunicaciones%20y%20nuevas%20tecnolog%C3%ADas) -

-   <http://www.informatica-juridica.com/legislacion/espana/>
