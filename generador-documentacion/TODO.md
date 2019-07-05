# GENERADOR DOCUMENTACIÓN

Esta aplicación genera el sitio web http://www.mclibre.org/consultar/documentacion/


# Cosas para hacer
* 2019-06-13. Tamaños de los pdfs salen en MB, hacer que salgan en KB si es inferior a 1 MB.
* 2019-06.14. Añadiir en paginas.json el país de origen de cada revista
* 2019-06-14. La función ordena sólo funciona si reversed=True, me falta corregir si reversed=False
* 2019-06-14. No ordena por idioma (por ejemplo, para que ponga antes la versión en inglés y luego en español).
* 2019-06-14. Añadir un campo para explicaciones adicionales (p.e. Aprender para Educar tiene números posteriores que no puedo descargar y Occam's Razor ya no saca pdfs).
* 2019-06-15. En la primera línea de las páginas dice siempre "de la revista" pero cuando son recopilaciones debería decir "recopilaciones de la revista"
* 2019-06-15. Hay recopilaciones de MagPi que no tiene número
* 2019-06-15. the-magpi-essentials-C-01-en-201610.pdf tiene la C en mayúsculas
* 2019-07-04. Podría hacer una función para enlazar unos json con otros para sustituir los bucles que hay en varios sitios
* 2019-07-04. No ordena bien los números cuando pasan de unidad (por ejemplo Wirefremae 2019)
* 2019-07-05. En la versión antigua de las revistas inactivas salía el país. La información está en revistas.json, y la uso en las páginas individuales, pero no en la de páginas inactivas. Tendría que poner el país como campo y si tiene valor, utilizarlo al generar la página. En la página de revistas inactivas genero los años automáticamente, podría hacer lo mismo en las páginas individuales de revistas inactivas.