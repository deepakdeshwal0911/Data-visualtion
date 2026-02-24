# Generate Fibonacci series using function

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input())
fibonacci(num)

#Output:
#Enter the number of terms: 10
#0 1 1 2 3 5 8 13 21 34
