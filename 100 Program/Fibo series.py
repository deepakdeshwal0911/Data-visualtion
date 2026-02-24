# Generate Fibonacci series using while loop

n = int(input())

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

#Output:
#Enter the number of terms: 10
#0 1 1 2 3 5 8 13 21 34


