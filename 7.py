def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i=0
    while i<exp:
          base*=base
          i+=1
    return base
print(iterPower(3,5))
