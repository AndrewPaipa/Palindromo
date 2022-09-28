#subcadena Palindromo mas largo de una expresion (cadena mas grande)

def funtionPalindromo(expression):
    longExpression = len(expression)                    #Longitud de la cadena entrante
    subStrVector = []                                   #Vector de subcadenas
    vr = -1                                             #Variable de return
    
    for i in range(1,longExpression):                   #Bucle de 1 a longitud - 1  // empueza por la subcadena más grande "todo el str"
        invested = (longExpression + 1) - i             #Valculo de repeticione de subcadena

        for j in range(0,i):                            #Barrido de subcadenas en la cadena 
            subStr = expression[j:(j+invested)]         #Sub cadena 

            if subStr == subStr[::-1]:                  #Comprobando palindromo  
                subStrVector.append(subStr)             #Vector para validar si hay más de un solo palindromo del tamaño más largo
                vr = invested
        
        if vr != -1:                                    #Validación de return
            if subStrVector == []:                      #Si el vector esta vacio o no
                return(None)
            else:
                return(subStrVector)