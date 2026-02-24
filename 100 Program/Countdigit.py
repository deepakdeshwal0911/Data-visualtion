# Count digits in a number

num = int(input())

num = abs(num)   # Handle negative numbers
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10

print(count)