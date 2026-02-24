# Find factorial using function

def factorial(n):
    if n < 0:
        return "Factorial not defined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input())
print(factorial(num))

#Output:
#Enter a number: 5
#120


