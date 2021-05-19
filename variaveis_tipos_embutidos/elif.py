numero_secreto = 42

rodada = 1

total_de_tentativas1 = input("quantas tentativas : \n")
total_de_tentativas = int(total_de_tentativas1)

while ( rodada <= total_de_tentativas ):
    print ("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute1 = input("Digite seu número :\n")
    chute = int(chute1)

    print ("Voce digitou ", chute,  " !")

    chute = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if (chute):
        print ("Acertou !")
        break
    elif (maior):
        print ("Errou, seu chute for maior !")
    elif (menor):
        print ("Errou , seu chute foi menor !")

    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada + 1


print ("======= FIM DE JOGO ! =======")


