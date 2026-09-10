import random

def noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Kuinka monta tahkoa nopassa on? "))

silmaluku = 0
while silmaluku != tahkot:
    silmaluku = noppa(tahkot)
    print(silmaluku)