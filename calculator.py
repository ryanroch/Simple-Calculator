# Author: Ryan Rochmanofenna
# Assignment #2 - Calculator
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def print_menu():

    print("\n1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")

def do_addition():
    print("""
You have chosen the addition operation.""")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    addition = num_one + num_two
    print("The sum is", addition,".")

def do_subtraction():
    print("""
You have chosen the subtraction operation.""")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    subtraction = num_one - num_two
    print("The difference is", subtraction,".")

def do_multiplication():
    print("""
You have chosen the multiplication operation.""")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    product = num_one * num_two
    print("The product is",product,".")

def do_division():
    print("""
You have chosen the division operation.""")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    quotient = num_one / num_two
    print("The result of the division of the two numbers is",quotient,".")

def do_calculation():

    n = input("Please enter an option (1-4) or 'q' to quit: ")
    if n == "1":
        do_addition()
    if n == "2":
        do_subtraction()
    if n == "3":
        do_multiplication()
    if n == "4":
        do_division()
    if n == "q":
        print("\nGoodbye.")
        return n
    elif n != "1" and n != "2" and n != "3" and n != "4" and n != "q":
        print("""
That was not a valid choice. Try again.\n""")


def run_calculator():
    print("Welcome to the CS 1114 Calculator!")
    print_menu()
    key = do_calculation()
    while not key == "q":
        print_menu()
        key = do_calculation()

def main():

    """Runs a program for performing basic arithmetic
    operations between two numbers
    """

    # call run_calculator() here and remove pass below
    run_calculator()
    #pass

    
####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
