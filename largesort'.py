a=list(input("enter numbers in list"))
temp=0

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j+1] > a[j]:
            t = a[j]
            a[j ]=a[j+1]
            a[j+1] = t
print(a)
