

ch = input().strip()

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")


#Output:
#Enter a character: A
#Vowel
#Enter a character: b
#Consonant
#Enter a character: 1
#Invalid Input


