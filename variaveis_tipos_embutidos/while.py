n_secreto = 50
rodada = 1

tentativa1 = input("Quantas tentativas deseja executar : \n")
tentativa = int(tentativa1)

for rodada in range(rodada + 1,tentativa):

    print (" RODADA : \n", rodada)

    chute1 = input("Digite o chute : \n")
    chute = int(chute1)

    acertou = (chute == n_secreto)
    menor = (n_secreto < chute) 
    maior = (n_secreto > chute)

    if (acertou):
        print ("Acertou")
        break
    elif(menor):
        print ("Errou , seu chute foi menor que o número secreto !")
    elif(maior):
        print ("Errou , seu chute foi maior que o número secreto !")


