d = {}
n = int(input())
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

for key in sorted(d.keys()):
    print(key, d[key])

#Output:
#Enter number of entries: 3
#Enter key and value: c 3
#Enter key and value: a 1
#Enter key and value: b 2
#a 1
#b 2
#c 3
#Enter number of entries: 2
#Enter key and value: x 10
#Enter key and value: y 20
#x 10
#y 20

