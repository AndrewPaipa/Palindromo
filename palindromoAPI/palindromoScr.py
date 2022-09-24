#subcadena Palindromo mas largo de una expresion (cadena mas grande)

def funtionPalindromo(expression):

    longExpression = len(expression)
    
    for i in range(1,longExpression):

        for j in range(0,i):

            invested = (longExpression + 1) - i
            subStr = expression[j:(j+invested)]

            if subStr == subStr[::-1]:

                return(subStr)
    