# Find GCD using while loop

a = int(input())
b = int(input())

a = abs(a)
b = abs(b)

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)


#Output:
#Enter a number: 48
#Enter another number: 18
#6
#Enter a number: -56
#Enter another number: 98
#14
#Enter a number: 0
#Enter another number: 5
#5


