set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

difference_set = set1 - set2
print(*difference_set)
#Output:
#Enter numbers for set 1: 1 2 3
#Enter numbers for set 2: 3 4 5
#1 2
#Enter numbers for set 1: 10 20 30
#Enter numbers for set 2: 20 40 50
#10 30
