from reader import Reader

pergaminho = Reader('pergaminho.txt') # Iniciando a Classe Reader
castelos = [] # Iniciando a lista com os Castelos

pergaminho.feudoInicial(castelos) # Definido o primeiro Feudo
# print(castelos[0].getNroCastelo())
nro_castelos = pergaminho.nroCastelos() # Pego o numero total de Castelos
pergaminho.definindoCastelos(nro_castelos,castelos) # Dividido as informações dos Castelos
# for i in range(0,len(castelos)):
#     print('Castelo ',castelos[i].getNroCastelo())
#     print('Soldados: ',castelos[i].getSoldados())
pergaminho.definindoRotas(nro_castelos,castelos)

print(castelos[0].getRotas()) # Como pegar informações das rotas do castelo






