def make_pizza(size,*toppings):
    print(f"Making{size} - inches pizza with trailing ")
    for topping in toppings:
      print(f"{topping.title()}")
make_pizza(10,'extra cheese')
make_pizza(12,'extra cheese','capiscum','jalapeno')

