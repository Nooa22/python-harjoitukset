class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros += 1
        print("Hissi on kerroksessa " + str(self.kerros))

    def kerros_alas(self):
        self.kerros -= 1
        print("Hissi on kerroksessa " + str(self.kerros))

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)