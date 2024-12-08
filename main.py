def check_guess(guess, answer):
    global score
    if guess.lower() == answer:
        print("Correct answer")
        score += 1
    else:
        print("Wrong answer")

score = 0
print("Guess the animal")
guess1 = input("Which bear lives at the North Pole? \n")
check_guess(guess1, "polar bear")
guess2 = input("Name the programming language which is named after an animal.\n")
check_guess(guess2, "python")
guess3 = input("What is the largest animal?\n")
check_guess(guess3, "blue whale")

print(f"Your score is {score}.")
