import re

def main():
    texto = ' <a href="https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/6aDJhtuEC68">https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/6aDJhtuEC68</a></li>          <li>20/03/2013: <a href="https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/wx17oAA4BIc">https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/wx17oAA4BIc</a></li>          <li>21/03/2013: <a href="https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/wEUuOZfoAKE">https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/wEUuOZfoAKE</a></li>'

    print(f"Inicial: {texto}")
    print(texto)
    print()
    print("Coincidencia")


    # elimina urls
    elimina = ["https", "http", "ftp", "email"]
    for i in elimina:
        x = re.search(r"" + i + r"[^\s\"]+", texto)
        while x:
            print(x.group())
            texto = texto.replace(x.group(), " ")
            x = re.search(r"" + i + r"[^\s\"]+", texto)

    print()
    print(f"Final: {texto}")
    print()

if __name__ == "__main__":
    main()
