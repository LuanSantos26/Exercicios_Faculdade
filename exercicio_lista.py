
#Crie uma lista que receba elemento por elemento do teclado por usuario e coloque em uma lista.
lista = []
for i in range(5):  # Permite ao usuário adicionar 5 elementos
    elemento = input("Digite um elemento para adicionar à lista  o permitido no momento é 5 (ou 'sair' para encerrar): ")
    if elemento.lower() == 'sair':
        break
    lista.append(elemento)

print("Lista completa:", lista) 