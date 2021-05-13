

"""
This program is a Body Mass Index (BMI) calculator.
This calculator is used to measure the body fat of a person based on their height and weight.
The user will input their height (in centimeters) and the weight (in kilograms).
The program will calculate whether they are underweight, healthy, overweight, extremely overweight, obese or extremely obese.

BMI will be set to: weight / (height/100)**2(squared)

A BMI of <= 18.4
    print("You are underweight.")
A BMI of <= 24.9
    print("You are healthy.")
A BMI of <= 29.9
    print("You are overweight.")
A BMI of <= 34.9
    print("You are extremely overweight.")
A BMI of <= 39.9
    print("You are obese.")
A BMI of => 39.9
    print("You are extremely obese.")

"""

"""
try:
    height = float(input("Enter your height in CM: "))
except NameError:
    print("\nYou failed to input a number.")
    print("\nPlease don't do this again.")
except ZeroDivisionError:
    print("\nOne of your inputs is a zero. That's impossible.")
try:
    weight = float(input(Enter your weight in KG: "))
except NameError:
    print("\nYou did it again...")


BMI = weight / (height/100)**2

print("You BMI is: ", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are extremely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are extremely obese.")

"""

a = " Hello, this is a BMI calculator. It is a measure of body fat based on height and weight that applies to adult men and women and is endorsed by the U.S. Department of Health & Human Services." #brief intro
b = " This calculator will assess your measurements and output whether you classify as underweight, healthy, overweight, extremely overweight, obese, extremely obese."
c = " Please input your measurements into the following questions."
d = a + b + c
print(d)


try: #helps let the user know if they make an invalid input
    height = float(input("Enter your height in CM: "))
except ValueError: 
    print("\nThat is not a number.")
    print("\nPlease don't do this again.")
except NameError:
    print("\nYou failed to input a number.")
    print("\nPlease don't do this again.")
except ZeroDivisionError:
    print("\nOne of your inputs was a 0. That's impossible.")
try:
    weight = float(input("Enter your weight in KG: "))
except ValueError:
    print("\nYou did it again...")
except NameError:
    print("\nYou did it again...")
    

BMI = weight / (height/100)**2 #calculation for BMI

print("Your BMI is: ", BMI)

if BMI <= 18.4:
    print("According to the BMI calculator, you are underweight.")
elif BMI <= 24.9:
    print("According to the BMI calculator, you are healthy.")
elif BMI <= 29.9:
    print("According to the BMI calculator, you are overweight.")
elif BMI <= 34.9:
    print("According to the BMI calculator, you are extremely overweight.")
elif BMI <= 39.9:
    print("According to the BMI calculator, you are obese.")
else:
    print("According to the BMI calculator, you are extremely obese.")

thank_you_note = ("Thank you for using this BMI calculator.")
print(thank_you_note)
