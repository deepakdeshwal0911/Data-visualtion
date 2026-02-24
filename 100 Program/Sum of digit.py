# Find the sum of digits of a number

num = int(input())

num = abs(num)   # Handle negative numbers
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print(sum_digits)


#Output:
#Enter a number: 123
#6
#Enter a number: -456
#15
#Enter a number: 0
#0



