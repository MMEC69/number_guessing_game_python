#we can improve upon this code as we desire
import random
import math

print("=============Welcome to our number guessing, you may proceed by specifying a range.=============")

lower_end = int(input("Enter lower end of the range  : "))
higher_end = int(input("Enter higher end of the range: "))

total_number_of_guesses_allowed = 7

number_range_list = []

for i in range(lower_end, higher_end+1):
    number_range_list.append(i)

selected_random_value = random.choice(number_range_list)

number_of_allowed_tries = math.log(higher_end - lower_end + 1, 2)
number_of_allowed_tries = round(number_of_allowed_tries)
print("You have {} chances".format(number_of_allowed_tries))

print("=============Let's begin the game shall we=============")

count = 0

for i in range(int(number_of_allowed_tries)):
    count+=1
    user_answer = int(input("Give your answer: "))
    if user_answer == selected_random_value and count < 8:
        print("\nYou have chosen the right answer,\nYour answer = {}\nCorrect answer = {}\nTotal number of tries: {}\n".format(user_answer, selected_random_value, count))
        break
    elif count < number_of_allowed_tries:
        if user_answer < selected_random_value:
            print("\nThe value is too small go higher.")
        elif user_answer > selected_random_value:
            print("\nThe value is too high go lower.")
        print("Try agian :(\nAvailable tries: {}".format(number_of_allowed_tries-count))
        continue
    else:
        print("\nYou have used all of your {} tries, \nThe answer is {}, \nplz quit the game and try agian.".format(count,selected_random_value))

print("Thank you for trying our game, Good bye!")