def make_pizza(size,*toppings):
    print(f"Making {size} inches size")
    for topping in toppings:
        print(f"topping {topping.title()}")


def make_chocolate_milk_shake(size,*ingredients):
    print(f"Here is your {size} chocalate shake with following ingredients")
    for ingredient in ingredients:
        print(f"{ingredient.title()}")

def day_info():
    print("Today is Wednesday")




def month_info():
    print("It is june")

