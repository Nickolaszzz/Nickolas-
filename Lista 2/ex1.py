a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("É um triângulo!")
    if a == b == c:
        print("Tipo: Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")
else:
    print("Não pode ser um triângulo.")
