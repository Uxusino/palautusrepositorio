class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._historia = [0]

    def _lisaa_historiaan(self, arvo):
        self._historia.append(arvo)

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self._lisaa_historiaan(self._arvo)

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self._lisaa_historiaan(self._arvo)

    def nollaa(self):
        self._arvo = 0
        self._historia = [0]

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def tyhja_historia(self) -> bool:
        return self._historia == [0]
    
    def kumoa(self):
        if self._historia == [0]:
            return
        self._historia.pop()
        self._arvo = self._historia[-1]
