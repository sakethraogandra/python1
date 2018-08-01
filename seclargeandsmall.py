n=list(input("enter numbers in a list"))
'''large=0
seclarge=0
for i in n:
    if int(i)>large:
        seclarge=large
        large=int(i)
print(seclarge)'''
small=int(n[0])
secsmall=0
for i in n:
    if int(i)<small:
        secsmall=small
        small=int(i)
print(secsmall)
