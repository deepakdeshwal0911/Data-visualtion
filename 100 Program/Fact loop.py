# Find factorial using for loop

num = int(input())

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)

#Output:
#Enter a number: 5
#120
#Enter a number: 0
#1
#Enter a number: 1
#1


