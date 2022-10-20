# --- PART 1 ---
"""person = {"name": "Andre", "age": 31}

person["name"] = "Margarida"
person["job"] = "Worker"
person["caract"] = ("Alta", "Baixa")
print(person)

for i in person:
    # print(i)
    # print(person[i])
    print(f"Key: {i} - value: {person[i]}")"""


# --- PART 2 ---

persons_list = [
    ("Andre", 31, 1.9),
    ("Margarida", 47, 1.6),
    ("Andre2", 15, 1.34),
    ("Margarida2", 35, 1.65)
]


def get_info(name, lista):
    for i in lista:
        if i[0] == name:
            return i
    return None


infos = get_info("Andre2", persons_list)
print(infos)


persons_dict = {
    "Andre": (31, 1.9),
    "Margarida": (47, 1.6),
    "Andre2": (15, 1.34),
    "Margarida2": (35, 1.65)
}

infos = persons_dict.get("Andre3")
if not infos:
    print("Key not found")
else:
    print(infos)
