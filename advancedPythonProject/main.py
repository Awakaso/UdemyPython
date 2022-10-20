class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price


pizzas = [
    Pizza("Calzone", 11),
    Pizza("Peperoni", 9.5),
    Pizza("4 Queijos", 12)
]

# pizzas_name = []
# for i in pizzas:
#     pizzas_name.append(i.name)

pizzas_name = [i.name for i in pizzas if len(i.name) > 7]

print(pizzas_name)

# any : return True if one item is true
print([i.price > 10 for i in pizzas])
expensive_pizza = any([i.price > 10 for i in pizzas])
print(expensive_pizza)


# sum :
print(sum([i.price for i in pizzas]))
print([1 for i in pizzas if i.price > 10])
print(sum([1 for i in pizzas if i.price > 10]))



# ZIP lists
pizza_names = ("4 cheeses", "Calzone", "Hawai")
pizza_prices = (11, 9.5, 12)

pizza_names_prices = list(zip(pizza_names, pizza_prices))
print(pizza_names_prices)

for (name, price) in pizza_names_prices:
    print(f"{name} - {price}$")


unzipped = list(zip(*pizza_names_prices))
print(unzipped)

pn, pz = list(zip(*pizza_names_prices))
print(pn)
print(pz)