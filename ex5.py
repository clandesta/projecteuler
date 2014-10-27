num = 1
cnt=0
found = False
divisores = 21
while(found==False):
    for x in xrange(0,divisores):
        if(num%(x+1)==0):
            #print "num: {0} es divisible por {1}".format(num, x)
            cnt=cnt+1
        pass
    if(cnt==divisores-1):
        found=True
        print "Found NUM: ",num
    else:
        cnt=0
        num=num+1

    if(num%1000==0):
        print "num: {0}".format(num)

print "FIN"