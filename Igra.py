import random

random_number = random.randint(0, 20)

print "Welcome to my hidden numbers game! Ques the number between 0 in 20!"
# user inputs random number
user_input = raw_input("Please input number of your choice -->>")
# user's input change to int
user_input = int(user_input)


while user_input != random_number:

    if random_number < user_input:
        print "Your number is to high! Try again!"

    else:
        print "your number is to low! Try again!"

    user_input = int(raw_input())

print "You quesed the right number! Congratulations!"



