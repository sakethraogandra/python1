n=str(input("enter a number"))
ans=0
for i in n:
    ans+=pow(int(i),3)
if n==str(ans):
    print("arm",str(ans))
else:
    print("not arm",str(ans))
    
    
