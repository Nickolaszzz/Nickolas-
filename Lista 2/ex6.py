valor_hora = float(input("Valor por hora: "))
horas_mes = float(input("Horas trabalhadas: "))

bruto = valor_hora * horas_mes
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print(f"a. + Salário Bruto : R$ {bruto:.2f}")
print(f"b. - IR (11%)      : R$ {ir:.2f}")
print(f"c. - INSS (8%)     : R$ {inss:.2f}")
print(f"d. - Sindicato (5%): R$ {sindicato:.2f}")
print(f"e. = Salário Liquido : R$ {liquido:.2f}")
