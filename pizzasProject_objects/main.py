class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian
        # self.ingredients = []
        # self.vegetarian = False

    def Display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGAN"
        print("PIZZA " + self.name + " - " + str(self.price) + "$" + veg_str)
        print(", ".join(self.ingredients))
        print()


class CustomPizza(Pizza):
    base_price = 5
    custom_price = 0.89
    pizza_number = 0

    def __init__(self):
        CustomPizza.pizza_number += 1
        super().__init__("Custom " + str(CustomPizza.pizza_number), 0, [])
        self.ask_ingredients(CustomPizza.pizza_number)
        self.calculate_price()

    def ask_ingredients(self, pizza_number):
        print("Ingredientes para a pizza número " + str(pizza_number))
        while True:
            ingredient = input("Adicione ingredientes para a pizza " + str(pizza_number) + " (ENTER para sair): ")
            if ingredient == "":
                print()
                return

            self.ingredients.append(ingredient.capitalize())
            print("Você tem " + str(len(self.ingredients)), "ingredientes adicionados: " + ", ".join(self.ingredients))

    def calculate_price(self):
        if len(self.ingredients) > 0:
            self.price = len(self.ingredients) * self.custom_price * self.base_price


pizzas = [Pizza("4 Queijos", 8.99, ("Mozzarella", "Cheddar", "Parmesão", "Feta"), True),
          Pizza("Peperoni", 10.99, ("Mozzarella", "Pepperoni")),
          Pizza("Frango BBQ", 12, ("Mozzarella", "Frango Grelhado", "Cebola Roxa", "Pimentos Verdes")),
          Pizza("Vegetariana", 8.99, ("Mozzarella", "Cebola Roxa", "Pimentos Verdes", "Cogumelos Frescos", "Azeitonas",
                                      "Tomate Fresco", "Feta", "Parmesão"), True),
          CustomPizza(),
          CustomPizza()
          ]


def pizza_sort(e):
    return e.price


# pizzas.sort(key=pizza_sort)

for pizza in pizzas:
    # if "Feta" in pizza.ingredients:
    pizza.Display()
