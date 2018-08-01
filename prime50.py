'''def prime(n):
    nooffact=0
    
    for i in range(1,n+1):
        if n%i==0:
            nooffact+=1
    if nooffact==2:
        return n
for k in range(2,51):
    print(prime(k))'''

count=0
strn=""
for p in range(2,51):
    count=0
    for i in range(1,p+1):
        if p%i==0:
           count+=1
    if count==2:
        strn+=str(p)
        

print(strn)
