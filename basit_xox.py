
def yap(a,b,c,d,e,r,f,g,h):
    sr = (f"""

___{a}___  ___{b}___  ___{c}___

___{d}___  ___{e}___  ___{r}___

___{f}___  ___{g}___  ___{h}___

    """)
    print(sr)
def sölük():
    sözlük["a"] = "A"
    sözlük["b"] = "B"
    sözlük["c"] = "C"
    sözlük["d"] = "D"
    sözlük["e"] = "E"
    sözlük["r"] = "R"
    sözlük["f"] = "F"
    sözlük["g"] = "G"
    sözlük["h"] = "H"
    yap(sözlük["a"],sözlük["b"],sözlük["c"],sözlük["d"],sözlük["e"],sözlük["r"],sözlük["f"],sözlük["g"],sözlük["h"])
while True:
    sözlük = {
    "a" : "A",
    "b" : "B",
    "c" : "C",
    "d" : "D",
    "e" : "E",
    "r" : "R",
    "f" : "F",
    "g" : "G",
    "h" : "H",}
    liste = list(sözlük.keys())
    yap(sözlük["a"],sözlük["b"],sözlük["c"],sözlük["d"],sözlük["e"],sözlük["r"],sözlük["f"],sözlük["g"],sözlük["h"])
    while True:
        if sözlük["a"] == sözlük["b"] == sözlük["c"]:
            print(f" oyunu {sözlük['a']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["d"] == sözlük["e"] == sözlük["r"]:
            print(f" oyunu {sözlük['d']} kazandı")
            print(f" oyunu {sözlük['a']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["f"] == sözlük["g"] == sözlük["h"]:
            print(f" oyunu {sözlük['f']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["b"] == sözlük["e"] == sözlük["g"]:
            print(f" oyunu {sözlük['b']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["c"] == sözlük["r"] == sözlük["h"]:
            print(f" oyunu {sözlük['c']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["a"] == sözlük["d"] == sözlük["f"]:
            print(f" oyunu {sözlük['a']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["c"] == sözlük["e"] == sözlük["f"]:
            print(f" oyunu {sözlük['c']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif sözlük["a"] == sözlük["e"] == sözlük["h"]:
            print(f" oyunu {sözlük['a']} kazandı")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        elif len(liste) == 0:
            print("berabere")
            cevap = input("tekrar oynamak istiyormusunuz(e/h):")
            if cevap == "e" or cevap == "E":
                sölük()
                liste = list(sözlük.keys())
                continue
            else:
                break
        harf = input("x mi o mu:")
        if harf == "o" or harf == "O" or harf == "X" or harf == "x":
            yer = input("harfi yazmak istediğiniz yer:")
            if yer in liste:
                sözlük[yer] = harf.upper()
                liste.remove(yer)
                yap(sözlük["a"],sözlük["b"],sözlük["c"],sözlük["d"],sözlük["e"],sözlük["r"],sözlük["f"],sözlük["g"],sözlük["h"])


            else:
                continue
        else:
            continue
    break

