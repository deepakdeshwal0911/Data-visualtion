t = tuple(map(int, input().split()))

if len(t) == len(set(t)):
    print("All Unique")
else:
    print("Not Unique")
#Output:
#Enter numbers: 1 2 3 4 5
#All Unique
#Enter numbers: 1 2 3 2 5
#Not Unique
    