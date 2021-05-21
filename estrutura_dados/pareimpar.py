lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
a = set(lista)

for i in a:
    if i % 2 == 0:
        print ("Número PAR : {} !".format(i))
    else:
        print ('Número ÍMPAR : {} !'.format(i))
