from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

GAMES = {
    "a": KPSPelaajaVsPelaaja(),
    "b": KPSTekoaly(),
    "c": KPSParempiTekoaly()
}

def get_game(command: str):
    return GAMES[command]