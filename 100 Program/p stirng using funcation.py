# Check palindrome string using function

def is_palindrome(text):
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return text == reversed_text

s = input()

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
#Output:
#Enter a string: madam
#Palindrome
#Enter a string: hello
#Not Palindrome


