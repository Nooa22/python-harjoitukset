def litroiksi(gallona):
    return gallona * 3.785

gallona = float(input("Anna gallonamäärä: "))

while gallona >= 0:
    litrat = litroiksi(gallona)
    print(litrat)
    gallona = float(input("Anna gallonamäärä: "))
