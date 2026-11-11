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

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, numero, kerros):
        self.hissit[numero - 1].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(3, 7)
talo.palohälytys()