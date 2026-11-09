"""Convierte un perfil del directorio actual mediante sustituciones de texto."""

from pathlib import Path


def convertir(texto: str) -> str:
    """Aplica las cinco sustituciones, respetando su orden y las mayúsculas."""
    sustituciones = (
        (r'\\\"\\\\n\\\"', 'YYY'),
        (r'\\n', 'XXX'),
        ('YYY', r'"\n"'),
        (r'\\\"', '"'),
        ('XXX', '\n'),
    )
    for buscar, reemplazar in sustituciones:
        texto = texto.replace(buscar, reemplazar)
    return texto


def main() -> None:
    archivos = sorted(Path.cwd().glob('*.code-profile'), key=lambda p: p.name)
    archivos = [
        archivo for archivo in archivos
        if archivo.is_file() and not archivo.name.endswith('-LINEAS.code-profile')
    ]
    if not archivos:
        print('No hay ficheros *.code-profile en el directorio actual.')
        return

    print('Elige el fichero inicial:')
    for numero, archivo in enumerate(archivos, start=1):
        print(f'{numero}. {archivo.name}')
    print('0. Salir')

    while True:
        try:
            numero = int(input('Número del fichero: '))
        except ValueError:
            print('Escribe un número entero del menú.')
            continue
        if numero == 0:
            return
        if 1 <= numero <= len(archivos):
            inicial = archivos[numero - 1]
            break
        print(f'Escribe un número entre 0 y {len(archivos)}.')

    final = inicial.with_name(f'{inicial.stem}-LINEAS{inicial.suffix}')
    sobrescribir = False
    if final.exists():
        print(f'El fichero {final.name} ya existe.')
        respuesta = input('¿Quieres sobreescribirlo? [s/N]: ').strip().casefold()
        if respuesta not in ('s', 'sí', 'si'):
            print('Operación cancelada.')
            return
        sobrescribir = True

    try:
        with inicial.open('r', encoding='utf-8', newline='') as fichero:
            texto = fichero.read()
        resultado = convertir(texto)
        # El modo exclusivo impide sobreescribir sin confirmación si aparece
        # un fichero de destino después de la comprobación anterior.
        modo = 'w' if sobrescribir else 'x'
        with final.open(modo, encoding='utf-8', newline='') as fichero:
            fichero.write(resultado)
    except (OSError, UnicodeError) as error:
        print(f'No se ha podido completar la conversión: {error}')
        return
    print(f'Fichero generado: {final.name}')


if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print('\nOperación cancelada.')
