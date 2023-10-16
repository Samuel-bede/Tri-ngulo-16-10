#Descubra se os lados de um polígono formam triângulo.
a = int(input('Digite um tamanho para o triângulo: '))
b = int(input('Digite um tamanho para o triângulo: '))
c = int(input('Digite um tamanho para o triângulo: '))
if a == b and a == c:
    print('Pelos dados inseridos, este polígono forma um triângulo!')
else:
    print('Pelos dados inseridos, este polígono não forma um triângulo!')
