"""

Greatest common divisor

"""

def gcd(a,b):

    if a < b :

        a, b = b, a

    if a % b == 0 :

        return b

    else :

        # r = a % b
        # a = b
        # b = r
        return gcd(b, a % b)

print(gcd(4,28))



