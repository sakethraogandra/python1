n=list(input("enter a string"))
ch=str(input("enter a charecter"))
count=0
for i in n:
    if i==ch:
        count+=1
        n[n.index(i)]=count
print(n)
    
    

            
