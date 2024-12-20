from enum import Enum
from tkinter import ttk, constants, StringVar

from sovelluslogiikka import Sovelluslogiikka


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Operaatio:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._syote = syote

class Summa(Operaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self._sovelluslogiikka.plus(self._syote())

class Erotus(Operaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self._sovelluslogiikka.miinus(self._syote())

class Nollaus(Operaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumous(Operaatio):
    def __init__(self, sovelluslogiikka, syote):
        super().__init__(sovelluslogiikka, syote)
    
    def suorita(self):
        self._sovelluslogiikka.kumoa()


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except Exception as e:
            print(str(e))
            return 0

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        self._komennot = {
            Komento.SUMMA: Summa(self._sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(self._sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(self._sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumous(self._sovelluslogiikka, self._lue_syote)
        }

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):

        self._komennot[komento].suorita()

        if self._sovelluslogiikka.tyhja_historia():
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
