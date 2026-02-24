# Calculate power using recursive function

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

b = int(input())
e = int(input())

print(power(b, e))


#Output:
#Enter the base: 2
#Enter the exponent: 3
#8
