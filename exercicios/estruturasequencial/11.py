
altura = float(input ("Digite sua altura : \n"))

sexo = str(input ("Digite (h) para homem ou (m) para mulher : \n"))

homem = (sexo == "h")
mulher = (sexo == "m")

if (homem):

    print ("Seu peso ideal é ", (72.7*altura) - 58, "kg !")

elif (mulher):

    print ("Seu peso ideal é ", (62.1*altura) - 44.7, "kg !")


