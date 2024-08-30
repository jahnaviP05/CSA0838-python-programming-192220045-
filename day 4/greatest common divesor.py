def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return 
print(gcd(48, 18))  
print(gcd(100, 25)) 
