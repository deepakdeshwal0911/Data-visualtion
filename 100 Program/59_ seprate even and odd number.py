numbers = list(map(int, input().split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", *even)
print("Odd:", *odd)

#Output:
#Enter numbers: 1 2 3 4 5 6
#Even: 2 4 6
#Odd: 1 3 5
#Enter numbers: 7 8 9 10 11
#Even: 8 10
#Odd: 7 9 11
