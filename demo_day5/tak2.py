
prompt="please enter your toppings"
toppings_not_available_in_store=['basil_leaves','cheery']
toppings=[]
active=True
while active:
    message=input(prompt)
    if message.lower()=='quit':
        active=False
        break
    else:
        toppings.append(message)
