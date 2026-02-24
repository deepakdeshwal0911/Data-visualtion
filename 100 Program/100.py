s = input()
compressed = ''
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    compressed += s[i] + str(count)
    i += 1
print(compressed)   
#Output:
#Enter a string: aaabbc
#a3b2c1
#Enter a string: Hello
#H1e1l2o1

    