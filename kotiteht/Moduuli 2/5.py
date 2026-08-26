leiviska = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

yhteensa = leiviska * 20 * 32 + naulat * 32 + luodit
grammat = yhteensa * 13.3
kilogrammat = int(grammat // 1000)
grammat = grammat % 1000

print(f"\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.0f} grammaa.")