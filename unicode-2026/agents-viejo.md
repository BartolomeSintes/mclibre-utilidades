

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

