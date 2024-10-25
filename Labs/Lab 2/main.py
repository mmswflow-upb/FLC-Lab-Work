# Exercise 1: Program to print numbers between 40 and 70 divisible by 3
print("\nEx 1:")
for num in range(40, 71):
    if num % 3 == 0:
        print(num)

# Exercise 2: Program to take user's first and last names and print them in reverse order
print("\nEx 2:")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)

# Exercise 3: Program to display sum of all numbers from 1 to user input
print("\nEx 3:")
user_input = int(input("Enter an integer: "))
total_sum = sum(range(1, user_input + 1))
print(f"Sum of numbers from 1 to {user_input} is: {total_sum}")

# Exercise 4: Program to display "Success" while looping through the first 10 numbers starting from 5
print("\nEx 4:")
for i in range(5, 15):
    print("Success")

# Exercise 5: Program to count specific letters in a string
print("\nEx 5:")
string = "Welcome to the lab!"
count_letters = sum(string.count(char) for char in "mlcae")
print(f"Total count of m, l, c, a, e: {count_letters}")

# Exercise 6: Program to find factorial of a number inputted by the user
print("\nEx 6:")
import math
number = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {number} is: {math.factorial(number)}")

# Exercise 7: Program to adjust user input number based on conditions
print("\nEx 7:")
num_input = int(input("Enter a number: "))
if num_input > 100:
    result = num_input / 2 + 20
else:
    result = num_input * 3 - 200
print(f"Result: {result}")

# Exercise 8: Program to transform user input sequence into a list and tuple
print("\nEx 8:")
numbers = input("Enter numbers separated by commas: ")
numbers_list = numbers.split(",")
numbers_tuple = tuple(numbers_list)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)

# Exercise 9: Program to print the square of all numbers from 1 to a given one
print("\nEx 9:")
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(f"Square of {i}: {i ** 2}")
