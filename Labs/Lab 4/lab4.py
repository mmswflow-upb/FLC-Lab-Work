import re

# Exercise 1: Print only the strings that start with either c or s and end with e
def exercise_1():
    a = "rectangle"
    b = "square"
    c = "sphere"
    d = "triangle"
    e = "cone"
    f = "cube"
    g = "cylinder"

    shapes = [a, b, c, d, e, f, g, "cue"]
    pattern = re.compile(r'^[cs].*e$')

    filtered_shapes = [shape for shape in shapes if pattern.match(shape)]
   
    print("Exercise 1:", filtered_shapes)


# Exercise 2: Write a regex that prints only the words that have exactly 4 letters
def exercise_2():
    words = "car, cat, dog, pool, bath, cone, cube, ring, int"
    words_list = words.split(", ")

    four_letter_words = [word for word in words_list if re.fullmatch(r'\b\w{4}\b', word)]
    print("Exercise 2:", four_letter_words)


# Exercise 3: Loop through the list and match only the words ending in "re" using regex
def exercise_3():
    shapes_list = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", 
                   "rectangle", "parallelogram", "trapezoid"]

    pattern = re.compile(r'.*re$')
    words_ending_re = [word for word in shapes_list if pattern.match(word)]
    print("Exercise 3:", words_ending_re)


# Exercise 4: Extract digits and non-digits from geo string
def exercise_4():
    geo = ("A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. "
           "While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides.")

    digits = re.findall(r'\d+', geo)
    non_digits = re.findall(r'\D+', geo)

    print("Exercise 4 - Digits:", digits)
    print("Exercise 4 - Non-digits:", non_digits)


# Exercise 5: Extract the year, month, and date from the link
def exercise_5():
    link = ("https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-"
            "the-war-for-gloria-read-until-you-understand-and-the-end-of-bias")

    date_part = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', link)
    if date_part:
        year, month, day = date_part.groups()
        print(f"Exercise 5: Year: {year}, Month: {month}, Day: {day}")


# Exercise 6: Change the date format to DD-MM-YYYY
def exercise_6():
    date = "2021-11-02"
    formatted_date = "-".join(reversed(date.split("-")))
    print("Exercise 6:", formatted_date)


# Exercise 7: Write a function to check if a string starts with a digit
def starts_with_digit(s):
    return bool(re.match(r'^\d', s))

def exercise_7():
    print("Exercise 7 - Example 1:", starts_with_digit("1test"))  # True
    print("Exercise 7 - Example 2:", starts_with_digit("test1"))  # False


# Exercise 8: Write a function to check if a string ends with a digit
def ends_with_digit(s):
    return bool(re.search(r'\d$', s))

def exercise_8():
    print("Exercise 8 - Example 1:", ends_with_digit("test1"))  # True
    print("Exercise 8 - Example 2:", ends_with_digit("1test"))  # False


# Exercise 9: Write a function to check if a string contains a digit
def contains_digit(s):
    return bool(re.search(r'\d', s))

def exercise_9():
    print("Exercise 9 - Example 1:", contains_digit("test1"))  # True
    print("Exercise 9 - Example 2:", contains_digit("test"))   # False


# Run all exercises
if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
