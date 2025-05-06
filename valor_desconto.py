# Este programa calcula o valor do desconto em um produto e o valor final do produto após aplicar o desconto.
# O desconto é calculado com base no valor do produto e na porcentagem de desconto fornecida pelo usuário.
valor = float(input("Digite o valor do produto: "))
print("Escolha a forma de pagamento:")
print("1 - À vista no PIX (10% de desconto)")   
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Parcelado em 2x (sem desconto)")
print("4 - Parcelado em 3x (10% de juros)")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    desconto_pix = valor * (10 / 100)
    valor_final = valor - desconto_pix
    print(f"O valor do desconto é: {desconto_pix:.2f}")
    print(f"O valor final do produto é: {valor_final:.2f}")
elif opcao == 2:
    desconto_cartao = valor * (5 / 100)
    valor_final = valor - desconto_cartao
    print(f"O valor do desconto é: {desconto_cartao:.2f}")
    print(f"O valor final do produto é: {valor_final:.2f}")
elif opcao == 3:
    valor_final = valor
    print(f"O valor do desconto é: 0.00")
    print(f"O valor final do produto é: {valor_final:.2f}")
elif opcao == 4:
    juros = valor * (10 / 100)
    valor_final = valor + juros
    print(f"O valor do desconto é: 0.00")
    print(f"O valor final do produto é: {valor_final:.2f}")
else:
    print("Opção inválida. Tente novamente.")
# O programa calcula o valor do desconto e o valor final do produto com base na opção de pagamento escolhida pelo usuário.

