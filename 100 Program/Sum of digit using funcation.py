# Find sum of digits using function

def sum_of_digits(n):
    n = abs(n)          # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input())
print(sum_of_digits(num))

#Output:
#Enter a number: 123
#6
#Enter a number: -456
#15
#Enter a number: 0
#0
