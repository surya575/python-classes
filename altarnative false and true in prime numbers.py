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
##print(prime1(5))

            
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



##def fact(n):
##    f=1
##    for i in range(1,n+1):
##        f*=i
##    print(f)
##
##n=int(input('enter a number: '))
##print(fact(n))    
##
##

        
##







##def st(a):
##    if a is ' ':
##        return 0
##    else:
##        return(1+st(a[1: ]))
##    
##print(st('jayafjfjf '))               
##




##
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##        else:
##            return True
##def rev(n):
##    a=n
##    r=0
##    while n:
##        rem=n%10
##        r=r*10+rem
##        n=n//10
##    return(r)
##
##    
##        
##        
##n=int(input('enter a number: '))
##if prime(n) and prime(rev(n)):
##    print(True)
##else:
##    print(False)
     
##      
##
##
##for i in range(1,n+1):
##    for k in range




