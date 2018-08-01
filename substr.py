s=str(input("enter string of numbers"))
m=[]
l=""
summ=0
for i in range(len(s)):
    summ=0
    for j in range(i,len(s)):
       
           
        print(s[i],s[j])
        summ+=int(s[j])
        print(summ)
        
       
        
        if summ==10 :
            l=s[i:j+1]
            
           
            print(l)
            m.append(l)
           
           
        if summ>10:
            summ=0
            break
        else:
            
            continue
print(m)
