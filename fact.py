n=int(input("enter a number"))
l=1
if n==0:
    print("fact is"+str(1))
else:
    for i in range(1,n+1):
        l=n*l
        n=n-1
    
print(str(l))
