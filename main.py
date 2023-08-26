
#Create Function to Calculate BMI 
def calculate_bmi(weight,height):
    BMI = weight / (height **2) #
    return BMI

#Function to interpret BMI and Return the Status of body
def interpret_bmi(bmi):
    if bmi < 18.5: #if bmi less than 18.5 return status message  Underweight
        return "Underweight"
    elif bmi <=18.5 or bmi < 25:#if bmi between 18.5 and less than 25 return status message  Normal weight
        return "Normal weight"
    elif bmi <=25 or bmi < 30:#if bmi between 25 and less than 30 return status message  Overweight
        return "Overweight"
    else:
        #if bmi greater then 30 or Otherways return status message  Obese
        return "Obese"




weight=float(input("Enter the weight in kilograms...."))#Store weight from the user in variable weight
height=float(input("Enter the height in metres..."))#Store height from the user in variable height
#Call function calculate_bmi and the reterned value of calculate_bmi function pass as the argument to the interpret_bmi to print body status
print(interpret_bmi(calculate_bmi(weight,height)))

#end of code 
