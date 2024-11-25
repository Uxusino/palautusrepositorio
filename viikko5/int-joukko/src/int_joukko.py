KAPASITEETTI = 5
OLETUSKASVATUS = 5

TYPES = {
    "kapasiteetti": KAPASITEETTI,
    "kasvatuskoko": OLETUSKASVATUS
}


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.validate_list_attribute("kapasiteetti", kapasiteetti)
        self.kasvatuskoko = self.validate_list_attribute("kasvatuskoko", kasvatuskoko)

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    @staticmethod
    def validate_list_attribute(type: str, attr) -> int:
        if not attr:
            return TYPES[type]
        if not isinstance(attr, int) or attr < 0:
            raise Exception(f"Väärä {type}")  # heitin vaan jotain :D
        return attr

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1
            return True
        
        if self.kuuluu(n):
            return False

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            self.kopioi_lista(self.ljono, taulukko_old)
            self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.ljono)

        return True

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta == -1:
            return False

        for j in range(kohta, self.alkioiden_lkm - 1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu

        self.alkioiden_lkm -= 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        new_list = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            new_list.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            new_list.lisaa(b_taulu[i])

        return new_list

    @staticmethod
    def leikkaus(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        new_list = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    new_list.lisaa(b_taulu[j])

        return new_list

    @staticmethod
    def erotus(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        new_list = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            new_list.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            new_list.poista(b_taulu[i])

        return new_list

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        if self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuotos = tuotos + str(self.ljono[i])
            tuotos = tuotos + ", "
        tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
        tuotos = tuotos + "}"
        return tuotos
