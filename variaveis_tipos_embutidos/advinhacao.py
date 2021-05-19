print('******************************')
print('*Jogo da adivinhação*')
print('******************************')

n_secreto = 42

chute1 = input("Digite um número : \n")
chute = int(chute1)
print ("Voce digitou ", chute, " !")

acertou = (chute == n_secreto)
menor = (chute < n_secreto)
maior = (chute > n_secreto)

if (acertou):
    print ("Acertou , parabens !")
elif (menor):
    print ("Errou ! chute menor que número secreto !")
elif (maior):
    print ("Errou ! chute maior que o número secreto !")


