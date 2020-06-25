c = ["0203C", "0232D"]
for tmp in c:
    t = "U+" + str(int(tmp, 16)).upper() + " "
    print(t)
    t = "&amp;#x" + "{:x}".format(int(tmp, 16)) + ";"
    print(t)
    t = f"&amp;#x{int(tmp, 16):x};"
    print(t)
    t = f"&#x{int(tmp, 16):X}"
    print(t)

a = [1, 2, 3, 1, 1, 2, 2, 1, 1, 1, 2, 1]
quita = 1
print(a)
a = [valor for valor in a if valor != quita]
print(a)
