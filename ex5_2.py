import sys, time
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallMultiple(num, size):
    for x in xrange(1,size):
        if(num%x!=0):
            return False
        pass
    return True

def searchSmallMultiple(size):
    found = False; num=1
    init = time.time()
    while(found==False):
        if(smallMultiple(num,size)):
            found=True
            print "El menor numero divisible por los primeros {0} numeros es: {1} en {2}sec".format(size, num, time.time();
            return num
        else:
            # print "NUM {0}".format(num)
            num+=1


searchSmallMultiple(20)
