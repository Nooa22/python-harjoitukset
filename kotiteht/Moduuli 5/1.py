import random
määrä = int(input("Anna arpakuutioiden määrä: "))

summa = 0

for luku in range(määrä):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print("Silmälukujen summa:", summa)