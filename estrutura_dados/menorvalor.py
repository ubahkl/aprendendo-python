
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

menorvalor = lista[0]
maiorvalor = lista[0]

for contador in range(0,len(lista)):
    if (menorvalor > lista[contador]):
        menorvalor = lista[contador]
        
    elif (maiorvalor < lista[contador]):
        maiorvalor = lista[contador]
        
        
print ("O menor valor é {} !".format(menorvalor))

print ("O maior valor é {} !".format(maiorvalor))