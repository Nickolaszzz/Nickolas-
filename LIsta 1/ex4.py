sal = float(input('digite seu salário: '))
aum = float(input('digite o aumemento em porcentagem (ex: 15: '))
va = aum / 100 * sal
vt = va + sal
print(f'seu aumento foi de {va:.2f}')
print(f'o aumento no seu salario foi de R$:{vt:.2f}')
