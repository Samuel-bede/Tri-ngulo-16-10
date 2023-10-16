# Validador de Triângulo
print('\n\t\t\t --Validador de Triângulo--\n\n')

a = float(input('Informe o tamanho do lado a: '))
b = float(input('Informe o tamanho do lado b: '))
c = float(input('Informe o tamanho do lado c: '))

# Processamento e Saída
if (a > b + c) or (b > a + c) or (c > a + b):
    print('Pelos dados inseridos, este polígono NÃO forma um triângulo!')
else:
    print('Pelos dados inseridos, este polígono forma um triângulo!')
