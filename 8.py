def re(bal,an,mpr):
    monthlyir =an/12.0
    mminmonpay=mpr*bal
    unpaid=0
    i=1
    unpaid=bal-mminmonpay
    for i in range(13):
             
             bal=unpaid+(monthlyir*unpaid)
             unpaid=bal-mminmonpay
             print("month"+str(i)+"Remaining balance"+str(bal))
             i+=1
    return round(bal,2)
print(re(42,0.2,0.04))
