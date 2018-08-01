n=int(input("enter a number"))
n1=n
n2=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<n2:
            print("_",end=" ")
        else:
                
                print(n1,end=" ")
                n1-=1
    print("\n")
    n1=n
    n2=n2-1
