("Welcome to Health check")

name = input("Enter your name:")
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter: "))

BMI = weight / (height * height)

print("\n--- Health Report ---")
print("Name:", name)
print("Weight:", weight)
print("Height:",height)
print("BMI:",round(BMI,2))

if BMI < 18.5:
    print("you are underweight")
elif BMI  >= 18.5 and BMI  < 30:
    print("you are normal")
elif BMI  >= 25 and BMI < 30:
    print("you are overweight")
else:
    print("you are obese")
    


