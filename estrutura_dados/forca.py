palavra_secreta = "banana"

acertou = False
enforcou = False

while (not acertou and not enforcou):
    
    chute = input("Qual letra :")
    
    posicao = 0 
    
    for letra in palavra_secreta:
        
        print (letra)
        
        
        if (chute.upper() == letra.upper()):
            
            print ("Encontrei a letra {} na posição {}".format(letra,posicao))
            
            posicao = posicao + 1 
            
            print ("Jogando ...")
            
            
            
            
            