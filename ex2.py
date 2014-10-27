def fibonnacci(n):
    fibonacciAnterior = 1
    fibonacciActual = 0
    k = 0
    while k <= n-1:
        sumaFibonacci = fibonacciAnterior+fibonacciActual
        fibonacciAnterior = fibonacciActual
        fibonacciActual = sumaFibonacci
        k+=1
    return fibonacciActual


res =0
for x in xrange(0,3999999):
    fib = fibonnacci(x)
    if(fib >= 4000000):
        break
    else:
        if(fib%2==0):
            res += fib

print res
