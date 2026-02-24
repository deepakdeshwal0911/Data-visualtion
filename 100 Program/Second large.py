# Find second largest number in list

numbers = list(map(int, input().split()))

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)

#Output:
#Enter numbers: 34 67 23 89 12
#67
#Enter numbers: 5 6 5 7 8 6
#7
