#--------------------------------------------------------------------------------------------------------------------------------------#
# DSA LAB 1 EXRCISE 2
# Programmed by: Ahiezer Dayl P. Dalangin (BSCpE 2-3)
#--------------------------------------------------------------------------------------------------------------------------------------#

try:
    # Prompt the user to choose what they want to calculate
    value = input("What do you want to calculate? \n Choose a number \n1. Voltage \n2. Current \n3. Resistance \n Enter:")

    # Check if the user chose to calculate Voltage
    if value == "1":
        # Prompt the user to enter the value of current
        curr = input("Enter the value of current: ")
        # Prompt the user to enter the value of resistance
        res = input("Enter the value of resistance: ")
        # Calculate the voltage using Ohm's Law (V = I * R)
        volt = int(curr) * int(res)
        # Print the calculated voltage
        print("Voltage: ", volt)

    # Check if the user chose to calculate Current
    elif value == "2":
        # Prompt the user to enter the value of voltage
        voltage = input("Enter the value of voltage: ")
        # Prompt the user to enter the value of resistance
        res = input("Enter the value of resistance: ")
        # Calculate the current using Ohm's Law (I = V / R)
        current = int(voltage) / int(res)
        # Print the calculated current
        print("Current: ", current)

    # Check if the user chose to calculate Resistance
    elif value == "3":
        # Prompt the user to enter the value of voltage
        voltage = input("Enter the value of voltage: ")
        # Prompt the user to enter the value of current
        curr = input("Enter the value of current: ")
        # Calculate the resistance using Ohm's Law (R = V / I)
        resistance = int(voltage) / int(curr)
        # Print the calculated resistance
        print("Resistance: ", resistance)

    # Handle invalid input
    else:
        print("Invalid input.")

# Handle division by zero errors
except ZeroDivisionError as E:
    print(E)
# Handle value errors
except ValueError as v:
    print(v)

# End of program