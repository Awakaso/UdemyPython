def ask_for_name():
    name_temp = ""
    while name_temp == "":
        name_temp = input("What is your name? ")
    return name_temp


def ask_for_age(person_name):
    age_temp = 0
    while age_temp == 0:
        age_str = input(person_name + ", what is your age? ")
        try:
            age_temp = int(age_str)
        except:
            print("ERROR: Age must be a number")
    return age_temp


def ask_for_height(person_name):
    height_temp = 0
    while height_temp == 0:
        height_str = input(person_name + ", what is your height? ")
        try:
            height_temp = float(height_str)
        except:
            print("ERROR: Age must be a number")
    return height_temp


def display_results(name, age, height):
    print()
    print("Your name is " + name + ", you are " + str(age) + " years old")
    # print(f"Your name is {name}, you are {age} years old")
    # print("Your name is %s, you are %s years old" % (name, age))
    print("Soon you will be " + str(age+1))

    if age >= 18:
        if age > 60:
            print("You are a senior")
        else:
            print("You are a adult")
    elif age == 17:
        print("You are almost adult")
    else:
        if age < 10:
            if age == 1 or age == 2:
                print("You are a baby")
            else:
                print("You are a kid")
        else:
            print("You are a minor")

    print("Your height is: " + str(height) + "m")


# name1 = ask_for_name()
# age1 = ask_for_age(name1)

# name2 = ask_for_name()
# age2 = ask_for_age(name2)

# display_results(name1, age1)
# display_results(name2, age2)


for i in range(0, 3):
    name = "foo" + str(i+1)
    age = ask_for_age(name)
    height = ask_for_height(name)
    display_results(name, age, height)



'''
password = ""
while not password == "1234" :
    password = input("What is the password? ")
'''
