class IAtaque:
    def ataque(self):
        pass
class Ataque1(IAtaque):
    def ataque(self):
        print('Combo patada y puño   +15')
class Ataque2(IAtaque):
    def ataque(self):
        print('Uso de armas y espadas    +20')
class Ataque3(IAtaque):
    def ataque(self):
        print('Uso de arco y flecha    +20')
class Ataque4(IAtaque):
    def ataque(self):
        print('Agarre y golpe   +10')
class IMovimiento:
    def movimiento(self):
        pass
class Mov1(IMovimiento):
    def movimiento(self):
        print('Caminar')
class Mov2(IMovimiento):
    def movimiento(self):
        print('Correr')
class Mov3(IMovimiento):
    def movimiento(self):
        print('Saltar')
class Mov4(IMovimiento):
    def movimiento(self):
        print('Camuflarse')
class Mov5(IMovimiento):
    def movimiento(self):
        print('Uso de vehiculo/caballo')
class UnidadesMilitares:
    def __init__(self,ataque: IAtaque,movimiento: IMovimiento) -> None:
        self.ataque=ataque
        self.movimiento=movimiento
    def perform_atacK(self):
        self.ataque.ataque()
    def perform_movement(self):
        self.movimiento.movimiento()
    def descripcion():
        print('Unidades militares')

class Soldado(UnidadesMilitares):
    def __init__(self, ataque, movimiento) -> None:
        super().__init__(ataque,movimiento)
    def descripcion():
        print('Eres un soldado, elige tu modo de ataque/movimiento')
class Arquero(UnidadesMilitares):
    def __init__(self, ataque, movimiento) -> None:
        super().__init__(ataque,movimiento)
    def descripcion():
        print('Eres un arquero, elige tu modo de ataque/movimiento')
class Caballero(UnidadesMilitares):
    def __init__(self, ataque, movimiento) -> None:
        super().__init__(ataque,movimiento)
    def descripcion():
        print('Eres un caballero, elige tu modo de ataque/movimiento')

if __name__ == '__main__':
    atack=Ataque1()
    mov=Mov1()
    jugador= Soldado(atack,mov)
    Soldado.descripcion()
    jugador.perform_atacK()
    jugador.perform_movement()