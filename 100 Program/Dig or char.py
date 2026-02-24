# Check whether a character is digit or alphabet

ch = input().strip()

if len(ch) == 1:
    if ch.isdigit():
        print("Digit")
    elif ch.isalpha():
        print("Alphabet")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")


#Output:
#Enter a character: A
#Alphabet
#Enter a character: 5
#Digit
#Enter a character: @
#Invalid Input
#Enter a character: AB
#Invalid Input


