# Check whether a number is Armstrong

num = int(input())

original = num
num = abs(num)

digits = len(str(num))
sum_power = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum_power += digit ** digits
    temp = temp // 10

if sum_power == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


#Output:
#Enter a number: 153
#Armstrong Number
#Enter a number: 123
#Not an Armstrong Number
#Enter a number: -370
#Armstrong Number


