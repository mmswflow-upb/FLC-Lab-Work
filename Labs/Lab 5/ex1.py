
def dfa_ex1(word):

    transitions = {
        "A": {"1": "B"},
        "B": {"1": "B"}
    }
    state = "A"
    
    for char in word:
        if char in transitions[state]:
            state = transitions[state][char]
        else:
            return False  
    return state == "B"  


def dfa_ex2(word):
  

    transitions = {
        "A": {"0": "B"},
        "B": {"0": "C"},
        "C": {"0": "D", "1": "E"},
        "D": {"0": "F"},
        "E": {"1": "G"},
        "F":{"0":"D", "1":"E"},
        "G":{"1":"G"}
    }
    state = "A"
    
    for char in word:
        if char in transitions[state]:
            state = transitions[state][char]
        else:
            return False  
    return state == "E" or state == "G" 




def dfa_ex3(word):
    if not word:
        return "The string does not belong to the language."  

   
    start_char = word[0]  
    end_char = word[-1]  

    
    transitions = {
        "A": {}, 
        "B": {}   
    }

    # Initialize the DFA
    state = "A"

    for char in word[1:-1]:  
        pass  

    # Process the last character
    if end_char == start_char:
        transitions["A"][end_char] = "B"  
    
  
    if end_char in transitions[state]:
        state = transitions[state][end_char]  


    return "The string belongs to the language." if state == "B" else "The string does not belong to the language."



# Test cases
print("Exercise 1:")
print(f'dfa_ex1("1") -> {dfa_ex1("1")}')     
print(f'dfa_ex1("111") -> {dfa_ex1("111")}')     
print(f'dfa_ex1("101") -> {dfa_ex1("101")}')

print("\nExercise 2:")
print(f'dfa_ex2("001") -> {dfa_ex2("001")}')         
print(f'dfa_ex2("0001") -> {dfa_ex2("0001")}')       
print(f'dfa_ex2("000") -> {dfa_ex2("000")}')         
print(f'dfa_ex2("0101") -> {dfa_ex2("0101")}')      
print(f'dfa_ex2("000011") -> {dfa_ex2("000011")}')   
print(f'dfa_ex2("0000111") -> {dfa_ex2("0000111")}') 
print(f'dfa_ex2("00001110") -> {dfa_ex2("00001110")}') 

print("\nExercise 3:")
print(f'dfa_ex3("abba") -> {dfa_ex3("abba")}')       
print(f'dfa_ex3("bxyzb") -> {dfa_ex3("bxyzb")}')    
print(f'dfa_ex3("abcdef") -> {dfa_ex3("abcdef")}')   