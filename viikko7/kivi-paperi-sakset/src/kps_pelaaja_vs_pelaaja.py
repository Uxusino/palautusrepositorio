from tuomari import Tuomari
from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()

    def _toisen_siirto(self, ensimmaisen_siirto=None):
        return input("Toisen pelaajan siirto: ")
