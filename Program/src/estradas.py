class Estradas():
    def __init__(self,castelo):
        """Construtor das estradas pegando a lista de rotas do Castelo"""
        self.castelo = castelo

    def acharMinimo(self,castelo):
        """Pega a lista de rotas de um castelo especifico"""
        lista = castelo.getRotas()
        for valor in lista:
            nova_lista = valor.getNroCastelo()
        return nova_lista

    
    
