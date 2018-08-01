n=[]
b=int(input("enter size of list"))
for k in range(b):
    c=int(input("enter elements"))
    n.append(c)
print(n)
m=[]
for i in range(b):
    for j in range(i+1,b):
        print(n[i],n[j])
        if n[j]==n[i]:
            
            
            m.append(n[j])
print("repeated numbers",m)
