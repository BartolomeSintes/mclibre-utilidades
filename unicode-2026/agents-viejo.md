

## 2026-10-17
- util.py crea el fichero ucdef.FICHERO_MANUAL_2 a partir de las listas win_10 y win_11. Quiero que cree el fichero ucdef.FICHERO_ELIMINADOS a partir de la lista uc_eliminados.
- Quiero que uc_11_generador.py al generar las páginas de /sitio no incluya los caracteres o secuencias incluidas en ucdef.FICHERO_MANUAL_2
- El formato de ucdef.FICHERO_MANUAL_2 puede ser similar al de unicode_txt_manual_1_noto.py por ejemplo (es decir, separando los caracteres que forman la secuencia).

- Perdón, me he equivocado. Te he dicho uqe quería que uc_11_generador.py al generar las páginas de /sitio no incluya los caracteres o secuencias incluidas en ucdef.FICHERO_MANUAL_2 y en realidad quería decir el fichero ucdef.FICHERO_ELIMINADOS

- En Windows 11 con Chrome, en html-unicode-simbolos.html el caracter U+261D se ve como emoji, no como texto, pero en Firefox se ve como texto. ¿Qué navegador lo está haciendo bien?
- Pasa lo mismo con U+26F9, U+270C, U+270D, U+1F3CB, U+1F3CC, U+1F590. ¿Puedes chequear quién lo está haciendo bien en cada caso?
Claude dice que quién lo hace bien es Firefox

- util.py tiene que compobar si los elementos de la lista uc_chrome no están incluido en la lista uc_firefox. Si hay alguno, el programa debe listar todos los que están y detenese.
- util.py tiene que compobar si los elementos de win_11 no están incluido en la lista uc_chrome o en la lista uc_firefox. Si hay alguno, el programa debe listar todos los que están y detenerse.

- No, el error tiene que mostrarse si algún elemento de uc_chrome está en uc_firefox. Y tiene que mostrar todos los que coinciden.
- No, el error tiene que mostrarse si algún elemento de win_11 está en uc_firefox o en uc_chrome. Y tiene que mostrar todos los que coinciden.

- util.py crea actualmente la lista manual_2 a partir de las listas win_10 y win_11. Quiero que en esa lista primero incluya los elementos que hay en uc_firefox y en uc_chrome, en ese orden. El mensaje a incluir en el caso de los elementos de uc_firefox es "No disponible en Firefox". El mensaje a incluir en el caso de los elementos de uc_chrome es "No disponible en Chrome".


## 2026-10-18

-   Quiero que en las páginas html creadas por uc_11_generador.py sólo se incluyan secuencias fully-qualified. Se trataría de eliminar las secuencias que no sea fully-qualified. No tengo claro si el mejor lugar para hacerlo es en el propio uc_11_generador.oy o si sería mejor hacerlo en uc_1_importa_unicode.py antes de guardar FICHERO_IMPORTADO (unicode_txt_importados.py). ¿Qué te parece?

-   Puedes hacer que uc_11_generador.py no importe seleccion_simbolos_manual.py y en su lugar utilice seleccion_simbolos.py (o los datos que exporta en seleccion_simbolos.py)?

- Sustituye en uc_11_generador.py y el resto de programas .py las referencias explícitas a ficheros por su nombre por las constantes definidas en ucdef.py? Por ejemplo uc_11_generador.py importa unicode_txt_derived_name cuando en ucdef.py FICHERO_UNICODE reperesenta el mismo fichero.

## 2026-10-20

El programa uc_11_grupos_manual_1_twemoji.py está escrito para ser llamado directamente desde el terminal. Quiero que se pueda llamar desde index.py eligiendo la opción 11.

Haz lo mismo con uc_12_grupos_manual_1_noto.py, uc_13_grupos_manual_twemoji_jdecked.py, uc_21_util.py y uc_22_generador.py

He modificado uc_11_grupos_manual_1_twemoji.py, uc_12_grupos_manual_1_noto.py y uc_13_grupos_manual_twemoji_jdecked.py de manera que a los elementos que se asignaba el grupo gr-genero-2 se le asigne el grupo gr-genero-1, pero ahora al ejecutar uc_22_generador.py da el error:
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\index.py", line 61, in <module>
    main()
    ~~~~^^
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\index.py", line 55, in main
    uc_22.main()
    ~~~~~~~~~~^^
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\uc_22_generador.py", line 1473, in main
    contenido=genera_pagina(pagina[0]), fecha=fecha
              ~~~~~~~~~~~~~^^^^^^^^^^^
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\uc_22_generador.py", line 100, in genera_pagina
    return genera_pagina_secuencias(pagina, ucdef.uc_grupos_generos)
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\uc_22_generador.py", line 1325, in genera_pagina_secuencias
    caracteres = ordena(caracteres, grupo[3])
  File "D:\_Carpetas_frecuentes\Documentos\_MCLibre.org\Actual\consultar\utilidades\unicode-2026\uc_22_generador.py", line 1273, in ordena
    cs += [cs2[i]]
           ~~~^^^
IndexError: list index out of range

¿Por qué? ¿Se puede corregir?

Lo que quiero es que si antes ordenaba hombre/mujer ahora quiero que ordene neutro/hombre/mujer. ¿Es eso lo que has hecho?


He modificado uc_11_grupos_manual_1_twemoji.py, uc_12_grupos_manual_1_noto.py y uc_13_grupos_manual_twemoji_jdecked.py de manera que a los elementos que se asignaba los grupos  gr-genero-3 y gr-genero-5 se le asigne el grupo gr-genero-2. ¿Puedes cambiar uc_22_generador.py para que los ordene en el orden neutro(hombre/mujer?

Hay dos problemas: las secuencias U+1F9D1 U+200D U+1F9D2 y U+1F9D1 U+200D U+1FA70 se clasifican como gr-genero-1 cuando no corresponden a ese grupo porque no hay secuencias similares neutro/hombre/mujer. ¿Podrías añadir condiciones para esos dos casos particulares en uc_11_grupos_manual_1_twemoji.py, uc_12_grupos_manual_1_noto.py y uc_13_grupos_manual_twemoji_jdecked.py?
 U+1F9D1 U+200D U+1FA70 lo dejo en gr-genero-1 y U+1F9D1 U+200D U+1F9D2 lo clasifico como gr-familias-4

Por qué en html-unicode-noto.html no hay ninguna secuencia de los grupos gr-genero-2, gr-genero-3, o gr-genero-4?

Me puedes dar un ejemplo de secuencia de 2 códigos con FE0F (371) que siguen sin dibujo en Noto?

Pero en la página html-unicode-noto.html quiero que los emojis que tienen forma predeterminada texto en la ficha aparezca con U+FE0F, que es la manera correcta de referirse al emoji. ¿Eso cómo se podría hacer?



Quiero que uc_22_generador.py al generar html-unicode-secuencias-generos.html ordene los elementos gr-colores-piel-2 de manera que se muestren los 15 emojis de cada profesión en este orden: primero los 5 emojis hechos a partir del emoji adulto (de claro a oscuro), depsués los cinco hechos a partir del emoji hombre (de claro a oscuro) y por último los 5 hecho a partir del emoji mujer.


