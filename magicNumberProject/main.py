import random


magic_number = random.randrange(1, 10)
guess_number = 0
lives = 3

while guess_number != magic_number:
    for i in range(0, 3):
        try:
            guess_number = int(input("What is the magic number (between 1 and 10)? "))
        except:
            print("ERROR: Enter a valid number. You lost 1 life.")
        i += 1
        lives -= 1

        if guess_number == magic_number:
            print("You won!")
            break
        elif lives > 0:
            if lives - 1 == 0:
                print("You lost 1 life. You have " + str(lives) + " remaining.")
                print("This is your last chance.")
            else:
                print("You lost 1 life. You have " + str(lives) + " remaining.")
        elif lives == 0:
            print("You lost!")
            print("The number was " + str(magic_number) + ", you fucking dumb!")
    break