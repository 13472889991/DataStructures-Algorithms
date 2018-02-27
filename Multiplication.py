from math import ceil
def karatsuba(a,b):
    
    if a < 10 and b < 10: 
        return a*b
    
    n = max(len(str(a)), len(str(b)))
    
    m = int(ceil(float(n)/2))
    
    a1 = int(a // 10**m)
    
    a2 = int(a % (10**m))
              
    b1 = int(b // 10**m)
              
    b2 = int(b % (10**m))
              
    a = karatsuba(a1,b1)
              
    d = karatsuba(a2,b2)
              
    e = karatsuba(a1 + a2, b1 + b2) -a -d
    
    return int(a*(10**(m*2)) + e*(10**m) + d)
