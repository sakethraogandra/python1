def smallnum(n):
    i=1
    count=0
    while True:
        for j in range(1,i+1):
            if i%j==0:
               count+=1
        
        if count==n:
            break
        else:
            count=0
            i+=1
    return i
s=smallnum(12)
print(s)
