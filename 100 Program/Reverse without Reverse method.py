# Reverse a list without using reverse() method

numbers = list(map(int, input().split()))

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(*reversed_list)

#Output:
#Enter numbers: 34 67 23 89 12
#12 89 23 67 34
#Enter numbers: 5 6 5 7 8 6
#6 8 7 5 6 5
