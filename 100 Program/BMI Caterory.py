# Calculate BMI and Category

weight = float(input())   # in kilograms
height = float(input())   # in meters

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


#Output:
#Enter weight in kg: 70
#Enter height in meters: 1.75
#22.857142857142858
#Normal Weight

