from castelo import Castelo

class Reader():
    def __init__(self,arquivo):
        self.arquivo = arquivo
    

    def feudoInicial(self,lista):
        """Serve para criar o primeiro feudo que iremos usar"""
        file = open(self.arquivo)
        header = file.readline()
        separador = header.split(' ')
        exercito_inicial = separador[0]
        novoCastelo = Castelo(0,exercito_inicial)
        lista.append(novoCastelo)


    def nroCastelos(self):
        """Serve para descobrir o numero total de Castelos"""
        file = open(self.arquivo)
        header = file.readline()
        separador = header.split(' ')
        nro_castelos = separador[1]
        return nro_castelos

    def estradasDoReino(self):
        """Serve para pegar o numero de estradas do evento"""
        file = open(self.arquivo)
        header = file.readline()
        separador = header.split(' ')
        nro_estradas = separador[2]
        return nro_estradas

    def definindoCastelos(self,nro_castelos,lista):
        """Serve para colocar as informações em um objeto Castelo"""
        file = open(self.arquivo)
        header = file.readline()
        lines = file.readlines()

        #Primeiras Linhas são o numero dos Castelos e o nro de soldados
        nro_castelos = int(nro_castelos)
        for line in lines[:nro_castelos]:
            separador = line.split(' ')
            nro_castelo = separador[0]
            nro_soldados = separador[1]
            novoCastelo = Castelo(nro_castelo,nro_soldados)
            lista.append(novoCastelo)


    def definindoRotas(self,nro_castelos):
        file = open(self.arquivo)
        header = file.readline()
        lines = file.readlines()

        # Proximas Linhas são as Estradas entre os Castelos
        nro_castelos = int(nro_castelos)
        for line in lines[nro_castelos+1:]:
            separador = line.split(' ')
            castelo_origem = separador[0]
            castelo_destino = separador[1]
            # TODO Criar o Método para poder definir as Rotas



        








            
            

        