import random

#Create a random code consisting of four digits using numbers 1-8, with no repeated digits




def generate_code():
    number_list = list(range(1,9))
    random.shuffle(number_list)
    code = ''.join(map(str, number_list[:4]))
    return code

# print(generate_code())

#Code checks if guess is correct and returns that check if input meets the length, repeating, and valid number requirments
#Will have at least two functions
#Shoudl return a boolean value (true or false)
#code check function returns x and o values adn game logic is determined by those two values
def check_guess(code, guess):
    if len(guess) != len(code):
        return False
    
    x_count = sum(1 for c, g in zip(code, guess) if c == g)
    
    code_set = set(code)
    guess_set = set(guess)
    
    common_digits = code_set.intersection(guess_set)
    
    o_count = sum(min(code.count(d), guess.count(d)) for d in common_digits) - x_count
    
    return (x_count, o_count) == (len(code), 0)

#Test Case: 
# code = '1234'
# guess = '1234'
# result = check_guess(code, guess)
# print("Generated Code:", code)
# print("Guess:", guess)
# result = check_guess(code, guess)
# print("Result:", result)