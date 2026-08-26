pituus = int(input("Kuinka pitkä olet? "))
if 100 <= pituus <140:
    print("Saat mennä lasten laitteisiin.")
elif pituus >= 140:
    print("Saat mennä kaikkiin laitteisiin.")
else:
    print("Et saa mennä mihinkään laitteeseen.")
