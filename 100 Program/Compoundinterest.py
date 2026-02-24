p=float(input("Enter Principal: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time: "))

amount = p * (1 + r / 100) ** t
ci = amount - p
print(ci)


#Output:
#Enter Principal: 1000
#Enter Rate of Interest: 5
#Enter Time: 2
#102.5


