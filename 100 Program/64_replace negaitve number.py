numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(*numbers)
#Output:
#Enter numbers: 1 -2 3 -4 5
#1 0 3 0 5
#Enter numbers: -10 20 -30 40 -50
#0 20 0 40 0
