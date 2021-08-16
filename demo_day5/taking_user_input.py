users=int(input("how many people are in their dinner group"))

if users>8:
    print(f"you will have to wait for a table ")
else:
    print(f"table is ready ,please come and join")

number=int(input("enter a number"))
if number%10==0:
    print(f"{number} is  a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

name=input("enter your name")
current_year=int(input("enter current_year"))

print(f"you entered your name as -{name.title()}")

if current_year%2==0:
  print(f"year {current_year} is an even year")
else:
  print(f"year {current_year} is an odd year")
