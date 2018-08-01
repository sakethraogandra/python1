s=str(input("enter license"))
l=s.split('-')
o=len(l[0])
m=l[1]
def rotate(st,n):
    return(st[n:]+st[:n])

"""m=[]
g=[]
rot=[]
o=len(l[0])
print(o)
for i in l[1]:
    m.append(i)
print(m)

if o==1:
    k=m[-1]
    m.pop()
    print(k)
    g.append(k)
    rot=g+m
print(rot)"""
