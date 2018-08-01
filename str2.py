n=int(input("enter a number"))
p=""

for i in range(1,n+1):
    if n%i==0:
       p+=str(i)
print((p))
