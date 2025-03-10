# LEGISLACIÓN INFORMÁTICA

Este repositorio contiene una colección legislativa de interés para profesores y alumnos de Informática.

## Urgentes

-   2021-12-26. Poner versión consolidada en todas las directivas. También lo tendría que hacer en las cosas del BOE y en el DOGV también tienen versiones consolidadas de algunas cosas. No tengo claro cómo gestiono las varias versiones de legislación consolidada en el json.

-   2021-12-26. Algunos RTF tiene tamaño 1 KB o 2KB. Es porque están vacíos o solo contienen el título. Debería descargarlos de nuevo o quitarlos.

-   2021-12-26. Poner enlaces https a DOGV. Poner enlaces permanentes eli a DOGV. <https://dogv.gva.es/es/projecte-eli-identificador-legislatiu-europeu>

-   2022-07-12. Unificar los ids de la legislación europea. En muchos casos utilizo la fecha, pero hay normas de la misma fecha, así que le añado un número de orden arbitrario (los pongo cuando me doy cuenta de que se repiten). Hoy creo que sería mejor usar el COM, que no se repite (aunque el COM se repite cuando son anexos y hay cosas que no tiene COM como los reglamentos de ejecución). Lo mejor sería usar el celex, pero es un número en el que no sé reconocer la fecha.

-   2022-07-12. Unificar las url de la legislación europea. En muchos casos pongo la url que pone cuando le das a l link a enlace pemanente de la página de eurlex, pero muchas veces en esa página también pone el eli. Debería poner el eli.

-   2022-07-12. Si no existen los ficheros el generador da error. Simplemente debería crearlos.

-   He añadido un campo comentario en la norma Conclusiones del Consejo sobre la ciberseguridad de los dispositivos conectados 2020/C 427/04. Debería añadirlo a todo para poder hacer anotaciones específicas (normalmente estará vacío).

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

-   2021-03-22. Las referencias de legislacion.json que no estaban incluidas en colecciones.json se añadían al final de otras.html, sin más explicaciones. Lo que he hecho es comentar las líneas de guarda_colecciones() que hacían eso. Ahora mismo, las únicas referencias en esa situación son los borradores de leyes ya aprobadas (boe-borrador-2019-1-rd). Y cuando genero el sitio, me muestra en pantalla qué referencias son. Si en el futuro la lista se hace muy larga, igual tendría que hacer un apartado de borradores, o una página que no estuviera enlazada con esas referencias para poderla mirar cuando hiciera falta.

- 2021-3-22. Me enviaron ayer un correo automático para decirme que había salido una nueva versión de EN 301 549. Hay una página que [informa de la versión](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=59546).

- 2021-12-23. No sé si ya lo tengo apuntado, pero debería chequear que no hay ids repetidos en legislacion.json, ni nombres de ficheros, ni urls.

## Otros

-   2019-11-30. Para localizar el permalink en los docv, escribir en google DOCV permalink ELI y el nombre de la referencia.

-   2009-12-01. Comunidad Valenciana. El diario oficial se llamó DOCV entre 2007 y 2016 [ref](https://valenciaplaza.com/el-docv-recupera-la-denominacion-de-generalitat-valenciana-desde-manana). Hay que tener cuidado con los nombres de los ficheros.

## Por incluir

-    ORDEN de 18 de junio de 1999, de la Conselleria de Cultura, Educación y Ciencia, por la que se regula la atención a la diversidad en la Educación Secundaria Obligatoria. <http://www.dogv.gva.es/datos/1999/06/29/pdf/1999_6082.pdf>

-   DECRETO 231/1997, de 2 de septiembre, del Gobierno Valenciano, por el que se regula la creación, estructura y funcionamiento de los Centros de Formación, Innovación y Recursos Educativos de la Comunidad Valenciana <http://www.dogv.gva.es/datos/1997/09/08/pdf/1997_10023.pdf>

-   LEY 12/1997, de 23 de diciembre, de Tasas de la Generalitat Valenciana. <http://www.dogv.gva.es/datos/1997/12/29/pdf/1997_4172.pdf>

-   ORDEN de 23 de julio de 1998, de la Conselleria de Cultura, Educación y Ciencia, por la que se fijan, implantan y cesan determinadas enseñanzas en los institutos y secciones de Educación Secundaria de la Comunidad Valenciana. <http://www.dogv.gva.es/datos/1998/09/09/pdf/1998_Q7241.pdf>

-   ORDEN de 3 de abril de 1998, de la Conselleria de Cultura, Educación y Ciencia, por la que se regula el procedimiento de admisión del alumnado en los centros de Educación Infantil, Educación Primaria y Educación Secundaria de la Comunidad Valenciana, sostenidos con fondos públicos <http://www.dogv.gva.es/datos/1998/04/08/pdf/1998_2708.pdf>

-   RESOLUCIÓN de 21 de mayo de 1998, de la Dirección General de Ordenación e Innovación Educativa y Política Lingüística, por la que se establecen normas para el cálculo de la nota media en el expediente académico del alumnado que solicita el acceso a enseñanzas universitarias de la Comunidad Valenciana desde la Formación Profesional. <http://www.dogv.gva.es/datos/1998/06/12/pdf/1998_4783.pdf>

-   ORDEN de 8 de julio de 1998 de la Conselleria de Cultura, Educación y Ciencia por la que se establece el proceso de implantacion de las enseñanzas de regimen general reguladas por la Ley Organica 1/1990 de Ordenacion General del Sistema Educativo y la progresiva extincion de las enseñanzas medias reguladas por la Ley General de Educación de 1970 en la Comunidad Valenciana.

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

-   [Guías de aplicación de las Normas Técnicas de Interoperabilidad (NTI)](https://www.anabad.org/guias-de-aplicacion-de-las-normas-tecnicas-de-interoperabilidad-nti-en-la-coleccion-administracion-electronica/)

-   ORDEN 4/2021, de 4 de febrero, del conseller de Educación, Cultura y Deporte, por el que se modifica la Orden 3/2020, de 6 de febrero, de la Consellería de Educación, Cultura y Deporte, por la que se determina la competencia lingüística necesaria para el acceso y el ejercicio de la función docente en el sistema educativo valenciano. https://dogv.gva.es/datos/2021/02/08/pdf/2021_1083.pdf

-   ORDEN 5/2021, de 12 de febrero, de la Conselleria de Educación, Cultura y Deporte, por la que se regulan el contenido, uso y acceso al expediente docente electrónico normalizado (EDEN), al servicio del sistema público educativo de la Generalitat. https://dogv.gva.es/datos/2021/02/17/pdf/2021_1347.pdf

-   ORDEN 3/2020, de 6 de febrero, de la Consellería de Educación, Cultura y Deporte, por la que se determina la competencia lingüística necesaria para el acceso y el ejercicio de la función docente en el sistema educativo valenciano. https://dogv.gva.es/datos/2020/02/10/pdf/2020_1131.pdf

## Dónde mirar referencias

-   <http://legislacioeducativa.blogspot.com/>

-   <http://bibliotecacefirevalencia.blogspot.com/search/label/Legislaci%C3%B3n>
    2022-02-26: He repasado del 2021-12-17 al 2022-02-25

-   <http://www.ceice.gva.es/es/web/centros-docentes/legislacion>

-   DOGV: [por materias](http://www.dogv.gva.es/es/legislacio-per-materies): -
    [Educación](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Educaci%C3%B3n&tit_materia=Educaci%C3%B3n) -
    [Accesibilidad](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Accesibilidad&tit_materia=Accesibilidad) -
    [Empleo y Formación Profesional](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Empleo%20y%20Formaci%C3%B3n%20profesional&tit_materia=Empleo%20y%20Formaci%C3%B3n%20profesional) -
    [Protección de datos](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Protecci%C3%B3n%20de%20datos&tit_materia=Protecci%C3%B3n%20de%20datos) -
    [Telecomunicaciones y nuevas tecnologías](http://www.dogv.gva.es/resultats-temes?&&L=1&tipo_search=legislacion&num_tipo=4&materia=Telecomunicaciones%20y%20nuevas%20tecnolog%C3%ADas&tit_materia=Telecomunicaciones%20y%20nuevas%20tecnolog%C3%ADas) -

-   <http://www.informatica-juridica.com/legislacion/espana/>

-   A veces el buscador no muestra el DOGV completo, pero esta dirección parece que sí: <http://www.dogv.gva.es/datos/1999/11/30/PortalSDLCAS.html>

- <https://algoquedaquedecir.blogspot.com/>. [Ratios en educación: normativa](http://algoquedaquedecir.blogspot.com/2018/12/ratios-en-educacion-normativa.html)

-   <https://www.csif.es/contenido/comunidad-valenciana/educacion/149216>

## Pendiente de incluir

-   <https://www.educacionyfp.gob.es/servicios-al-ciudadano/informacion-publica/audiencia-informacion-publica/abiertos/2021/pdr-evaluacion-promocion.html>

-   <https://www.educacionyfp.gob.es/servicios-al-ciudadano/informacion-publica/audiencia-informacion-publica/abiertos/2021/prd-cualificaciones-profesionales.html>

-   [Orden PRE/2740/2007, de 19 de septiembre, por la que se aprueba el Reglamento de Evaluación y Certificación de la Seguridad de las Tecnologías de la Información](https://www.boe.es/buscar/act.php?id=BOE-A-2007-16830)

-   [Common Criteria for Information Technology Security Evaluation](https://en.wikipedia.org/wiki/Common_Criteria)


## Ideas

-   2022-03-30. En los enlaces a versiones consolidadas, debería poner la fecha porque seguramente habrá versiones consolidadas posteriores.

-   2022-03-30. Tendría que revisar todos los enlaces para ver en qué casos hay versiones consolidadas y añadirlos o actualizarlos. Igual tendría que añadirlas en el websitewatcher para enterarme de las nuevas versiones actualizadas

-   2022-03-30. Otra cosa para revisar son los ficheros rtf de los dogv, que están vacíos en muchos casos.

-   2022-03-30. Otra cosa para revisar son los enlaces del dogv que ahora son https y los enlaces permanentes del dogv que me faltan en muchos casos.

-   2022-04-06. Tendría que poner dos campos más en legislacion.json, "fecha_derogación" y "derogado_por". No sé cómo tendría que llamarlo, porque además de derogadas, hay cosas vencidas que también se sustituyen unas a otras). Además, como hay cosas derogadas por dos (por ejemplo RD 1105/2014 está derogado por RD 217/2022 y por RD 243/2022), tendría que ser una lista. Puestos a soñar, algún día a partir de ahí podría hacer gráficas con las relaciones.

-   2022-04-06. Estaría bien que la información derogado por o sustituido por saliera en el propio cuadro, abajo, con enlace al otro.

-   2022-07-08. Al generar las páginas podría hacer la comprobación de campos repetidos, por ejemplo las "url" o el "id".

-   2022-07-16. Hay dogv para los que no hay rtf disponible. Podría hacer un programtia que los localizara y mostrara una página con enlaces para poder comprobar fácilmente si ya hay.

## legislación Europea

-   2022-07-13. He empezado a buscar con la búsqueda avanzada las Conclusiones del Consejo sobre temas educativas, año por año. He hecho hasta 2017
https://eur-lex.europa.eu/search.html?DTA=2017&SUBDOM_INIT=ALL_ALL&DTS_SUBDOM=ALL_ALL&textScope0=ti&DTS_DOM=ALL&lang=es&type=advanced&qid=1657292985931&andText0=%22Conclusiones+del+consejo%22&page=2

-   2022-12-30. Castilla La Mancha parece que es la primera comunidad que ha sacado el currículum del curso de especialización de Ciberseguridad: https://docm.jccm.es/docm/descargarArchivo.do?ruta=2022/07/18/pdf/2022_6692.pdf&tipo=rutaDocm

-   2023-01-27. Borradores Comunidad Valenciana https://stepv.intersindical.org/ensenyament_public/meses

-   2023-03-06. Artículo de xarxatic https://xarxatic.com/dudas-acerca-de-normativa-educativa-aqui-teneis-la-solucion/ sobre el sitio del MEC: https://educagob.educacionyfp.gob.es/ensenanzas.html

-   2023-03-06. La UE está aprobando más legislación relacionada con la seguridad informática.
    -   Chat Control 2 (Chat Control 1 es 2021/1232): https://www.theregister.com/2023/03/03/german_digital_committee_hearing_heaps/
    -   https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Links.html
        Al final de esta página hay enlaces a varias directivas, reglamentos, etc.
    -   https://www.nis-2-directive.com/
        Esta es una página parecida, pero hablando de la directiva NIS2
    -   https://eur-lex.europa.eu/eli/dir/2022/2557/oj
        Directiva (UE) 2022/2557 del Parlamento Europeo y del Consejo de 14 de diciembre de 2022 relativa a la resiliencia de las entidades críticas y por la que se deroga la Directiva 2008/114/CE del Consejo
    -   La propuesta de la CRA ha generado ruido:
        -   https://blog.nlnetlabs.nl/open-source-software-vs-the-cyber-resilience-act/
        -   https://blogs.eclipse.org/post/mike-milinkovich/cyber-resilience-act-good-intentions-and-unintended-consequences
        -   https://www.theregister.com/2022/09/16/eu_cyber_resilience_act/
        -   https://devclass.com/2023/01/24/eus-proposed-ce-mark-for-software-could-have-dire-impact-on-open-source/?td=rt-3a
        -   https://www.theregister.com/2023/01/30/opinion_eu_foss_security/
        -   Sesión en FOSDEM febrero 2023: https://fosdem.org/2023/schedule/event/cyber_resilience/
    -   https://ecommerce-europe.eu/news-item/the-european-commission-proposes-revision-of-the-product-liability-directive/
    -   https://ecommerce-europe.eu/news-item/european-commission-publishes-new-ai-liability-rules/
    -   https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206
        Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL LAYING DOWN HARMONISED RULES ON ARTIFICIAL INTELLIGENCE (ARTIFICIAL INTELLIGENCE ACT) AND AMENDING CERTAIN UNION LEGISLATIVE ACTS COM/2021/206 final
    -   https://www.europarl.europa.eu/doceo/document/TA-9-2023-0069_EN.pdf
        Data Act. Amendments adopted by the European Parliament on 14 March 2023 on the proposal for a regulation of the European Parliament and of the Council on harmonised rules on fair access to and use of data (Data Act) (COM(2022)0068 – C9-0051/2022 – 2022/0047(COD)

-   2023-03-31. https://xarxatic.com/recopilacion-de-articulos-acerca-de-legislacion-educativa/
-   2023-04-30. https://blog.cipi.es/blog2-intelectual/item/217-la-transposicion-de-las-directivas-de-la-ue-sobre-propiedad-intelectual
-   2023-04-30. https://digital-strategy.ec.europa.eu/en
-   2023-05-09. https://dgtic.gva.es/es/normativa tengo puesta alguna, pero no todas
-   2023-05-09. https://digital-strategy.ec.europa.eu/en/policies/cyber-solidarity visto en https://devclass.com/2023/04/28/brussels-greenlights-ai-act-chews-over-cyber-resilience-legislation/
-   2023-06-14. https://valenciaplaza.com/asi-funcionara-el-observatorio-de-la-inteligencia-artificial-de-la-comunitat-valenciana - https://dogv.gva.es/datos/2023/06/13/pdf/2023_6578.pdf - Un chiriguito inútil más
-   2023-06-15  https://xarxatic.com/dos-documentos-legales-que-como-docentes-de-la-publica-deberiais-tener-siempre-a-mano/ - https://www.boe.es/biblioteca_juridica/abrir_pdf.php?id=PUB-PB-2022-140
-   2023-06-29  https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-15051 - Orden EFP/694/2023, de 16 de junio, por la que se crean los departamentos didácticos de Informática y de Economía en los Institutos de Educación Secundaria de Ceuta y Melilla.
-   2024-06-05. Estudios nocturnos de Bachillerato
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1975-21701
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1976-16589
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1978-23730
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1985-25013
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1988-16731
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1975-8175
-   https://www.boe.es/diario_boe/txt.php?id=BOE-A-1972-1278
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1972-34
-   https://www.boe.es/diario_boe/txt.php?id=BOE-A-1971-936
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1975-16627
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1975-26270
-   https://www.boe.es/buscar/doc.php?id=BOE-A-1975-24066
-   Curso 2000/01, 1999/00, 1998/99: faltan instrucciones de inicio de curso, pero no las encontraba con Google o Bing, así que habría que ir día a día buscándolos en el DOGV de junio y julio (no cuesta tanto).
-   Real decreto aprobando el Reglamento provisional, que se inserta, para la aplicación del Estatuto de Enseñanza Industrial de 31 de Octubre de 1924, a las enseñanzas elementales y profesionales. https://www.boe.es/datos/pdfs/BOE//1925/283/A00146-00159.pdf
    Sale con otras cosas en https://www.boe.es/buscar/gazeta.php?campo%5B0%5D=ID_HIST&dato%5B0%5D=&campo%5B1%5D=TITULOS&dato%5B1%5D=&operador%5B1%5D=and&campo%5B2%5D=RNG.ID&dato%5B2%5D=&operador%5B2%5D=and&campo%5B3%5D=DEM.ID&dato%5B3%5D=&operador%5B3%5D=and&campo%5B4%5D=DOC&dato%5B4%5D=&operador%5B4%5D=and&campo%5B5%5D=TITULOS&dato%5B5%5D=real+decreto+aprobando+el+estatuto+de+ense%C3%B1anza+industrial&operador%5B5%5D=and&campo%5B6%5D=GAZ.ID&dato%5B6%5D=&campo%5B7%5D=NBO&dato%5B7%5D=&operador%5B8%5D=and&campo%5B8%5D=FPU&dato%5B8%5D%5B0%5D=&dato%5B8%5D%5B1%5D=&operador%5B9%5D=and&campo%5B9%5D=FAP&dato%5B9%5D%5B0%5D=&dato%5B9%5D%5B1%5D=&page_hits=50&sort_field%5B0%5D=FPU&sort_order%5B0%5D=desc&sort_field%5B1%5D=REF&sort_order%5B1%5D=asc&accion=Buscar

## Cosas a hacer periódicamente

-   Comprobar si la legislación más antigua está derogada (empezar por la más antigua vigente y avanzar hasta casi el final).
-   Actualizar las versiones consolidadas del BOE.
-   Comprobar si hay enlaces permanentes para DOGV.
-   Comprobar si hay ids repetidos o hay enlaces repetidos

## URGENTE

-   Los ELI del DOGV ya no van. Mirar en https://dogv.gva.es/es/eli para ver si hay una manera de reconvertirlos a los que hay ahora y redirigir los eli a enlaces no eli.

