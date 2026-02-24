# Reverse a number using while loop

num = int(input())

sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(sign * reverse)

#Output:
#Enter a number: 123
#321
#Enter a number: -456
#-654
#Enter a number: 0
#0

