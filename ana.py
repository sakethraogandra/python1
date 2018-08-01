n=str(input("enter a string"))
n1=str(input("enter string to check"))
n2=""
for i in n1:
    if i in n:
        n2+=i
if n2==n1:
    print("its a anagram")
else:
    print("not")
