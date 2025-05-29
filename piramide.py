#Faça uma piramide usando laço de repetição, usando * 
piramide = int(input('Digite o número de linhas da pirâmide: '))
for i in range(1, piramide + 1):
    print(' ' * (piramide - i) + '*' * (2 * i - 1))
# Exemplo de uso:
# Digite o número de linhas da pirâmide: 5
#     *
#    *****
#   *******
#  *********
# ***********
#1. A pirâmide será impressa com o número de linhas especificado pelo usuário.
