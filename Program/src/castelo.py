class Castelo():
    def __init__(self,nro_castelo,nro_soldados):
        """Classe para definir o Castelo"""
        self.nro_castelo = nro_castelo
        self.nro_soldados = nro_soldados
        self.rotas = []
    
    #SOBRECARGA
    def __init__(self):
        pass

    # Métodos básicos para pegar informações
    def getSoldados(self):
        soldados = int(self.nro_soldados)
        return soldados
    def getNroCastelo(self):
        castelo = int(self.nro_castelo)
        return castelo
    def setSoldados(self,nro_soldados):
        self.nro_soldados = nro_soldados
    def setCastelos(self,nro_castelo):
        self.nro_castelo = nro_castelo

    #Métodos para adicionar os Castelos conectados
    def castelosConectados(self,castelo_destino):
        self.rotas.append(castelo_destino)

    def getRota(self,nro_castelo):
        return self.rotas

       
            


        
   
    
    

