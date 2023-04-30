# BMI calculator
# BMI = Weight(kg)/height^2(m2)

print("Welcome To BMI Calculator")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
m2 = height ** 2
BMI = weight / m2
print("Your BMI is " + str(BMI))

if BMI < 18.5:
    print("You are Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You have a Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("You are Overweight")
else:
    print("You have Obesity")

