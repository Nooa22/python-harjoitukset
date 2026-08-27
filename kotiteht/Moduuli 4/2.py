while True:
	tuumat = float(input("Anna tuumamäärä: "))

	if tuumat < 0:
		break

	senttimetri = tuumat * 2.54
	print(f"{senttimetri} cm")
