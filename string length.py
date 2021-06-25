def str(a):
    if a is '':
        return 0
    else:
        return(1+str(a[1: ]))

print(str(''))
        
