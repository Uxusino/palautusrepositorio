from tuomari import Tuomari

MOVES = ["k", "p", "s"]

class KiviPaperiSakset:
    def __init__(self):
        self._tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto, tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto = None):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto1, siirto2):
        return siirto1 in MOVES and siirto2 in MOVES
