pizzas = ["4 cheeses", "vegetarian", "hawai", "calzone", "four seasons"]


def custom_sort(e):
    return len(e)


def insert_pizza():
    try:
        new_pizza = input("Add your pizza: ")
    except:
        print("Error: Type a new one")
        return

    if new_pizza.lower() in pizzas:
        print("Pizza already exists.")
    else:
        pizzas.append(new_pizza.lower())


def display(produtos, n_elementos = -1):
    prod = produtos

    if not n_elementos == -1:
        prod = produtos[0:n_elementos]

    if len(prod) == 0:
        print("NO PIZZAS")

    else:
        print("----- PIZZAS (" + str(len(prod)) + ") -----")
        prod.sort(reverse=True, key=custom_sort)
        for i in prod:
            print(i)

        print()
        print("First pizza: " + prod[0])
        print("Last pizza: " + prod[-1])


insert_pizza()
display(pizzas)
