# Find sum of even numbers up to N

n = int(input())

sum_even = 0
i = 2

while i <= n:
    sum_even += i
    i += 2

print(sum_even)