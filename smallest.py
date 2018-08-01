s=list(input("enter elements in a list"))
small=s[0]
for i in s:
    for j in s:
        if j<i:
            small=j
print("smallest number="+str(small))
