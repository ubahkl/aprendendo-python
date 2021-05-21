lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

#lista par e impar !
listapares = []
listaimpar = []

#indice index(contador) no looping (0 a 15) = 16 lacos.
for index in range(0,len(lista)):
    
    #o indice vai percorrer a lista comencando de zero 
    if (lista[index] % 2 == 0):
        #vai adicionar os números na lista com a funcao append !
        listapares.append(lista[index])  
        
    else:
        listaimpar.append(lista[index])
        
print ("Esses são os números pares {} !".format(listapares))
print ("Esses são os números impares {} !".format(listaimpar))
