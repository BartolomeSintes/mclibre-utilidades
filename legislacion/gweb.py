import json, pathlib
from datetime import date
import gconst, gjson


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


def cabecera(titulo, profundidad):
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
    tmp += "</head>\n"
    tmp += "\n"
    tmp += "<body>\n"
    tmp += f"  <h1>{titulo}</h1>\n"

    if profundidad == 0:
        tmp += '<p><a href="https://github.com/BartolomeSintes/mclibre-legislacion"><img style="position: absolute; top: 0; right: 0; border: 0; opacity: 0.7;" src="https://camo.githubusercontent.com/e7bbb0521b397edbd5fe43e7f760759336b5e05f/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f677265656e5f3030373230302e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_green_007200.png"></a></p>'

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
        tmp += "        <li>Educativa\n"
        tmp += "          <ul>\n"
        tmp += '            <li><a href="educativa-eu.html">Unión Europea</a></li>\n'
        tmp += '            <li><a href="educativa-es.html">España</a></li>\n'
        tmp += "            <li>Comunidades Autónomas:\n"
        tmp += "              <ul>\n"
        tmp += '                <li><a href="educativa-es-vc.html">Comunidad Valenciana</a></li>\n'
        tmp += '                <li><a href="educativa-es-min.html">Territorio MEC</a></li>\n'
        tmp += "              </ul>\n"
        tmp += "            </li>\n"
        tmp += '            <li><a href="educativa-derogada.html">Derogada</a></li>\n'
        tmp += "          </ul>\n"
        tmp += "        </li>\n"
        tmp += '        <li><a href="otras.html">Otros temas</a></li>\n'
        tmp += '        <li><a href="cronologico.html">Orden Cronológico</a></li>\n'
        tmp += "      </ul>\n"
        tmp += "    </div>\n"
    tmp += "  </nav>\n"
    tmp += "\n"

    return tmp


def seccion(legislacion, id, titulo):
    tmp = f'  <section id="{id}">\n'
    tmp += f"    <h2>{titulo}</h2>\n"
    tmp += "\n"
    tmp += f'    <div class="disposiciones">\n'
    for elemento in legislacion:
        tmp += f'      <article class="disposicion" id="{elemento["id"]}">\n'
        tmp += f'        <h3>{elemento["descripción"]}</h3>\n'
        tmp += f'        <p class="publicacion">\n'
        tmp += f'          {bandera(elemento["ámbito"], 25)}\n'
        tmp += f'          {elemento["origen"]} {elemento["fecha"]}\n'
        if elemento["vigencia"] == gconst.DEROGADO:
            tmp += f'          <span class="derogado">derogado</span>\n'
        tmp += "        </p>\n"
        for version in elemento["versiones"]:
            tmp += '        <p class="fichero">\n'
            if len(elemento["versiones"]) != 1:
                tmp += f'        {version["versión"][:1].upper() + version["versión"][1:]}: '
            for i in range(len(version["enlaces"])):
                if version["enlaces"][i]["formato"] != "web":
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
        tmp += f'    <article class="disposicion" id="{elemento["id"]}">\n'
        tmp += f'      <h3>{elemento["descripción"]}</h3>\n'
        tmp += f'      <p class="publicacion">\n'
        tmp += f'        {bandera(elemento["ámbito"], 25)}\n'
        tmp += f'        {elemento["origen"]} {elemento["fecha"]}\n'
        if elemento["vigencia"] == gconst.DEROGADO:
            tmp += f'        <span class="derogado">derogado</span>\n'
        tmp += "      </p>\n"
        for version in elemento["versiones"]:
            tmp += '      <p class="fichero">\n'
            if version["versión"] == "borrador":
                tmp += f'        <img src="../{gconst.DIR_IMAGES}/en-construccion.svg" alt="Borrador" title="Borrador" width="25">'
                tmp += '<span class="derogado">borrador</span>'
            if len(elemento["versiones"]) != 1:
                tmp += (
                    f'      {version["versión"][:1].upper() + version["versión"][1:]}: '
                )
            for i in range(len(version["enlaces"])):
                if version["enlaces"][i]["formato"] != "web":
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
            if version["enlaces"][i]["formato"] != "web":
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


def guarda_fichas():
    # Carga json
    with open(gconst.JSON_FILE_REFERENCES, encoding="utf-8") as file:
        tmp = json.load(file)
    legislacion = gjson.ordena(tmp, "fecha", True)["legislacion"]

    # Genera índice
    t = ""
    t += "\n"
    t += cabecera("Legislación informática - Orden cronológico", 1)

    t += f"  <p>Esta página muestra las {len(legislacion)} referencias legislativas de este repositorio en orden cronológico inverso.</p>\n"
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


def guarda_index(nombre):
    # Carga json legislación
    with open(gconst.JSON_FILE_REFERENCES, encoding="utf-8") as file:
        tmp = json.load(file)
    legislacion = gjson.ordena(tmp, "fecha", False)["legislacion"]

    ids = [d["id"] for d in legislacion]

    t = ""
    t += cabecera("Legislación Informática", 0)

    t += "  <p>Este sitio web recopila legislación relacionada con la Informática. Se trata en su mayor parte de legislación "
    t += "educativa, pero también contiene legislación relacionada con otros temas (protección de datos, seguridad, etc.).</p>\n"
    t += "\n"
    t += f"  <p>Este sitio web contiene {len(ids)} referencias, distribuidas en varias páginas:</p>\n"
    t += "  <ul>\n"
    t += "    <li>Legislación educativa\n"
    t += "      <ul>\n"
    t += '        <li><a href="listados/educativa-eu.html">Unión Europea</a></li>\n'
    t += '        <li><a href="listados/educativa-es.html">España</a></li>\n'
    t += "        <li>Comunidades Autónomas:\n"
    t += "          <ul>\n"
    t += '            <li><a href="listados/educativa-es-vc.html">Comunidad Valenciana</a></li>\n'
    t += '            <li><a href="listados/educativa-es-min.html">Territorio MEC</a></li>\n'
    t += "          </ul>\n"
    t += "        </li>\n"
    t += '        <li><a href="listados/educativa-derogada.html">Derogada</a></li>\n'
    t += "      </ul>\n"
    t += "    </li>\n"
    t += '    <li><a href="listados/otras.html">Otros temas</a></li>\n'
    t += '    <li><a href="listados/cronologico.html">Todas las referencias en orden cronológico inverso</a></li>\n'
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
        t += cabecera(pagina["titulo"], pagina["profundidad"])
        # t += '  <p><a href="fichas.html">Versión en forma de fichas</a></p>\n'
        # t += "\n"
        cuenta = gjson.cuenta_referencias_en_coleccion(pagina)
        t_intro = pagina["introducción"]
        if cuenta == 1:
            if "NNN referencias legislativas relacionadas" in t_intro:
                t += t_intro.replace("NNN referencias legislativas relacionadas", f"{cuenta} referencia legislativa relacionada")
            elif "NNN referencias legislativas derogadas relacionadas" in t_intro:
                t += t_intro.replace("NNN referencias legislativas derogadas relacionadas", f"{cuenta} referencia legislativa derogada relacionada")
        else:
            if "NNN referencias legislativas relacionadas" in t_intro:
                t += t_intro.replace("NNN referencias legislativas relacionadas", f"{cuenta} referencias legislativas relacionadas")
            elif "NNN referencias legislativas derogadas relacionadas" in t_intro:
                t += t_intro.replace("NNN referencias legislativas derogadas relacionadas", f"{cuenta} referencias legislativas derogadas relacionadas")
        t += "\n"
        for apartado in pagina["contenido"]:
            t += f'  <h2>{apartado["apartado"]["titulo"]}</h2>\n'
            t += "\n"
            t += "  <ul>\n"
            for id in apartado["apartado"]["referencias"]:
                t += muestra_referencia(
                    gjson.selecciona_en_json(legislacion, "id", id),
                    pagina["profundidad"],
                )
                ids.remove(id)
            t += "  </ul>\n"
            t += "\n"

        if pagina["nombre"] == "listados/otras.html":
            # t += f"  <h2>Otros</h2>\n"
            # t += "\n"
            t += "  <ul>\n"
            for id in ids:
                t += muestra_referencia(
                    gjson.selecciona_en_json(legislacion, "id", id),
                    pagina["profundidad"],
                )
            t += "  </ul>\n"
            t += "\n"
        print(f"Quedan por ordenar {len(ids)} referencias")

        t += pie()

        with open(
            f'{gconst.DIR_SITE}/{pagina["nombre"]}', "w", encoding="utf-8"
        ) as fichero:
            fichero.write(t)
    if ids:
        print(ids)

    return coleccion
