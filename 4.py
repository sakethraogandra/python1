low=1
high=10
val=int((low+high)/2)
print("think of a number ")
while True:
    print("is this your guess"+str(val))
    ans=input("press h if high press l if low or press c if correct")
    if ans=='h':
        high=val
    elif ans=='l':
        low=val
    elif ans=='c':
        print(str(val)+"is the answer")
        break
    else:
        print("fif not get it")
    val=int((low+high)/2)
