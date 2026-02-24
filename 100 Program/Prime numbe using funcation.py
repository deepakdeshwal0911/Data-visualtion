# Check prime number using function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input())

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
#Output:
#Enter a number: 7
#Prime
#Enter a number: 10
#Not Prime


