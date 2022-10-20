import random

operatorsList = ["+", "-", "*", "/"]
guess_result = 0.0
correct_percent = 0
count = 0


def ask_for_number(num1, num2, oper):
    guess_number = 0.0

    try:
        guess_number = input("Compute: " + str(num1) + " " + oper + " " + str(num2) + " = ")
    except:
        print("ERROR: Enter a valid number.")

    return float(guess_number)


print("Each correct question gives you 1 point.")
print("You need to get 3 points to pass.")


for i in range(0, 4):

    number1 = random.randrange(1, 10)
    number2 = random.randrange(1, 10)
    operator = random.choice(operatorsList)

    print("Question nº" + str(i+1) + " out of 4:")
    guess_result = ask_for_number(number1, number2, operator)

    if operator == "+":
        correct_result = number1 + number2
    elif operator == "-":
        correct_result = number1 - number2
    elif operator == "*":
        correct_result = number1 * number2
    elif operator == "/":
        correct_result = number1 / number2

    if correct_result == guess_result:
        print("Right answer")
        correct_percent += 25
        count += 1
    else:
        print("Wrong answer")

    print()


print("Your points: " + str(count) + " out of 4")
print("You correctly anwser to " + str(correct_percent) + "%")


if correct_percent < 25:
    print("You are zero!")
elif correct_percent == 25:
    print("You are on avarage. Unfortunatly, you didn't passed.")
elif correct_percent == 50:
    print("You are on avarage. Unfortunatly, you didn't passed.")
elif correct_percent == 75:
    print("You passed. You are slightly better than the avarage. Take a balon.")
elif correct_percent == 100:
    print("Perfect! You passed. You should get a battery operated toaster.")
