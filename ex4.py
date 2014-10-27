def isPalindromo(var):
    #Dar vuelta la cadena y comparar que sean iguales.
    if var==var[::-1]:
        return True
    else:
        return False

ganador = 0
numAux = 0
for x in xrange(999,1,-1):
    for y in xrange(999,1,-1):
        numAux = x*y
        if( isPalindromo(str(numAux)) and numAux>ganador ):
            ganador=numAux
        pass
    pass

print ganador;
