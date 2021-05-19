


salario_hora_trabalhada = float(input ("Digite o salário por hora trabalhada : \n"))

numero_hora_trabalhada = int(input("Digite o número de hora trabalhada : \n"))

total_mes = float(salario_hora_trabalhada * numero_hora_trabalhada)

bruto = total_mes

renda = bruto * (11/100)

inss = bruto * (8/100)

sindicato = bruto * (5/100)

liquido = bruto - (renda + inss + sindicato)

print ("Salário Bruto: {} reais !".format(bruto))
print ("Imposto de renda : {} reias".format(renda))
print ("INSS : {} reais !".format(inss))
print ("Sindicato : {} reias !".format(sindicato))
print ("Líquido : {} reais !".format(liquido))
