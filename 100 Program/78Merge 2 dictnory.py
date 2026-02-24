dict1 = {}
dict2 = {}

n1 = int(input())
for _ in range(n1):
    k, v = input().split()
    dict1[k] = int(v)

n2 = int(input())
for _ in range(n2):
    k, v = input().split()
    dict2[k] = int(v)

# Merge manually
for k, v in dict2.items():
    dict1[k] = v

print(dict1)

#Output:
#Enter number of entries for dict 1: 3
#Enter key and value: a 1
#Enter key and value: b 2
#Enter key and value: c 3
#Enter number of entries for dict 2: 2
#Enter key and value: d 4
#Enter key and value: e 5
#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#Enter number of entries for dict 1: 2

#Enter key and value: x 10
#Enter key and value: y 20
#Enter number of entries for dict 2: 3
#Enter key and value: z 30
#Enter key and value: w 40
#Enter key and value: v 50
#{'x': 10, 'y': 20, 'z': 30, 'w': 40, 'v': 50}

    