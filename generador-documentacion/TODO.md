# GENERADOR DOCUMENTACIÓN

Esta aplicación genera el sitio web http://www.mclibre.org/consultar/documentacion/


# Cosas para hacer
* 2019-06-13. Que compruebe que los ficheros de plantillas en ORIGEN y los nombres de las páginas en PAGINA coinciden.
* 2019-06-13. La fecha de creación de cada página la tendría que poner a partir las fechas de creación de los registros).
* 2019-06-13. Tamaños de los pdfs salen en MB, hacer que salgan en KB si es inferior a 1 MB.
* 2019-06.14. Añadiir en paginas.json el país de origen de cada revista
* 2019-06-14. Mirando la fecha de las imágenes de las portadas puedo ver cuándo he añadido cada revista.
* 2019-06-14. El formato de los documentos lo puedo sacar de la extensión. No hace falta que sea una clave.
* 2019-06-14. la función ordena sólo funciona si reversed=True, me falta corregir si reversed=False
* 2019-06-14. No ordena por idioma (por ejemplo, para que ponga antes la versión en inglés y luego en español).
* 2019-06-14. Añadir un campo para explicaciones adicionales (p.e. Aprender para Educar tiene números posteriores que no puedo descargar y Occam's Razor ya no saca pdfs).
* 2019-06-14. Odroid magazine tiene dos páginas web (versión inglesa y española) http://magazine.odroid.com/es/
* 2019-06-15. En la primera línea de las páginas dice siempre "de la revista" pero cuando son recopilaciones debería decir "recopilaciones de la revista"
* 2019-06-15. Hay recopilaciones de MagPi que no tiene número
* 2019-06-15. the-magpi-essentials-C-01-en-201610.pdf tiene la C en mayúsculas
* 2019-07-04. Podría hacer una función para enlazar unos json con otros para sustituir los bucles que hay en varios sitios
* 2019-07-04 Gimp magazine no sale bien ordenado en revistas-inactivas.html