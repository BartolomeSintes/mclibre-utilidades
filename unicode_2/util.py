
# Genera la lista para manual_2
# Solo tengo que copiar los códigos que no se ven bien en este programa
# y me genera el texto que puedo copiar en manual_2

origen = [
    "U+1F468 U+200D U+1F37C",
    "U+1F469 U+200D U+1F37C",
    "U+1F3CB U+200D U+2640",
    "U+1F3CB U+200D U+2642",
]

t = ""
for cadena in origen:
    t += "  [\n"
    cadena2 = cadena.replace("U+", "").split(" ")
    # print(cadena2)
    t += f"    {cadena2},\n"
    t += "    ['No disponible en Windows 10']\n"
    t += "  ],\n"

print(t)
