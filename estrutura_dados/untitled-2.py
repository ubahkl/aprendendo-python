#f) imprima a soma dos elementos de valor negativo


lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
soma = 0

for i in lista:
    
    if i < 0:
        print ("Este número é negativo : {} !".format(i))
        
        soma = soma + i 
        
        
print ("A soma de todos os números negativos é {} !".format(soma))