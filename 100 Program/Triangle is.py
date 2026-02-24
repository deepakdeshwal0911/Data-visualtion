
a = float(input())
b = float(input())
c = float(input())


if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Valid Triangle")


#Output:
#Enter a number: 5
#Enter a number: 5
#Enter a number: 5
#Equilateral Triangle
#Enter a number: 5
#Enter a number: 5
#Enter a number: 3
#Isosceles Triangle
#Enter a number: 5
#Enter a number: 4
#Enter a number: 3
#Scalene Triangle
#Enter a number: 1
#Enter a number: 2
#Enter a number: 3
#Not a Valid Triangle

