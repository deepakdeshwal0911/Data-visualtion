# Print all divisors of a number

num = int(input())

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

#Output:
#Enter a number: 12
#1 2 3 4 6 12
#Enter a number: 15
#1 3 5 15


