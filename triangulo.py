p1=float(input("Digite o primeiro lado do triângulo :"))
p2=float(input("Digite o segundo lado do triângulo:")) 
p3=float(input("Digite o terceiro lado do triângulo:"))
if p1 + p2 > p3 and p1 + p3 > p2 and p2 + p3 > p1:
    print("Os lados formam um triângulo")   
if p1 == p2 and p2 == p3:
    print("O triângulo é equilátero, todos os lados são iguais")
elif p1 == p2 or p1 == p3 or p2 == p3:
    print("O triângulo é isósceles, com dois lados iguais")
elif p1 != p2 and p1 != p3 and p2 != p3:
    print("O triângulo é escaleno,todos os lados são diferentes")