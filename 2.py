s=input("enter string")
a="bob"
count=0
for i in range(len(s)):
    if s[i:i+3]==a:
        count=count+1
print(count)
