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




##
##n=int(input()
##
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(chr(64+j),end=' ')
####    print()
####
####
##
##
##
##
##n=int(input()
##for i in range(65,65+n):
##    for j in range(65,i+1):
##        print(chr(j),end=" ")
##     print()
##
##
##


##
##
##
##



##
##n=int(input('enter a number: '))
##f=int(input('enter a number: '))
##c=0
##i=1
##def fact(n,f,c,i):
##    if i>n:
##        return 0
##    if n%i==0:
##        c+=1
##        if c==f:
##            return i
##        else:
##            return fact(n,f,c,i+1)
##    else:
##         return fact(n,f,c,i+1)
##
##
##
##print(fact(n,f,c,i))        








def cp(n):
    if n==1 or n==2 or n==3 or n==5 or n==7:
        return 0
    if n==4 or n==6 or n==9 or n==0:
        return 1
    else:
        return 2


def cpsum(t):
    s=0
    while t:
        rem=t%10
        t=t//10
        s+=cp(rem)
        return s
    
t=int(input())
print(cpsum())





