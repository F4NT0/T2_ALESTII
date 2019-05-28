from castelo import Castelo

# LENDO O ARQUIVO
file = open('pergaminho.txt')

# Trabalhando com o Header
header = file.readline()
separate = header.split(' ')
exercito_inicial = separate[0]
nro_castelos = separate[1]
nro_estradas = separate[2]


nro_castelos = int(nro_castelos) # numero de castelos que iremos trabalhar
feudos = [] # criando o vetor dos castelos


lines = file.readlines()
for line in lines:
    separate = line.split(' ')
    value1 = separate[0]
    value2 = separate[1]
    novoCastelo = Castelo(value1,value2)
    print(novoCastelo.getNroCastelo())
