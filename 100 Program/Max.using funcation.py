# Find maximum of three numbers using function

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_max(num1, num2, num3))


#Output:
#Enter a number: 5
#Enter a number: 10
#Enter a number: 3
#10

