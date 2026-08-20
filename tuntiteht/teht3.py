gramma =int(input("Kuinka monta grammaa: "))
g = gramma % 1000
kilo = gramma / 1000
print(f"Määrä kiloina ja grammoina: {kilo:.0f} kg {g} g")