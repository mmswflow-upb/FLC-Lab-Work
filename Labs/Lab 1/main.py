def Ex1():
    list1 = ["Math", "English", "History", "Chemistry", "Biology"]
    print(f"Second item in the list: {list1[1]}")
    print(f"Length of list: {len(list1)}")
    print(f"Second, third and forth items in the list: {list1[1:4]}")
    print(f"Fourth element from the end of the list: {list1[len(list1)-1]}")

    list2 = list1.copy()
    list2.remove("Chemistry")
    print(f"List without Chemistry: {list2}")

    list3 = list1.copy()
    list3.insert(2, "Geography")
    print(f"List with Geography: {list3}")

    list4 = list1.copy()
    list4[1] = "Romanian"
    print(f"List with Romanian: {list4}")


'''

1. Print the value for “Lname”
2. Copy the dictionary into a new variable and change the age from 23 to 21 in the new dictionary
3. Add the key/value pair “occupation” : “student” to the dictionary
4. Copy the dictionary into a new variable and remove Fname from the new dictionary
5. Print a list that contains all the key/value pairs of the dictionary
6. Print a list that contains all the values in the dictionary
7. Use setdefault() to search for “hobby” : “chess” and print the updated dictionary
8. Empty the dictionary
'''

def Ex2():
    dict1 = {"Fname" : "Jane", "Lname" : "Doe", "age" : 23}

    print(f"Value for Lname: {dict1['Lname']}")

    dict2 = dict1.copy()
    dict2["age"] = 21

    print(f"Dictionary with age 21: {dict2}")

    dict1["occupation"] = "student"
    
    print(f"Dictionary with occupation: {dict1}")

    dict3 = dict1.copy()
    dict3.pop("Fname")

    print(f"Dictionary without Fname: {dict3}")

    print(f"List with key/value pairs: {dict1.items()}")
    print(f"List with values: {dict1.values()}")

    dict1.setdefault("hobby", "chess")
    print(f"Dictionary with hobby: {dict1}")

    dict1.clear()
    print(f"Empty dictionary: {dict1}")

Ex1()
print("\n\n")
Ex2()