# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Ask user for input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI and print result
bmi = calculate_bmi(weight, height)
print("Your BMI is:", round(bmi, 2))

# Determine BMI category and recommend diet
if bmi < 18.5:
    print("You are underweight. You should consider eating more carbohydrates and proteins to gain weight.")
elif 18.5 <= bmi <= 24.9:
    print("You are of normal weight. Keep up the good work!")
elif 25 <= bmi <= 29.9:
    print("You are overweight. You should consider eating fewer carbohydrates and more vegetables to lose weight.")
else:
    print("You are obese. You should consider eating a low-calorie diet and getting regular exercise.")
