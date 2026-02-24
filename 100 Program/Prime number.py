# Print all prime numbers between 1 and N

n = int(input())

for num in range(2, n + 1):
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")

#Output:
#Enter a number: 20
#2 3 5 7 11 13 17 19


