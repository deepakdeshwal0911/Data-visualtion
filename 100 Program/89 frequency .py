s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for k, v in freq.items():
    print(k, v)
#Output:
#Enter a string: hello
#h 1
#e 1
#l 2
#o 1
#Enter a string: programming
#p 1
#r 2
#o 1
#g 2
#a 1
#m 2
#i 1
#n 1
