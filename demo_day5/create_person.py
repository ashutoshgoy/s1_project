
users=[]
def full_name(first_name,last_name):
    name=f"{first_name} {last_name}"
    users.append(name)
    return users


prompt='Asking user for first name and last name,Type quit when done'
active=True
while active:


   print("Please enter first name and last name")
   print("press q to exit")
   first_name=input("First name=")
   if first_name=='q':
       active=False
       break
   last_name=input("last name =")
   if last_name.lower()=='q':
        active-False
        break


   else:
        people=full_name(first_name,last_name)


for l in people:
    print(f"{l}")