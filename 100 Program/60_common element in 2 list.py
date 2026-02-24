list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print(*common)
#Output:
#Enter first list: 1 2 3 4
#Enter second list: 3 4 5 6
#3 4
#Enter first list: 5 6 7
#Enter second list: 6 7 8
#6 7
