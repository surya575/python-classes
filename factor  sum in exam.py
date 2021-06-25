##n=int(input())
##f=int(input())
##c=0
##def fact(n,f,c):
##    for i in range(1,n+1):
##        if n%i==0:
##            c+=1
##            if c==f:
##                return i
##    else:
##        return 0
##
##print(fact(n,f,c




##n=int(input())
##f=int(input())
##c=0
##def fact(n,f,c):
##    for i  in range(1,n//2+1):
##        if n%i==0:
##            c+=1
##            if c==f:
##                return i
##        else:
##            return 0
##        
##print(fact(n,f,c))        
##        





n=int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()  
