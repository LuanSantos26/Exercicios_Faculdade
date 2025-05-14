senha = input("Digite a senha: ")
tentativas = 0  
while tentativas < 3:
    senha_digitada = input("Digite a senha novamente: ")
    if senha_digitada == senha:
        print("Senha correta!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Você tem {3 - tentativas} tentativas restantes.")