# Count vowels using function

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in text:
        if ch in vowels:
            count += 1
            
    return count

s = input()
print(count_vowels(s))
#Output:
#Enter a string: Hello World
#3
#Enter a string: Python Programming
#4
