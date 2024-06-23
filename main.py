import random

range1 = int(input("Enter the lower range: "))
range2 = int(input("Enter the upper range: "))
if range1 > range2:
    print("Invalid range")
    exit(1)

num_answer = random.randint(range1, range2)

while True:
    num_guess = int(input("Enter your guess: "))
    if num_guess == num_answer:
        print("You got it!")
        break
    elif num_guess < num_answer:
        print("Too low")
    else:
        print("Too high")



