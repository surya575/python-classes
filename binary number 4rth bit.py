##n=int(input('enter a number: '))
##a=0
##b=1
##print(a,b,end=' ')
##for i in range(3,n+1):
##    c=a+b
##    a=b
##    b=c
##    print(b,end=' ')


##
##
##def add(a,b):
##    print(a+b)
##def sub(a,b):
##    print(a-b)
##def mul(a,b):
##    print(a*b)
##def dev(a,b):
##    print(a/b)
##
##a=int(input('enter a number: '))
##b=int(input('enter a number: '))
##print()
##c=int(input('enter a choice: '))
##
##
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##else:
##    dev(a,b)



##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            print('False')
##            break
##        
##        else:
##            print('True')
##
##
##def prime1(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##        else:
##            return True
##
##
##prime(5)
##print(prime1(6))
##
##            
##
##a=int(input('enter a number: '))
##if prime(a):
##    print(a,'is prime')
##while True:
##    a+=1
##    if prime(a):
##        print(a,'is prime')
##        break
##

##
##def prime111(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##        else:
##            return True
##
##
##prime(6)
##print(prime111(6))
##        
##    
    






n=int(input())
n=bin(n)
print('binary',n)
n=n[2:]
print('proper binary',n)

n=n[::-1]
print('reversed',n)
print(n[3])










##n=int(input('enter a number: '))
##rem=0
##s=''
##while True:
##    rem=n%2
##    print(rem)
##    s+=str(rem)
##    n=n//2
##    if n<=1:
##        print(1)
##        s+=str(1)
##        break
##
##s=s[::-1]
##print('4rth bit',s[3])
##



