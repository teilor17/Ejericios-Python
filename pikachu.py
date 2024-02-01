
class Pikachu:

    def __init__(self, poder, resis, cura):
        self.poder = poder
        self.resis = resis
        self.cura = cura
        self.puntos = 0


poder1 = int(input('ingrese el poder del pikachu 1: '))
resis1 = int(input('ingrese la resistencia del pikachu 1: '))
cura1 = int(input('ingrese la curacion del pikachu 1: '))

poder2 = int(input('ingrese el poder del pikachu 2: '))
resis2 = int(input('ingrese la resistencia del pikachu 2: '))
cura2 = int(input('ingrese la curacion del pikachu 2: '))


pikachu_1 = Pikachu(poder1, resis1, cura1)
pikachu_2 = Pikachu(poder2, resis2, cura2)


for atributo in ['poder', 'resis', 'cura']:
    if getattr(pikachu_1, atributo) > getattr(pikachu_2, atributo):
        pikachu_1.puntos += 1
    elif getattr(pikachu_2, atributo) > getattr(pikachu_1, atributo):
        pikachu_2.puntos += 1


if pikachu_1.puntos > pikachu_2.puntos:
    print(f'''THE WIN PIKACHU 1,
    PUNTOS : {pikachu_1.puntos}
    Poder de: {poder1},
    Resistencia de: {resis1},
    Curacion de: {cura1} ''')
    print(f'''lOSES  PIKACHU 2,
    PUNTOS : {pikachu_2.puntos}
    Poder de: {poder1},
    Resistencia de: {resis1},
    Curacion de: {cura1} ''')
elif pikachu_2.puntos > pikachu_1.puntos:
    print(f'''THE WIN PIKACHU 2,
    PUNTOS : {pikachu_2.puntos}
    Poder de: {poder1},
    Resistencia de: {resis1},
    Curacion de: {cura1} ''')
    print(f'''LOSES PIKACHU 1,
    PUNTOS : {pikachu_1.puntos}
    Poder de: {poder1},
    Resistencia de: {resis1},
    Curacion de: {cura1} ''')
else:
    print('EMPATE, NINGUN PIKACHU GANA')






