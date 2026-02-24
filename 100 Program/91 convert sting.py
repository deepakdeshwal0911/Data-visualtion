s = input()
words = s.split()
title_case = ''
for w in words:
    title_case += w[0].upper() + w[1:].lower() + ' '
print(title_case.strip())
#Output:
#Enter a string: hello world
#Hello World
#Enter a string: this is a test

#This Is A Test
