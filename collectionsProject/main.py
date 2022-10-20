# collections : Arrays, Lists, Tuples
# Tuples() : immutable : you cannot change it
# Listas[] : mutable : you can add/delete/modify items


# -----------TUPLES--------------
# "Brian", "Bob", "Alice", "Jean"
'''persons = ("Brian", "Bob", "Alice", "Jean")  # Tuple
print(persons)
print(persons[1])


for i in range(0, len(persons)):
    print(persons[i])'''


# -----------LISTS--------------
# "Brian", "Bob", "Alice", "Jean"
'''persons = ["Brian", "Bob", "Alice", "Jean"]  # List
print(persons)
print(persons[1])
new_person = "Andre"
persons.append(new_person)
persons[0] = "Andre"
print(persons)
del persons[-1]
print(persons)'''


# -----------FUNCTIONS AND TUPLES--------------
'''def get_informations():
    return "Alice", 26, 1.6


def display_info(name, age, height):
    print("Name: " + name)
    print("Age: " + str(age))
    print("Height: " + str(height))


infos = get_informations()
print(infos)

print("Name: " + infos[0])
print("Age: " + str(infos[1]))
print("Height: " + str(infos[2]))


name, age, height = get_informations()
print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height))


display_info(infos[0], infos[1], infos[2])
display_info(*infos)  # unpack tuple info'''


# -----------SLICES--------------
# "Brian", "Bob", "Alice", "Jean"
persons = ("Brian", "Bob", "Alice", "Jean", "Steven", "John")
# print(persons)

# start:stop:step
for i in persons[0:2]:
    print(i)


name = "Alice"
for i in name[0:2]:
    print(i)
