
multa = float(4.00)
peso_maximo = float(50.00)



peso = float(input("Digite o peso do pescado : \n"))

if (peso > peso_maximo):
    excesso = abs(peso - peso_maximo)
    print ("Seu pescado excedeu {} kg !".format(excesso))

    total = float(excesso * multa)

    print ("Multa a se pagar {} reais !".format(total))


else:
    print ("Seu pescado não excedeu o PESO LIMITE ! \n PESO ATUAL : {:.2f} kg !".format(peso))
