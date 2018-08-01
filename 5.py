x=28
g=0
inc=0.01
aprox=0.01
count=0

    
while (g**2-x)<aprox and (g**2-x)<0:
    g+=inc
    count+=1
print("guess:"+str(g))
