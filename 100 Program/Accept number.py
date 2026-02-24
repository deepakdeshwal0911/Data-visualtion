# Accept numbers until 0 is entered and print sum

total = 0

while True:
    num = int(input())
    
    if num == 0:
        break
    
    total += num

print(total)

#Output:
#Enter a number: 5
#Enter a number: 10
#Enter a number: -3
#Enter a number: 0
#12


