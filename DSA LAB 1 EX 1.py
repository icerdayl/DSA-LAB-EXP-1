#--------------------------------------------------------------------------------------------------------------------------------------#
# DSA LAB 1 EXRCISE 1
# Programmed by: Ahiezer Dayl P. Dalangin (BSCpE 2-3)
#--------------------------------------------------------------------------------------------------------------------------------------#

# Prompt the user to enter a temperature
try:    
    temp = float(input("Please enter a temperature: "))
except ValueError:
    exit("Invalid input. Please enter numbers only.")

# Prompt the user to choose the type of conversion
conversion = input("Choose your type of Conversion:\nPress: \n1: Celsius to Fahrenheit \n2: Fahrenheit to Celsius \n Enter: ")

# Check if the user chose Celsius to Fahrenheit conversion
if conversion == "1":
    # Convert the temperature from Celsius to Fahrenheit
    result1 = float(temp) * (9/5) + 32
    # Print the result in Fahrenheit
    print(result1, "Degrees Fahrenheit")

# Check if the user chose Fahrenheit to Celsius conversion
elif conversion == "2":
    # Convert the temperature from Fahrenheit to Celsius
    result2 = (float(temp) - 32) * (5/9)
    # Print the result in Celsius
    print(result2, "Degrees Celsius")

# Handle invalid input
else:
    print("Invalid Input")

# End of Program