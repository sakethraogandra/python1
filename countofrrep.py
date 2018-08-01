n=list(input("enter numbers"))
count=0
m=[]

for i in n:
    if i not in m:
        
       count=0
       for j in n:
         if i==j:
             count+=1
       print(i+"-"+str(count))
       m.append(i)
            
