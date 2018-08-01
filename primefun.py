def prime(n):
    nooffact=0
    
    for i in range(1,n+1):
        if n%i==0:
            nooffact+=1
    if nooffact==2:
        print("it is a prime number"+str(nooffact))
    else:
        print("not a prime"+str(nooffact))
s=prime(2)
print(s)
