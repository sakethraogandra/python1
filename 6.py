x=25

low=1
high=x
delta=0.01
g=(low+high)/2

while abs(g**2-x)>= delta:
    if g**2>x:
        high=g
    elif (g**2<x):
        low=g
    g=(high+low)/2
print("guess"+str(g))
