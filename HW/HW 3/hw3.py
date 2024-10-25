import re

# Exercise 1: Check if a string contains only lowercase letters, digits, and *
def contains_lowercase_digits_star(s):
    return bool(re.fullmatch(r'[a-z0-9*]+', s))

def exercise_1():
    print("Exercise 1 - Right Example:", contains_lowercase_digits_star("abc123*"))  # True
    print("Exercise 1 - Wrong Example:", contains_lowercase_digits_star("Abc123*"))  # False

# Exercise 2: Check if a string contains uppercase letters followed by _ and lowercase letters
def contains_upper_lower_pattern(s):
    return bool(re.fullmatch(r'[A-Z]+_[a-z]+', s))

def exercise_2():
    print("Exercise 2 - Right Example:", contains_upper_lower_pattern("FILS_student"))  # True
    print("Exercise 2 - Wrong Example:", contains_upper_lower_pattern("fils_STUDENT"))  # False

# Exercise 3: Print all the words ending in "le" or "re"
def exercise_3():
    hw4 = "rectangle square sphere triangle cone cube cylinder"
    words_ending_in_le_or_re = [word for word in hw4.split() if word.endswith('le') or word.endswith('re')]
    print("Exercise 3:", words_ending_in_le_or_re)

# Exercise 4: Create a regex with at least two groups and print all matches
def exercise_4():
    s = "This is a number 1234, and here's another 5678."
    pattern = re.compile(r'(\d{2})(\d{2})')
    matches = pattern.findall(s)
    print("Exercise 4 - Matches:", matches)

# Exercise 5: Change date format from YY-MM-DD to DD-MM-YY and month number to month name
def change_date_format(date):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    day, month, year = date.split('-')
    month_name = months[int(month)-1]
    return f"{day}-{month_name}-{year}"

def exercise_5():
    print("Exercise 5:", change_date_format("21-12-01"))

# Exercise 6: Match text starting with 'm', ending with 'n', with exactly 3 characters between
def match_m_n_three_between(s):
    return bool(re.fullmatch(r'm...n', s))

def exercise_6():
    print("Exercise 6 - Right Example:", match_m_n_three_between("melon"))  # True
    print("Exercise 6 - Wrong Example:", match_m_n_three_between("man"))  # False

# Exercise 7: Match text starting with 'h' followed by exactly 2 or 3 'i'
def match_h_with_2_or_3_i(s):
    return bool(re.fullmatch(r'hi{2,3}', s))

def exercise_7():
    print("Exercise 7 - Right Example:", match_h_with_2_or_3_i("hii"))  # True
    print("Exercise 7 - Wrong Example:", match_h_with_2_or_3_i("hiiii"))  # False

# Exercise 8: Match words containing 'q', but not at the start or end of the word
def match_q_not_start_or_end(s):
    return bool(re.search(r'\Bq\B', s))

def exercise_8():
    print("Exercise 8 - Right Example:", match_q_not_start_or_end("equal"))  # True
    print("Exercise 8 - Wrong Example:", match_q_not_start_or_end("qatar"))  # False

# Exercise 9: Replace all 'a' with 'u' and all 'i' with 'e'
def replace_a_with_u_and_i_with_e(s):
    return s.replace('a', 'u').replace('i', 'e')

def exercise_9():
    print("Exercise 9:", replace_a_with_u_and_i_with_e("animals are interesting"))

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
