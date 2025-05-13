contador = 0
acumulador = 0
n=int(input("Quantos números voce deseja calcular a média? "))
while contador < n:
    numero = float(input("Digite um número: "))
    acumulador += numero
    contador += 1
media = acumulador / contador
print("a soma dos números é: ", acumulador)
print("a média dos números é: ", media)