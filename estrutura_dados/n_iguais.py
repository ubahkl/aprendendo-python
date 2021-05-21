lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

maiorelemento = lista[0]
menorelemento = lista[0]
soma_negativos = []
lista_par = []
lista_impar = []
lista_igual = []
soma_nega = 0

for i in range(0,len(lista)):
    if (menorelemento > lista[i]):
        menorelemento = lista[i]
        
    elif (maiorelemento < lista[i]):
        maiorelemento = lista[i]
        
    if (lista[i] % 2 == 0):
        lista_par.append(lista[i]) 
    else:
        lista_impar.append(lista[i])
        
    if lista[i] < 0:
        soma_negativos.append(lista[i])
        soma_nega = soma_nega + lista[i]
        
        
        
        
        
        
        
        
        
    lista_igual.append(lista[i])
        
    

print (menorelemento)
print (maiorelemento)
print (set(lista_par))
print (set(lista_impar))
print (lista_igual)
print (soma_negativos)
print (soma_nega)
        
        


