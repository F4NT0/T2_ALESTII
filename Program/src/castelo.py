class Castelo():
    def __init__(self,nro_castelo,nro_soldados):
        """Classe para definir o Castelo"""
        self.nro_castelo = nro_castelo
        self.nro_soldados = nro_soldados
        self.proximo = None
        self.rotas = []
    

    # Métodos básicos para pegar informações
    def getNroSoldados(self):
        """Pegar o Número de Soldados"""
        soldados = int(self.nro_soldados)
        return soldados

    def getNroCastelo(self):
        """Pegar o Número do Castelo"""
        castelo = int(self.nro_castelo)
        return castelo

    def getProximo(self):
        """Pegar o Próximo Nodo que iremos ir"""
        return self.proximo

    def setSoldados(self,nro_soldados):
        """Definir o Número de Soldados"""
        self.nro_soldados = nro_soldados

    def setCastelos(self,nro_castelo):
        """Definir o Número de Castelos"""
        self.nro_castelo = nro_castelo

    def setProximo(self,proximo):
        """Definir qual proximo Nodo iremos ir"""
        self.proximo = proximo

    #Métodos para adicionar os Castelos conectados
    def castelosConectados(self,castelo_destino):
        """Adicionamos os Nodos que possuimos Rotas na Lista Rotas"""
        self.rotas.append(castelo_destino)

    def getRota(self,nro_castelo):
        """Enviamos a Lista de Rotas para fora"""
        return self.rotas

       
            


        
   
    
    

