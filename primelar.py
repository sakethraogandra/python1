def maxprime(n):
    m=[]
    
    j=1
    count=0
    
    for i in range(2,n+1):
        
        if n%i==0:
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count==2:
                m.append(i)
                count=0
    print(m)
    s=max(m)
    print(s)
    return s
z=int(input("enter a number for sum"))
summ=0
for l in range(9):
    v=maxprime(z)
    
    summ+=v
    z+=1
print(summ)
    
