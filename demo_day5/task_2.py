prompt="please enter your toppings,Type 'quit' when done"
active=True
toppings=[]
toppings_not_available=['basil leaves','cherry']
while active:
    message=input(prompt).lower()

    if message=='quit':
        active=False
        break
    else:

                toppings.append(message)



for topping in toppings:
      if topping in toppings_not_available:
       print(f"we are sorry !{topping.title()} is not available today")

      else:
       print(f"{topping.title()} will be added to the pizza")
