from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._ai = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto = None):
        if ensimmaisen_siirto:
            self._ai.aseta_siirto(ensimmaisen_siirto)
        move = self._ai.anna_siirto()
        print(f"Tietokone valitsi: {move}")
        return move
