class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit


auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"\nNopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

auto.kiihdytä(-200)

print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

auto.kiihdytä(60)
auto.kulje(1.5)

print(f"Kuljettu matka: {auto.kuljettu_matka} km")