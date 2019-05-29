<center>

</center>

<code style="color : "></code>


<center>
    <h1>O caminho dos castelos</h1>
</center>

<center>
    <h3>Gabriel Fanto Stundner</h3>
    <h4>Faculdade de Informática - PUCRS</h4>
    <h5>29 de Maio de 2019</h5>
</center>

---

<center>
    <code style="color : blue">Resumo</code>
</center>

---

Este Artigo apresenta uma forma de se conquistar Feudos inimigos utilizando grafos, onde a cada Castelo possui um Exercito específico e devemos utilizar uma parte dele para consquistar os outros Feudos pelas rotas definidas


---

## Introdução

Neste trabalho estamos trabalhando com a leitura de um Arquivo texto que possui as seguintes informações importantes:
* Primeira linha possui as informações gerais que precisamos
  * Número de Soldados do Castelo Inicial
  * Número de Castelos Totais que iremos tentar Conquistar
  * Número de Estradas que podemos interagir 
* Nas proximas Linhas até o número total de castelos totais temos:
  * Número do Castelo Especifico
  * Número de Soldados desse Castelo
* Nas Linhas em diante após definir o castelo e os soldados temos:
  * O número do Castelo origem
  * O número do Castelo Destino

Com essas informações iremos fazer o Seguinte:

Iremos criar <code style="color : green">Nodos</code> que irão armazenar as informações do castelo, onde cada informação retirada do arquivo nas primeiras linhas irão ser guardadas(número do Castelo e Número de Soldados).

Dentro de Cada nodo existe uma Lista de outros Nodos que são referenciados ao Nodo atual, ou seja, são Nodos que possuem uma Rota a este Nodo, onde o Nodo atual pode ir se quiser

Quando tivermos todos os Nodos organizados, com as referências bem definidas na Lista interna queremos fazer as Seguinte coisas:

1. Queremos verificar qual dos Castelos que queremos ir tem o menor número de Soldados, sendo esse número menor que a metade de soldados que queremos utilizar.
2. Todo feudo que estamos devemos deixar 50 soldados para que protejam o nosso Castelo inicial e com o resto dos Soldados iremos atacar o Pŕoximo Castelo
3. 
