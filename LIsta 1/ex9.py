dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram percorridos? "))

# R$ 60,00 por dia e R$ 0,15 por km
total = (dias * 60) + (km * 0.15)

print(f"O total a pagar é R$ {total:.2f}")
