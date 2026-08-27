pienin = None
suurin = None
luku = input("Anna luku: ")
while luku != "":
    luku = int(luku)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

    luku = input("Anna luku: ")

print("Pienin luku:", pienin)
print("Suurin luku:", suurin)