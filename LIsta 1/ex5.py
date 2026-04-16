pm = float(input('digite o preço da mercadoria: '))
des = float(input('digite o des em porcentagem (ex: 15: '))
va = des / 100 * pm
vt = pm - va
print(f'seu desconto foi de {va:.2f}')
print(f'o preço do seu produto é de R$:{vt:.2f}')
