import json
import pathlib
from datetime import date
import gconst
import gjson


def fecha_a_texto(numero):
    return (
        str(int(numero[8:10]))
        + " de "
        + gconst.MES[int(numero[5:7])]
        + " de "
        + str(numero[0:4])
    )


def bandera(entidad, ancho):
    return f'<img src="../{gconst.DIR_IMAGES}/bandera-{gconst.CODIGOS_ISO_3166[entidad]}.svg" alt="{entidad}" title="{entidad}" width="{ancho}">'


def cabecera(titulo, profundidad, incluye_js):
    tmp = "<!DOCTYPE html>\n"
    tmp += '<html lang="es">\n'
    tmp += "<head>\n"
    tmp += '  <meta charset="utf-8">\n'
    tmp += f"  <title>{titulo}</title>\n"
    tmp += '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    if profundidad == 0:
        tmp += f'  <link rel="stylesheet" href="{gconst.FILE_CSS}">\n'
        tmp += f'  <link rel="icon" href="varios/favicon.ico">\n'
    else:
        tmp += f'  <link rel="stylesheet" href="../{gconst.FILE_CSS}">\n'
        tmp += f'  <link rel="icon" href="../varios/favicon.ico">\n'
    if incluye_js:
        tmp += '  <script>\n'
        tmp += '    function filtra() {\n'
        tmp += '      var checks = {\n'
        tmp += '        "disposicion": true,\n'
        tmp += '        "origen-ue": document.getElementById("origen-ue").checked,\n'
        tmp += '        "origen-es": document.getElementById("origen-es").checked,\n'
        tmp += '        "origen-es-tm": document.getElementById("origen-es-tm").checked,\n'
        tmp += '        "origen-es-cv": document.getElementById("origen-es-cv").checked,\n'
        tmp += '        "vigencia-borrador": document.getElementById("vigencia-borrador").checked,\n'
        tmp += '        "vigencia-vigente": document.getElementById("vigencia-vigente").checked,\n'
        tmp += '        "vigencia-derogado": document.getElementById("vigencia-derogado").checked,\n'
        tmp += '        "vigencia-vencido": document.getElementById("vigencia-vencido").checked,\n'
        tmp += '      };\n'
        tmp += '      var elementos = document.getElementsByClassName("disposicion");\n'
        tmp += '      for (var i = 0; i < elementos.length; i++) {\n'
        tmp += '        listaClases = elementos[i].classList;\n'
        tmp += '        elementos[i].style.display = "flex";\n'
        tmp += '        for (var j = 0; j < listaClases.length; j++) {\n'
        tmp += '          if (!checks[listaClases[j]]) {\n'
        tmp += '            elementos[i].style.display = "none";\n'
        tmp += '            cuenta--;\n'
        tmp += '          }\n'
        tmp += '        }\n'
        tmp += '      }\n'
        tmp += '      var cuenta = 0;\n'
        tmp += '      for (var i = 0; i < elementos.length; i++) {\n'
        tmp += '        if (elementos[i].style.display == "flex") {\n'
        tmp += '          cuenta++;\n'
        tmp += '        }\n'
        tmp += '      }\n'
        tmp += '      document.getElementById("contador").innerHTML = cuenta;\n'
        tmp += '    }\n'
        tmp += '\n'
        tmp += '    window.addEventListener("load", filtra);\n'
        tmp += '  </script>\n'

    tmp += "</head>\n"
    tmp += "\n"
    tmp += "<body>\n"
    tmp += f"  <h1>{titulo}</h1>\n"
    tmp += "\n"

    if profundidad == 0:
        tmp += '  <p><a href="https://github.com/BartolomeSintes/mclibre-legislacion"><img style="position: absolute; top: 0; right: 0; border: 0; opacity: 0.7;" src="varios/iconos/fork-me-on-github.png" alt="Fork me on GitHub"></a></p>\n'

    tmp += "\n"

    if profundidad == 0:
        tmp += '  <nav class="portada">\n'
        tmp += "    <p>\n"
        tmp += '      <a href="https://www.mclibre.org/"><img src="varios/iconos/icono-logo-mclibre.svg" alt="Logotipo www.mclibre.org" title="Material Curricular Libre - www.mclibre.org" width="144" height="76"></a>\n'
        tmp += "    </p>\n"
        tmp += "\n"
    else:
        tmp += "  <nav>\n"
        tmp += "    <p>\n"
        tmp += '      <a href="../index.html"><img src="../varios/iconos/icono-legislacion.svg" alt="Índice" title="Ir al Índice" width="48" height="48"></a>\n'
        tmp += '      <a href="#"><img src="../varios/iconos/icono-arrow-circle-up.svg" alt="Principio de la página" title="Principio de la página" width="36" height="36"></a>\n'
        tmp += "    </p>\n"
        tmp += "\n"
        tmp += '    <div class="toc">\n'
        tmp += '      <h2><a href="../index.html">Legislación</a></h2>\n'
        tmp += "\n"
        tmp += "      <ul>\n"
        tmp += '        <li><a href="cronologico.html">Orden Cronológico</a></li>\n'
        tmp += "        <li>Educativa (vigente)\n"
        tmp += "          <ul>\n"
        tmp += '            <li><a href="educativa-eu.html">Unión Europea</a></li>\n'
        tmp += '            <li><a href="educativa-es.html">España</a></li>\n'
        tmp += "            <li>Comunidades Autónomas:\n"
        tmp += "              <ul>\n"
        tmp += '                <li><a href="educativa-es-vc.html">Comunidad Valenciana</a></li>\n'
        tmp += '                <li><a href="educativa-es-min.html">Territorio MEC</a></li>\n'
        tmp += "              </ul>\n"
        tmp += "            </li>\n"
        tmp += "          </ul>\n"
        tmp += "        </li>\n"
        tmp += '        <li><a href="otras.html">Otros temas (vigente)</a></li>\n'
        tmp += "        <li>Educativa (derogada/vencida)\n"
        tmp += "          <ul>\n"
        tmp += '            <li><a href="educativa-derogada-eu.html">Unión Europea</a></li>\n'
        tmp += '            <li><a href="educativa-derogada-es.html">España</a></li>\n'
        tmp += '            <li><a href="educativa-derogada-es-cv.html">Comun. Valenc. derogada</a></li>\n'
        tmp += '            <li><a href="educativa-derogada-anual-es-cv.html">Comun. Valenc. vencida</a></li>\n'
        tmp += '            <li><a href="educativa-derogada-es-min.html">Territorio MEC</a></li>\n'
        tmp += "          </ul>\n"
        tmp += "        </li>\n"
        tmp += '        <li><a href="otras-derogada.html">Otros temas (derog./venc.)</a></li>\n'
        tmp += "      </ul>\n"
        tmp += "    </div>\n"
    tmp += "  </nav>\n"
    tmp += "\n"
    if incluye_js:
        tmp += '  <table>\n'
        tmp += '    <tr>\n'
        tmp += '      <td colspan="5">Mostrar / Ocultar referencias:</td>\n'
        tmp += '    </tr>\n'
        tmp += '    <tr>\n'
        tmp += '      <td>Origen:</td>\n'
        tmp += '      <td><label><input type="checkbox" name="origen-ue" id="origen-ue" checked onclick="filtra()">Unión Europea</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="origen-es" id="origen-es" checked onclick="filtra()">España</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="origen-es-tm" id="origen-es-tm" checked onclick="filtra()">Territorio MEC</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="origen-es-cv" id="origen-es-cv" checked onclick="filtra()">Comunidad Valenciana</label></td>\n'
        tmp += '    </tr>\n'
        tmp += '    <tr>\n'
        tmp += '      <td>Vigencia:</td>\n'
        tmp += '      <td><label><input type="checkbox" name="vigencia-borrador" id="vigencia-borrador" checked onclick="filtra()">Borrador</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="vigencia-vigente" id="vigencia-vigente" checked onclick="filtra()">Vigente</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="vigencia-derogado" id="vigencia-derogado" checked onclick="filtra()">Derogado</label></td>\n'
        tmp += '      <td><label><input type="checkbox" name="vigencia-vencido" id="vigencia-vencido" checked onclick="filtra()">Vencido</label></td>\n'
        tmp += '    </tr>\n'
        tmp += '  </table>\n'
        tmp += "\n"

    return tmp


def seccion(legislacion, identificador, titulo):
    tmp = f'  <section id="{identificador}">\n'
    tmp += f"    <h2>{titulo}</h2>\n"
    tmp += "\n"
    tmp += f'    <div class="disposiciones">\n'
    for elemento in legislacion:
        tmp += f'      <article class="disposicion'
        tmp += f' {elemento["ámbito"]}'
        tmp += f' {elemento["vigencia"]}'
        tmp += f'" id="{elemento["id"]}">\n'
        tmp += f'        <h3>{elemento["descripción"]}</h3>\n'
        tmp += f'        <p class="publicacion">\n'
        tmp += f'          {bandera(elemento["ámbito"], 25)}\n'
        tmp += f'          {elemento["origen"]} {elemento["fecha"]}\n'
        if elemento["vigencia"] == gconst.DEROGADO:
            tmp += f'          <span class="derogado">derogado</span>\n'
        elif elemento["vigencia"] == gconst.VENCIDO:
            tmp += f'          <span class="derogado">vencido</span>\n'
        tmp += "        </p>\n"
        for version in elemento["versiones"]:
            tmp += '        <p class="fichero">\n'
            if len(elemento["versiones"]) != 1:
                tmp += f'        {version["versión"][:1].upper() + version["versión"][1:]}: '
            for i in range(len(version["enlaces"])):
                if version["enlaces"][i]["formato"] == "memoria":
                    file = pathlib.Path(
                        f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                    )
                    weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                    formato = file.suffix[1:].upper()
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += f'          <a href="{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria</a>'
                    else:
                        tmp += f'          <a href="{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria({version["enlaces"][i]["idioma"].upper()})</a>'
                elif version["enlaces"][i]["formato"] != "web":
                    file = pathlib.Path(
                        f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                    )
                    weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                    formato = file.suffix[1:].upper()
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += f'          <a href="{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}</a>'
                    else:
                        tmp += f'          <a href="{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}({version["enlaces"][i]["idioma"].upper()})</a>'
                else:
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += f'          <a href="{version["enlaces"][i]["url"]}">web</a>'
                    else:
                        tmp += f'          <a href="{version["enlaces"][i]["url"]}">web({version["enlaces"][i]["idioma"].upper()})</a>'
                if i < len(version["enlaces"]) - 1:
                    tmp += " -\n"
                else:
                    tmp += "<br>\n"
            tmp += "        </p>\n"
        tmp += f'        <p class="titulo">{elemento["titulo"]}</p>\n'
        tmp += "      </article>\n"
        tmp += "\n"
    tmp += f"    </div>\n"
    tmp += "  </section>\n"
    tmp += "\n"
    return tmp


def cronologico(legislacion):
    tmp = ""
    tmp += f'  <div class="disposiciones">\n'
    for elemento in legislacion:
        tmp += f'    <article class="disposicion'
        if elemento["ámbito"] == "Unión Europea":
            tmp += ' origen-ue'
        elif elemento["ámbito"] == "España":
            tmp += ' origen-es'
        elif elemento["ámbito"] == "Comunidad Valenciana":
            tmp += ' origen-es-cv'
        elif elemento["ámbito"] == "Ministerio de Educación":
            tmp += ' origen-es-tm'
        else:
            tmp += ' origen-xxx'

        if elemento["vigencia"] == "borrador":
            tmp += ' vigencia-borrador'
        elif elemento["vigencia"] == "vigente":
            tmp += ' vigencia-vigente'
        elif elemento["vigencia"] == "derogado":
            tmp += ' vigencia-derogado'
        elif elemento["vigencia"] == "vencido":
            tmp += ' vigencia-vencido'
        else:
            tmp += ' vigencia-xxx'
        tmp += f'" id="{elemento["id"]}">\n'
        tmp += f'      <h3>{elemento["descripción"]}</h3>\n'
        tmp += f'      <p class="publicacion">\n'
        tmp += f'        {bandera(elemento["ámbito"], 25)}\n'
        tmp += f'        {elemento["origen"]} {elemento["fecha"]}\n'
        if elemento["vigencia"] == gconst.DEROGADO:
            tmp += f'        <span class="derogado">derogado</span>\n'
        elif elemento["vigencia"] == gconst.VENCIDO:
            tmp += f'        <span class="derogado">vencido</span>\n'
        tmp += "      </p>\n"
        for version in elemento["versiones"]:
            tmp += '      <p class="fichero">\n'
            if version["versión"] == "borrador":
                tmp += f'        <img src="../{gconst.DIR_IMAGES}/en-construccion.svg" alt="Borrador" title="Borrador" width="25">'
                tmp += '<span class="derogado">borrador</span>\n'
            if len(elemento["versiones"]) != 1:
                tmp += (
                    f'        {version["versión"][:1].upper() + version["versión"][1:]}:\n'
                )
            for i in range(len(version["enlaces"])):
                if version["enlaces"][i]["formato"] == "memoria":
                    file = pathlib.Path(
                        f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                    )
                    weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                    formato = file.suffix[1:].upper()
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += f'        <a href="../{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria</a>'
                    else:
                        tmp += f'        <a href="../{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria({version["enlaces"][i]["idioma"].upper()})</a>'
                elif version["enlaces"][i]["formato"] != "web":
                    file = pathlib.Path(
                        f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                    )
                    weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                    formato = file.suffix[1:].upper()
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += f'        <a href="../{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}</a>'
                    else:
                        tmp += f'        <a href="../{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}({version["enlaces"][i]["idioma"].upper()})</a>'
                else:
                    if version["enlaces"][i]["idioma"] == "es":
                        tmp += (
                            f'        <a href="{version["enlaces"][i]["url"]}">web</a>'
                        )
                    else:
                        tmp += f'        <a href="{version["enlaces"][i]["url"]}">web({version["enlaces"][i]["idioma"].upper()})</a>'
                if i < len(version["enlaces"]) - 1:
                    tmp += " -\n"
                else:
                    tmp += "<br>\n"
            tmp += "      </p>\n"
        tmp += f'      <p class="titulo">{elemento["titulo"]}</p>\n'
        tmp += "    </article>\n"
        tmp += "\n"
    tmp += f"    </div>\n"
    tmp += "\n"
    return tmp


def pie():
    tmp = "\n"
    tmp += "  <footer>\n"
    tmp += f"    <p>Última modificación de esta página: {fecha_a_texto(str(date.today()))}</p>\n"
    tmp += "  </footer>\n"
    tmp += "</body>\n"
    tmp += "</html>\n"
    return tmp


def muestra_referencia(elemento, profundidad):
    if profundidad == 0:
        camino = ""
    else:
        camino = "../"
    tmp = ""
    tmp += f'    <li class="disposicion" id="{elemento["id"]}">\n'
    tmp += f'      <strong class="descripcion">{elemento["descripción"]}</strong><br>\n'
    tmp += f'      <span class="titulo">{elemento["titulo"]}</span><br>\n'
    if elemento["vigencia"] == gconst.DEROGADO:
        tmp += f'      <span class="derogado">derogado</span><br>\n'
    elif elemento["vigencia"] == gconst.VENCIDO:
        tmp += f'          <span class="derogado">vencido</span><br>\n'
    tmp += f'      <span class="publicacion">\n'
    for version in elemento["versiones"]:
        tmp += '        <span class="fichero">\n'
        if len(elemento["versiones"]) == 1:
            tmp += f'          {elemento["origen"]} {elemento["fecha"]}:\n'
        elif version["versión"] == "original" or version["versión"] == "anexo":
            tmp += f'        {version["versión"][:1].upper() + version["versión"][1:]}: {elemento["origen"]} {elemento["fecha"]}:\n'
        else:
            tmp += f'        {version["versión"][:1].upper() + version["versión"][1:]} ({version["fecha"]}):\n'

        for i in range(len(version["enlaces"])):
            if version["enlaces"][i]["formato"] == "memoria":
                file = pathlib.Path(
                    f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                )
                weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                formato = file.suffix[1:].upper()
                if version["enlaces"][i]["idioma"] == "es":
                    tmp += f'          <a href="{camino}{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria</a>'
                else:
                    tmp += f'          <a href="{camino}{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">Memoria({version["enlaces"][i]["idioma"].upper()})</a>'
            elif version["enlaces"][i]["formato"] != "web":
                file = pathlib.Path(
                    f'{gconst.DIR_SITE}/{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}'
                )
                weight = str(round(file.stat().st_size / 1024 / 1024, 1)) + " MB"
                formato = file.suffix[1:].upper()
                if version["enlaces"][i]["idioma"] == "es":
                    tmp += f'          <a href="{camino}{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}</a>'
                else:
                    tmp += f'          <a href="{camino}{gconst.DIR_FILES}/{version["enlaces"][i]["url"]}" title="{weight}">{formato}({version["enlaces"][i]["idioma"].upper()})</a>'
            else:
                if version["enlaces"][i]["idioma"] == "es":
                    tmp += f'          <a href="{version["enlaces"][i]["url"]}">web</a>'
                else:
                    tmp += f'          <a href="{version["enlaces"][i]["url"]}">web({version["enlaces"][i]["idioma"].upper()})</a>'
            if i < len(version["enlaces"]) - 1:
                tmp += " -\n"
            else:
                tmp += "\n"
        tmp += "        </span><br>\n"
    tmp += "      </span>\n"
    tmp += "    </li>\n"
    tmp += "\n"
    return tmp


def guarda_fichas(eliminar):
    # Carga json
    with open(gconst.JSON_FILE_REFERENCES, encoding="utf-8") as file:
        tmp = json.load(file)
    legislacion = gjson.ordena(tmp, "fecha", True)["legislacion"]

    print(f"Hay {len(legislacion)} referencias.")

    for ref in eliminar:
        for i in range(len(legislacion)-1,-1,-1):
            if legislacion[i]["id"] == ref:
                del legislacion[i]

    print(f"Se muestran en las páginas {len(legislacion)} referencias.")

    # Genera índice
    t = ""
    t += "\n"
    t += cabecera("Legislación informática - Orden cronológico", 1, 1)

    t += f'  <p>Esta página muestra las <span id="contador">{len(legislacion)}</span> referencias legislativas de este repositorio en orden cronológico inverso.</p>\n'
    t += "\n"

    t += cronologico(legislacion)

    # Ahora saco todas las fichas juntas, sin ordenar por grupos, como hice al principio
    # grupo = gjson.selecciona(legislacion, "ámbito", "Unión Europea")
    # grupo = gjson.selecciona(grupo, "vigencia", "vigente")
    # t += seccion(grupo, "ue", "Legislación Unión Europea")

    # grupo = gjson.selecciona(legislacion, "ámbito", "España")
    # grupo = gjson.selecciona(grupo, "vigencia", "vigente")
    # t += seccion(grupo, "es", "Legislación Española")

    # grupo = gjson.selecciona(legislacion, "ámbito", "Comunidad Valenciana")
    # grupo = gjson.selecciona(grupo, "vigencia", "vigente")
    # t += seccion(grupo, "es-cv", "Legislación Comunidad Valenciana")

    # grupo = gjson.selecciona(legislacion, "vigencia", "derogado")
    # t += seccion(grupo, "derogada", "Legislación derogada")

    t += pie()
    with open(
        f"{gconst.DIR_SITE}/{gconst.FILE_FICHAS}", "w", encoding="utf-8"
    ) as fichero:
        fichero.write(t)


def guarda_index(restos):
    # Carga json legislación
    with open(gconst.JSON_FILE_REFERENCES, encoding="utf-8") as file:
        tmp = json.load(file)
    legislacion = gjson.ordena(tmp, "fecha", False)["legislacion"]

    ids = [d["id"] for d in legislacion]

    t = ""
    t += cabecera("Legislación Informática", 0, 0)

    t += '  <p style="margin-right: 50px">Este sitio web recopila legislación relacionada con la Informática. Se trata en su mayor parte de legislación '
    t += "relacionada con la enseñanza, pero también contiene legislación relacionada con otros temas (protección de datos, seguridad, etc.).</p>\n"
    t += "\n"
    t += f"  <p>Este sitio web contiene {len(ids) - len(restos)} referencias, distribuidas en varias páginas:</p>\n"
    t += "  <ul>\n"
    t += '        <li><a href="listados/cronologico.html">Todas las referencias en orden cronológico inverso</a></li>\n'
    t += "        <li>Legislación Educativa vigente\n"
    t += "          <ul>\n"
    t += '            <li><a href="listados/educativa-eu.html">Unión Europea</a></li>\n'
    t += '            <li><a href="listados/educativa-es.html">España</a></li>\n'
    t += "            <li>Comunidades Autónomas:\n"
    t += "              <ul>\n"
    t += '                <li><a href="listados/educativa-es-vc.html">Comunidad Valenciana</a></li>\n'
    t += '                <li><a href="listados/educativa-es-min.html">Territorio MEC</a></li>\n'
    t += "              </ul>\n"
    t += "            </li>\n"
    t += "          </ul>\n"
    t += "        </li>\n"
    t += '        <li><a href="listados/otras.html">Legislación Informática vigente (no educativa)</a></li>\n'
    t += "        <li>Legislación Educativa derogada o vencida\n"
    t += "          <ul>\n"
    t += '            <li><a href="listados/educativa-derogada-eu.html">Unión Europea</a></li>\n'
    t += '            <li><a href="listados/educativa-derogada-es.html">España</a></li>\n'
    t += '            <li><a href="listados/educativa-derogada-es-cv.html">Comunidad Valenciana derogada</a></li>\n'
    t += '            <li><a href="listados/educativa-derogada-anual-es-cv.html">Comunidad Valenciana vencida</a></li>\n'
    t += '            <li><a href="listados/educativa-derogada-es-min.html">Territorio MEC</a></li>\n'
    t += "          </ul>\n"
    t += "        </li>\n"
    t += '        <li><a href="listados/otras-derogada.html">Legislación Informática derogada o vencida (no educativa)</a></li>\n'
    t += "  </ul>\n"
    t += "\n"
    t += "  <p>Para facilitar su consulta, los textos legales se ofrecen en varios formatos:</p>\n"
    t += "  <ul>\n"
    t += "    <li>enlace web a la página de la publicación original (EUR-LEX, BOE, DOGV, etc.)</li>\n"
    t += "    <li>en formato PDF</li>\n"
    t += "    <li>en su caso, en otros formatos editables (RTF, etc.)</li>\n"
    t += "  </ul>\n"
    t += "\n"
    t += "  <p>En algunos casos se ofrecen también las versiones consolidadas de las normas, que no tienen valor jurídico.</p>\n"
    t += "\n"

    t += pie()

    with open(
        f"{gconst.DIR_SITE}/{gconst.FILE_INDEX}", "w", encoding="utf-8"
    ) as fichero:
        fichero.write(t)


def guarda_colecciones(nombre):
    # Carga json legislación
    with open(gconst.JSON_FILE_REFERENCES, encoding="utf-8") as file:
        tmp = json.load(file)
    legislacion = gjson.ordena(tmp, "fecha", False)["legislacion"]

    ids = [d["id"] for d in legislacion]
    print(f"Hay {len(ids)} referencias")

    # Carga json colecciones
    with open(gconst.JSON_FILE_COLLECTIONS, encoding="utf-8") as file:
        tmp_file = json.load(file)
    coleccion = gjson.selecciona_en_json(tmp_file["colecciones"], "nombre", nombre)

    for pagina in coleccion["paginas"]:
        t = ""
        t += cabecera(pagina["titulo"], pagina["profundidad"], 0)
        # t += '  <p><a href="fichas.html">Versión en forma de fichas</a></p>\n'
        # t += "\n"
        cuenta = gjson.cuenta_referencias_en_coleccion(pagina)
        t_intro = pagina["introducción"]
        t += t_intro.replace("NNN", f"{cuenta}")
        # 2022-06-29 He quitado el if else porque ninguna página va a tener solo una referencia legislativa
        # y en realidad hay más encabezados posibles (vencidas, etc.)
        # if cuenta == 1:
        #     if "NNN referencias legislativas relacionadas" in t_intro:
        #         t += t_intro.replace("NNN referencias legislativas relacionadas", f"{cuenta} referencia legislativa relacionada")
        #     elif "NNN referencias legislativas derogadas relacionadas" in t_intro:
        #         t += t_intro.replace("NNN referencias legislativas derogadas relacionadas", f"{cuenta} referencia legislativa derogada relacionada")
        # else:
        #     if "NNN referencias legislativas relacionadas" in t_intro:
        #         t += t_intro.replace("NNN referencias legislativas relacionadas", f"{cuenta} referencias legislativas relacionadas")
        #     elif "NNN referencias legislativas derogadas relacionadas" in t_intro:
        #         t += t_intro.replace("NNN referencias legislativas derogadas relacionadas", f"{cuenta} referencias legislativas derogadas relacionadas")
        t += "\n"
        for apartado in pagina["contenido"]:
            t += f'  <h2>{apartado["apartado"]["titulo"]}</h2>\n'
            t += "\n"
            t += "  <ul>\n"
            for identificador in apartado["apartado"]["referencias"]:
                t += muestra_referencia(
                    gjson.selecciona_en_json(legislacion, "id", identificador),
                    pagina["profundidad"],
                )
                ids.remove(identificador)
            t += "  </ul>\n"
            t += "\n"

        # 2021-03-22. He comentado estas líneas que lo que hacían era añadir las referencias no incluidas en colecciones.json
        # Pero como hay referencias de legislacion.json que me interesa que no salgan (los borradores, por ejemplo), lo he quitado.
        #
        # if pagina["nombre"] == "listados/otras.html":
        #     # t += f"  <h2>Otros</h2>\n"
        #     # t += "\n"
        #     t += "  <ul>\n"
        #     for identificador in ids:
        #         t += muestra_referencia(
        #             gjson.selecciona_en_json(legislacion, "id", identificador),
        #             pagina["profundidad"],
        #         )
        #     t += "  </ul>\n"
        #     t += "\n"
        print(f"Quedan por ordenar {len(ids)} referencias")

        t += pie()

        with open(
            f'{gconst.DIR_SITE}/{pagina["nombre"]}', "w", encoding="utf-8"
        ) as fichero:
            fichero.write(t)
    if ids:
        print(ids)

    return coleccion, ids
