# Calculate power without using exponent operator

base = int(input())
exponent = int(input())

result = 1

for i in range(exponent):
    result = result * base

print(result)

#Output:
#Enter the base: 2
#Enter the exponent: 3
#8
#Enter the base: 5
#Enter the exponent: 4
#625

