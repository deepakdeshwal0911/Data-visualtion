# Find GCD using function

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

print(find_gcd(num1, num2))

#Output:
#Enter a number: 48
#Enter a number: 18
#6

