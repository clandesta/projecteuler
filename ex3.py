import math,time

def find_prime_factors(n):
    remaining = n
    primefactors = []
    while remaining != 1:

        if primefactors == []:
            i=1
        else:
            i=primefactors[len(primefactors)-1]-1
            
        # print "remaining:{0}, i:{1}".format(remaining,i)
        while i < remaining:
            i+=1
            # print "-->remaining:{0}, i:{1}".format(remaining,i)
            if remaining%i == 0:
                # print "---->remaining:{0}, i:{1}".format(remaining,i)
                remaining = remaining/i
                primefactors.append(i) 
                break
    return primefactors

def factorialGzip(x):
    d = 3
    expn = []
    while (d * d < x):
        if x % d == 0: 
            expn.append(d*d)
            x /= d
        else: 
            d += 2
    print expn
    return x
   
num=600851475143
x=600851475143

#print "{0} es primo?, {1}".format(num,isPrimo(num))
t0 = time.time()
print "find_prime_factors {0}, se demoro:{1:.3f}".format(find_prime_factors(num), time.time()-t0 )
t0 = time.time()
print "factorialGzip {0}, se demoro:{1:.3f}".format(factorialGzip(num), time.time()-t0 )

