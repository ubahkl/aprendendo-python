numero_em_texto = '12'
numero = int(numero_em_texto)
chute1 = 0

chute = input("Digite um número : \n")
chute1 = int(chute)

if (chute1 == numero):
    print ("Vc acertou !  Parabéns !")
else:
    if chute1 > numero:
        print ("Chute maior que o número !")
    else:
        print ("Chute menor que o número !")

