keys = input().split()
values = list(map(int, input().split()))

d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)
#Output:
#Enter keys: a b c
#Enter values: 1 2 3
#{'a': 1, 'b': 2, 'c': 3}
#Enter keys: x y
#Enter values: 10 20
#{'x': 10, 'y': 20}
