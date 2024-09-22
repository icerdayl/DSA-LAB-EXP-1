#--------------------------------------------------------------------------------------------------------------------------------------#
# DSA LAB 1 EXRCISE 3
# Programmed by: Ahiezer Dayl P. Dalangin (BSCpE 2-3)
#--------------------------------------------------------------------------------------------------------------------------------------#

# Prompt the user to enter an odd number
n = int(input("Enter an odd number: "))

# Check if the entered number is even
if n % 2 == 0:
    # If the number is even, print an error message
    print("Please provide an odd integer.")
else:
    # If the number is odd, proceed to print the pattern

    # First part: Print the top half of the diamond
    for i in range(1, n + 1, 2):
        # Calculate the number of spaces and asterisks for the current row
        blank = ' ' * ((n - i) // 2)
        star = '*' * i
        # Print the current row
        print(blank + star)
    
    # Second part: Print the bottom half of the diamond
    for i in range(n - 2, 0, -2):
        # Calculate the number of spaces and asterisks for the current row
        blank = ' ' * ((n - i) // 2)
        star = '*' * i
        # Print the current row
        print(blank + star)

# End of program