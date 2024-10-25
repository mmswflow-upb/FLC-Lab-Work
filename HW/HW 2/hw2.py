import random
import os
import ex1Module
from datetime import datetime, timedelta


# Exercise 2: Create a list populated with 5 random numbers (Hint: use randint()).
def ex2():
    print("Ex 2")
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print(random_numbers)

# Exercise 3: Write a function that prints a list of 5 random integers between 40 and 70.
def ex3():
    print("Ex 3")
    random_numbers = [random.randint(40, 70) for _ in range(5)]
    print(random_numbers)

# Exercise 4: Use the datetime module to create a datetime object and print the full name of the weekday of that day.
def ex4():
    print("Ex 4")
    today = datetime.now()
    print(today.strftime("%A"))

# Exercise 5: Create a directory. Create a .txt file in it. Add some text to it. Read the first 2 lines. Overwrite the text inside the file.
def ex5():
    print("Ex 5")
    dir_name = "test_directory"
    file_name = "test_file.txt"
    
    # Create directory
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    # Create and write to the file
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, "w") as f:
        f.write("This is line 1.\nThis is line 2.\nThis is line 3.")
    
    # Read the first 2 lines
    with open(file_path, "r") as f:
        lines = f.readlines()
        print("First 2 lines:", lines[:2])
    
    # Overwrite the file
    with open(file_path, "w") as f:
        f.write("This is the overwritten content.")

# Exercise 6: Print the name of the operating system. List the files and directories in the current directory.
def ex6():
    print("Ex 6")
    print("Operating System:", os.name)
    print("Files and directories in the current directory:", os.listdir("."))

# Exercise 7: Write a program that displays the date that was 10 days before the current date.
def ex7():
    print("Ex 7")
    today = datetime.now()
    ten_days_ago = today - timedelta(days=10)
    print("Date 10 days ago:", ten_days_ago.strftime("%Y-%m-%d"))

# Call all the functions
ex1Module.ex1("Alice")
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
