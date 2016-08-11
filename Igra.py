import random

print "Welcome to my hidden numbers game! Ques the number between 0 in 20!"

answer = "Y"

while answer == "Y":

    user_input = raw_input("Please input number of your choice -->>")

    user_input = int(user_input)
    random_number = random.randint(0, 20)

    while user_input != random_number:

        if random_number < user_input:
            print "Your number is to high! Try again!"

        else:
            print "your number is to low! Try again!"

        user_input = int(raw_input())

    print "You quesed the right number! Congratulations!"

    while True:
        print "would you like to play another game?"
        answer = raw_input()
        if answer not in "YN":
            print "Please enter Y or N only."
        else:
            break
print "Thank you for playing"
