#subcadena Palindromo mas largo de una expresion (cadena mas grande)

def funtionPalindromo(expression):

    longExpression = len(expression)                    #longitud de la cadena entrante
    subStrVector = []
    
    for i in range(1,longExpression):                   #bucle de 1 a longitud - 1  // empueza por la subcadena más grande "todo el str"

        invested = (longExpression + 1) - i             #calculo de repeticione de subcadena

        for j in range(0,i):                            #barrido de subcadenas en la cadena 

            
            subStr = expression[j:(j+invested)]         #Sub cadena 


            if subStr == subStr[::-1]:                  #Comprobando palindromo  

                subStrVector.append(subStr)             #Vector para validar si hay más de un solo palindromo del tamaño más largo
        
    if subStrVector == []:                              #si el vector esta vacio o no
        return(None)
    else:
        return(subStrVector)