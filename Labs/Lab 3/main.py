import math
import random
from datetime import datetime

# Function for Exercise 1
def display_current_date_time():
    now = datetime.now()
    print(now.strftime("%B %d, %Y %H:%M:%S"))

# Function for Exercise 2
def calculate_circle_area():
    radius = int(input("Enter the radius of the circle: "))
    area = math.pi * radius**2
    print(f"The area of the circle is: {area} or {radius**2}π")

# Function for Exercise 3
def select_random_number():
    numbers = [1, 2, 3, 4, 5]
    random_number = random.choice(numbers)
    print(f"Random number from the list: {random_number}")

# Function for Exercise 4
def shuffle_list():
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)
    print(f"Shuffled list: {items}")

# Function for Exercise 5
def compute_lcm_gcd():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    lcm = abs(num1 * num2) // math.gcd(num1, num2)
    gcd = math.gcd(num1, num2)
    

    print(f"LCM of {num1} and {num2} is {lcm}")
    print(f"GCD of {num1} and {num2} is {gcd}")

# Function for Exercise 6
def compute_factorial():
    num = int(input("Enter a number: "))
    factorial = math.factorial(num)
    print(f"Factorial of {num} is {factorial}")

# Function for Exercise 7
def display_week_number():
    date = datetime.now()
    week_number = date.isocalendar()[1]
    print(f"Week number of the current date: {week_number}")

# Function for Exercise 8
def compute_distance_between_points():
    x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"The distance between the points is: {distance}")

# Main function to call all exercises
def main():
    print("Ex 1: Display current date and time")
    display_current_date_time()

    print("\nEx 2: Calculate area of a circle")
    calculate_circle_area()

    print("\nEx 3: Select a random number from a list")
    select_random_number()

    print("\nEx 4: Shuffle elements of a list")
    shuffle_list()

    print("\nEx 5: Compute LCM and GCD of two numbers")
    compute_lcm_gcd()

    print("\nEx 6: Compute factorial of a number")
    compute_factorial()

    print("\nEx 7: Display the week number of the current date")
    display_week_number()

    print("\nEx 8: Compute distance between two points")
    compute_distance_between_points()

if __name__ == "__main__":
    main()
