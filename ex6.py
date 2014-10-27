def ex6():
    sumas = 0
    cuadrados = 0
    for x in xrange(1,101):
        cuadrados += pow(x,2)
        sumas +=x 
        pass
    print (pow(sumas,2))
    print cuadrados
    print "Resultado ", (pow(sumas,2)) - cuadrados

ex6()