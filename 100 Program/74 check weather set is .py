set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

if set1.issubset(set2):
    print("Yes")
else:
    print("No")
#Output:
#Enter numbers for set 1: 1 2 3
#Enter numbers for set 2: 1 2 3 4 5
#Yes
#Enter numbers for set 1: 1 2 3
#Enter numbers for set 2: 4 5 6
#No
