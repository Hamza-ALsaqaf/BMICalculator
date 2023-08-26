def calculate_bmi(weight,height):
    BMI = weight / (height **2)
    return BMI

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <=18.5 or bmi < 25:
        return "Normal weight"
    elif bmi <=25 or bmi < 30:
        return "Overweight"
    else:
        return "Obese"




weight=float(input("Enter the weight in kilograms...."))
height=float(input("Enter the height in metres..."))
print(interpret_bmi(calculate_bmi(weight,height)))
