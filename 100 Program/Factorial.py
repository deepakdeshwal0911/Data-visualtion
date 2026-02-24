# Find factorial using while loop

num = int(input())

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)


#Output:
#Enter a number: 5
#120
#Enter a number: 0
#1
#Enter a number: 1
#1


