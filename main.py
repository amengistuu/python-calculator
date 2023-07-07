# Design and implement a simple calculator program in Python that takes user input for two numbers 
# and performs basic arithmetic operations (addition, subtraction, multiplication, division). 
# The program should provide a user-friendly interface and handle invalid inputs gracefully.

def main():
    # ask user what do they want to do (add, subtract, multiply, or divide)
    # ask user for the numbers that they want to operate on
        # handle invalid numbers with exceptions based on operation
    # return result of operation to the user
    while True:
        operation = str(input("""Select the mathematical operation you want to do:
-- Addition
-- Subtraction
-- Multiplication
-- Division

Type "exit" to stop this program.
"""))

        if operation.lower() == "addition":
            pass
        elif operation.lower() == "subraction":
            pass
        elif operation.lower() == "multiplication":
            pass
        elif operation.lower() == "division":
            pass
        elif operation.lower() == "exit":
            break
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()