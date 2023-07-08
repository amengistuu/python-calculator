# Design and implement a simple calculator program in Python that takes user input for two numbers 
# and performs basic arithmetic operations (addition, subtraction, multiplication, division). 
# The program should provide a user-friendly interface and handle invalid inputs gracefully.
import sys

exit_program = False # flag variable

def set_exit_program():
    global exit_program
    exit_program = True # prevents the program from restarting from the beginning
    sys.exit()  # Exit the program

def main():
    # ask user what do they want to do (add, subtract, multiply, or divide)
    # ask user for the numbers that they want to operate on
        # handle invalid numbers with exceptions based on operation
    # return result of operation to the user

    # global exit_program # we need to declare the variable as global inside the main() function
    while True:
        operation = str(input("""Select the mathematical operation you want to do:
-- Addition
-- Subtraction
-- Multiplication
-- Division

Type "exit" to stop this program.
"""))

        if operation.lower() == "addition":
            # validation for first number
            while True:
                num1 = input("First number: ")
                if num1.lower() == "exit":
                    set_exit_program()
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # validation for second number
            while True:
                num2 = input("Second number: ")
                if num2.lower() == "exit":
                    set_exit_program()
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # calculate the result
            result = num1 + num2
            
            # dispay the result as int if it ends in .0
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            print(formatted_result)
        
        elif operation.lower() == "subtraction":
            # validation for first number
            while True:
                num1 = input("First number: ")
                if num1.lower() == "exit":
                    set_exit_program()
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # validation for second number
            while True:
                num2 = input("Second number: ")
                if num2.lower() == "exit":
                    set_exit_program()
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # calculate the result
            result = num1 - num2

            # dispay the result as int if it ends in .0
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            print(formatted_result)
        elif operation.lower() == "multiplication":
            # validation for first number
            while True:
                num1 = input("First number: ")
                if num1.lower() == "exit":
                    set_exit_program()
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # validation for second number
            while True:
                num2 = input("Second number: ")
                if num2.lower() == "exit":
                    set_exit_program()
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # calculate the result
            result = num1 * num2

            # dispay the result as int if it ends in .0
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            print(formatted_result)
        elif operation.lower() == "division":
            # validation for first number
            while True:
                num1 = input("First number: ")
                if num1.lower() == "exit":
                    set_exit_program()
                try:
                    num1 = float(num1)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # validation for second number
            while True:
                num2 = input("Second number: ")
                if num2.lower() == "exit":
                    set_exit_program()
                try:
                    num2 = float(num2)
                    break
                except ValueError:
                    print("You must type in a number.")
                except Exception as e:
                    print(f"An error occured: {str(e)}")
            
            # calculate the result
            result = num1 / num2

            # dispay the result as int if it ends in .0
            if result.is_integer():
                formatted_result = int(result)
            else:
                formatted_result = result
            print(formatted_result)
        elif operation.lower() == "exit":
            set_exit_program()
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()