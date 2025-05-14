senha = input("Digite a sua senha de acesso : ").lower
confirmacao = input("Confirme sua senha novamente :").lower
tentativas = 0
limite = 3

while limite < tentativas:
    senha = input("Digite a sua senha de acesso : ").lower()
    confirmacao = input("Confirme sua senha novamente :").lower()
    if senha == confirmacao:
        print("Senha correta, Acesso permitido !")
        break
    elif senha != confirmacao:
        print("Senha incorreta, Acesso negado !")
        limite -= 1
        if tentativas == limite:
            print("Limite de tentativas atingido, Acesso negado !")
  
