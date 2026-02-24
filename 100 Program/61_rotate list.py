numbers = list(map(int, input().split()))
k = int(input())

k = k % len(numbers)   # Handle large K

rotated = numbers[k:] + numbers[:k]


print(*rotated)
#Output:
#Enter numbers: 1 2 3 4 5
#Enter K: 2
#3 4 5 1 2
#Enter numbers: 10 20 30 40 50
#Enter K: 3
#40 50 10 20 30
