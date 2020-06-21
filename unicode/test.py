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
