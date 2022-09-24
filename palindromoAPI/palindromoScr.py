#subcadena Palindromo mas largo de una expresion (cadena mas grande)

def funtionPalindromo(expression):

    longExpression = len(expression)                    #longitud de la cadena entrante
    
    for i in range(1,longExpression):                   #bucle de 1 a longitud - 1  // empueza por la subcadena más grande "todo el str"

        for j in range(0,i):                            #barrido de subcadenas en la cadena 

            invested = (longExpression + 1) - i         #calculo de repeticione de subcadena
            subStr = expression[j:(j+invested)]         #Sub cadena 

            if subStr == subStr[::-1]:                  #Comprobando palindromo  

                return(subStr)
    