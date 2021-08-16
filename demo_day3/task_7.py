usernames=['admin','tim','ashutosh','rajat','ankit']



if usernames:

   for username in usernames:



     if username =='admin':
       print(f"Hello {username},would you like to see a status report")
     else:
       print(f"Hello {username},thank you for logging in again")
else:
    print("We need to find some users")


# bikes in show_room1
# bikes in show_room2
bikes_in_showroom1=['yamaha','tvs','bajaj']
bikes_in_showroom2=['ducati','duke','yamaha','bmw']
# common bytes in both the lists
#time complexity o(n) in python
#time_complexity o(n*2) in c++

for bike in bikes_in_showroom1:
    if bike in bikes_in_showroom2:
        print(f"Bike {bike.title()} is present in both  the showrooms")
