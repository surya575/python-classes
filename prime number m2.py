n=int(input('enter a number: '))
import math
s=int(math.sqrt(n))
c=0
for i in range(1,s+1):
    if n%i==0:
        c+=1
if c>1:
            print(n,'is not a prime number')
else:
                print(n,'is a prime')
