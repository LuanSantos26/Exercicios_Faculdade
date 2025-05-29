
#Crie uma lista que receba elemento por elemento do teclado por usuario e coloque em uma lista.
lista = []
for item in range(5):
    valor = input(f'Digite o {item + 1}º valor: ')
    lista.append(valor)

# Mostre a lista na tela
print('Lista:', lista)
# Mostre o tamanho da lista
print('Tamanho da lista:', len(lista))
# Mostre o primeiro e o último elemento da lista
print('Primeiro elemento:', lista[0])
print('Último elemento:', lista[-1])
# Mostre todos os elementos da lista
print('Todos os elementos da lista:')
for i, valor in enumerate(lista):
    print(f'Elemento {i + 1}: {valor}')