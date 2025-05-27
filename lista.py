lista=['maça, banana, laranja, uva, abacaxi, morango, kiwi, pêra, melancia, manga']
print('Lista de frutas:', lista)
for fruta in lista[0].split(', '):
    print(fruta.strip())
#def adicionar_fruta(fruta):
 #   if fruta not in lista[0]:
  #      lista[0] += ', ' + fruta
    #    print(f'{fruta} foi adicionada à lista.')
    #else:
     #   print(f'{fruta} já está na lista.')
#def remover_fruta(fruta):
 #   if fruta in lista[0]:
  #      lista[0] = ', '.join([f for f in lista[0].split(', ') if f.strip() != fruta])
   #     print(f'{fruta} foi removida da lista.')
 #   else:
#        print(f'{fruta} não está na lista.')
        