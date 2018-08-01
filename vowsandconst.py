n=str(input("enter a string"))
vowels=0
const=0
for j in n:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        vowels+=1
    else:
        const+=1
print("vowels"+" "+str(vowels)+"   Consonants"+" "+str(const))
