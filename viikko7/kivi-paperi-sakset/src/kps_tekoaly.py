from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._ai = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto=None):
        move = self._ai.anna_siirto()
        print(f"Tietokone valitsi: {move}")
        return move
