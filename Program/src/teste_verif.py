# Teste de Verificação do Castelo
from castelo import Castelo

castelo_inicial = Castelo(0,200)
proximo_castelo = Castelo(1,100)

castelo_inicial.castelosConectados(proximo_castelo)

# Teste do Castelo Inicial

print('Numero do Castelo Inicial: ', castelo_inicial.getNroCastelo())
print('Numero de Soldados do Castelo: ', castelo_inicial.getNroSoldados())

#Teste para ver se o castelo esta na lista

lista = castelo_inicial.getRota(castelo_inicial.getNroCastelo)
for valor in lista:
    print('Castelo na Lista: ',valor.getNroCastelo())

# Definindo o segundo castelo como proximo

castelo_inicial.setProximo(proximo_castelo)

print('Proximo Castelo da Lista: ', castelo_inicial.getProximo().getNroCastelo())
