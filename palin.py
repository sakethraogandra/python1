n=str(input("enter a number or a string"))
rev=""
rev=n[::-1]
if n==rev:
    print("palindrome")
else:
    print("not a palin")
