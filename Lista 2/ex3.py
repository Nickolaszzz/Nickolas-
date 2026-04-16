peso = float(input("Digite o peso dos peixes: "))
excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00

print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa:.2f}")
