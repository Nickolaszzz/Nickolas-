numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacao == "/":
    if numero2 == 0:
        print("Erro: não é possível dividir por zero!")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
else:
    print("Operação inválida!")
