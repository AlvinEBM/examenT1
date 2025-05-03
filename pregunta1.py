import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

equipo1 = Equipo("A")
equipo2 = Equipo("B")

def registarSet(equipo_ganador):
    if equipo_ganador == equipo1:
        equipo1.setGanados += 1
    elif equipo_ganador == equipo2:
        equipo2.setGanados += 1

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0

def puntos():
    return random.randint(10, 28)

def puntosExtras():
    return random.randint(0, 6)

def jugarPartido():
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        puntos1 = puntos()
        puntos2 = puntos()
        if puntos1 >= 25 and puntos1 > puntos2:
            registarSet(equipo1)
        elif puntos2 >= 25 and puntos2 > puntos1:
            registarSet(equipo2)
        else:
            while True:
                puntos1 += puntosExtras()
                puntos2 += puntosExtras()
                if puntos1 >= 25 and puntos1 > puntos2:
                    registarSet(equipo1)
                    
                elif puntos2 >= 25 and puntos2 > puntos1:
                    registarSet(equipo2)
                    

