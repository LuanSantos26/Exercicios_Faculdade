
#Crie uma lista que receba elemento por elemento do teclado por usuario e coloque em uma lista.
item=input("digite o item que queira adiconar em sua lista: ")
lista=[].append(item)
for item in lista:
    novo_item=input("digite um novo item em sua lista: ", [item+1])