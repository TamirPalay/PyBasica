# Exercise 1

# Declare a variable called first and assign it to "Hello World"
first = "Hello World"

# This is a comment.

# Log a message to the terminal
print("I AM A COMPUTER!")

# If statement checking conditions
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# Assign a variable called nope to an absence of value
nope = None

# Combine true and false using "and"
result_and = True and False
print("True and False =", result_and)

# Calculate the length of the string
length = len("What's my length?")
print("Length:", length)

# Convert string to uppercase
uppercase = "i am shouting".upper()
print("Uppercase:", uppercase)

# Convert string "1000" to number 1000
number = int("1000")
print("Number:", number)

# Combine number 4 with string "real"
combined = str(4) + "real"
print("Combined:", combined)

# Record output of 3 * "cool"
cool_result = 3 * "cool"
print("3 * 'cool' =", cool_result)

# Record output of 1 / 0 (this causes an error, so we catch it)
try:
    error_result = 1 / 0
except ZeroDivisionError:
    error_result = "Error: Division by zero"
print("1 / 0 =", error_result)

# Determine the type of []
type_of_list = type([])
print("Type of []:", type_of_list)

# Ask the user for their name
name = input("Enter your name: ")
print("Hello,", name)

# Ask the user for a number
user_number = float(input("Enter a number: "))

if user_number < 0:
    print("That number is less than 0!")
elif user_number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# Find index of "l" in "apple"
index_l = "apple".index("l")
print("Index of 'l' in apple:", index_l)

# Check whether "y" is in "xylophone"
check_y = "y" in "xylophone"
print("Is 'y' in xylophone?", check_y)

# Check whether a string called my_string is all lowercase
my_string = "hello world"
is_lowercase = my_string.islower()
print("Is my_string lowercase?", is_lowercase)


# =========================================
# Exercise 2 : Cat’s and Dog’s Years
# =========================================

def calculate_pet_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]


# Test the program with given values
print("\nPet years calculations:")

human_years = 10
print(calculate_pet_years(human_years))

human_years = 1
print(calculate_pet_years(human_years))

human_years = 2
print(calculate_pet_years(human_years))
