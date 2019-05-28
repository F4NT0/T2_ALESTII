class Castelo():
    def __init__(self,nro_castelo,nro_soldados):
        """Classe para definir o Castelo"""
        self.nro_castelo = nro_castelo
        self.nro_soldados = nro_soldados
        self.rotas = []

    # Métodos básicos para pegar informações
    def getSoldados(self):
        return self.nro_soldados
    def getNroCastelo(self):
        return self.nro_castelo
    def setSoldados(self,nro_soldados):
        self.nro_soldados = nro_soldados
    def setCastelos(self,nro_castelo):
        self.nro_castelo = nro_castelo

    #Métodos para adicionar os Castelos conectados
    def castelosConectados(self,castelo_destino):
        self.rotas.append(castelo_destino)

    def getRotas(self):
        for rota in self.rotas:
            print(rota)


        
   
    
    

