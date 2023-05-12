# GENERADOR DOCUMENTACIÓN

Esta aplicación genera el sitio web https://www.mclibre.org/consultar/documentacion/

## Cosas para hacer

-   2019-06-13. Tamaños de los pdfs salen en MB, hacer que salgan en KB si es inferior a 1 MB.
-   2019-06.14. Añadiir en paginas.json el país de origen de cada revista.
-   2019-06-14. La función ordena sólo funciona si reversed=True, me falta corregir si reversed=False.
-   2019-06-14. No ordena por idioma (por ejemplo, para que ponga antes la versión en inglés y luego en español).
-   2019-06-14. Añadir un campo para explicaciones adicionales (p.e. Aprender para Educar tiene números posteriores que no puedo descargar y Occam's Razor ya no saca pdfs).
-   2019-06-15. En la primera línea de las páginas dice siempre "de la revista" pero cuando son recopilaciones debería decir "recopilaciones de la revista".
-   2019-06-15. Hay recopilaciones de MagPi que no tiene número.
-   2019-07-04. Podría hacer una función para enlazar unos json con otros para sustituir los bucles que hay en varios sitios.
-   2019-07-04. No ordena bien los números cuando pasan de unidad (por ejemplo Wirefremae 2019).
-   2019-07-05. En la versión antigua de las revistas inactivas salía el país. La información está en revistas.json, y la uso en las páginas individuales, pero no en la de páginas inactivas. Tendría que poner el país como campo y si tiene valor, utilizarlo al generar la página. En la página de revistas inactivas genero los años automáticamente, podría hacer lo mismo en las páginas individuales de revistas inactivas. También podría generar un párrafo que dijera se publicó entre fecha y fecha.
-   2019-07-06. Generar index.html. Incluir contadores: en años, revistas y ejemplares, en revistas, ejemplares y años de publicación (desde XXXX para activas o XXXX-YYYY para inactivas).
-   2019-07-10. Repasar los enlaces a las páginas web y sustituir los enlaces rotos por enlaces a archive.org. Podría añadir rel="nofollow" y sacar del enlace el paréntesi que dice que es un enlace a la copia de archive.org.
-   2019-07-27. En la portada, al decir el número de ejemplares si hay versión en español cuenta el doble. Pasa en Odroid, por ejemplo.
-   2019-07-28. En la portada, las imágenes de las revistas inactivas podrían sacarse al azar, para que no fueran siempre las mismas.
-   2019-10-11. En la portada, las revistas inactivas podrían estar ordenadas por la antigüedad del último número.
-   2019-12-04. Hay revistas bimensuales (como Solo WordPress), pero el programa sólo escribe un mes.
-   2019-12-04. En los cuadros no pone el nombre de la revista. Debería ponerlo, porque no se puede buscar en la página escribiendo el nombre.
-   2020-05-24. Podría poner flechas para pasar de un año al siguiente y al anterior, o de una revista a la siguiente o a la anterior
-   2022-03-03. The Python Papers está desaparecido. Me podría dedicar a bajar los pdfs de archive.org y preparar los pdfs https://web.archive.org/web/20180819045931/http://ojs.pythonpapers.org/index.php/tpp/issue/archive. He guardado un artículo en revistas/, además de un python rag que he encontrado.
-   2023-02-10. En este repositorio <https://gitlab.com/sirtetris/ubunchu-translation> que he encontrado mirando <https://groups.google.com/g/ubunchu-translators> hay jpg de los número 9 a 14 (n sé si está todo). Podría hacer yo el pdf a partir de las imágenes, pero no tengo claro el copyright de estos números y es sospenchos que nadie lo haya publicado en pdf.
-   2023-02-10. En las revistas JOLTS que tengo colgadas faltan artículos que están sueltos en la web. Tendría que descargarlos y unirlos con PDFsam.

## Revistas para incluir

-   Buscador de revistas: <http://agora.edu.es/>
-   Revista CTS: <http://www.revistacts.net/>
-   Barbecho: <http://www.barbecho.uma.es/> (Revista antigua)
-   Aula de innovación educativa: <https://www.grao.com/es/productos/revistas>
-   Comunicar: <https://www.revistacomunicar.com/index.php?idioma=es>
-   Red Seguridad: <https://www.redseguridad.com/kiosko-pro/>
-   Kilobyte Magazine: <https://retro.wtf/kilobytemagazine/>
-   e-ducadores del mundo <https://e-ducadores.org/revista/2022/12/29/la-cuarta-edicion/> Es continuación de Aprender para educar, pero de 4 revistas solo he podido descargar en pdf 2 de ellas.
-   Revista TINO <https://revista.jovenclub.cu/numeros-de-tino/> hay 86 números, desde el 2007. No parece gran cosa, pero están todos los pdfs en <https://revista.jovenclub.cu/revista-tino-pdf/>
-   El predecesor de The R Journal se llamaba R news y hay varios años de revista en <https://www.r-project.org/doc/Rnews/index.html>
-   The Internet Protocol Journal <https://ipj.dreamhosters.com/internet-protocol-journal/issues/back-issues/>
-   Supervisión21 publicación de la Unión Sindical de Inspectores de Educación, https://usie.es/supervision21/index.php/Sp21/issue/archive

## Libros para incluir

-   https://www.systemsapproach.org/books.html
-   https://www.raspberrypi.org/research/publications/
    https://www.raspberrypi.org/app/uploads/2021/11/Teaching-programming-in-schools-pedagogy-review-Raspberry-Pi-Foundation.pdf
    https://www.raspberrypi.org/app/uploads/2021/05/Understanding-computing-education-Volume-1-Raspberry-Pi-Foundation-Research-Seminars.pdf
    https://www.raspberrypi.org/blog/research-report-teaching-programming/
-   https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-es.md

