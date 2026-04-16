import math

area = float(input("Tamanho da área a ser pintada em m²: "))
litros_necessarios = area / 3
# Cada lata tem 18 litros
quantidade_latas = math.ceil(litros_necessarios / 18)
preco_total = quantidade_latas * 80.00

print(f"Latas a comprar: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
