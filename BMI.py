height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI by doing weight divided by height in meters squared
BMI = weight / (height / 100) ** 2

# Print the BMI
print("Your BMI is", BMI, ".")

if BMI < 18.5:
    print("You are underweight. You should start eating much more food to try to gain some weight.")
elif BMI >= 18.5 and BMI < 25:
    print("You are in the healthy weight range. You should keep up the good work and continue to eat healthy and exercise regularly.")    
elif BMI >= 25 and BMI < 30:
    print("You are overweight. You should start eating less food and exercising more to try to lose some weight.")
elif BMI >= 30:
    print("You are obese. You should start eating much less food and exercising much more to try to lose a lot of weight, if not your health is at risk.") 
else:
    print("You have an invalid BMI, so this string has been printed.")          