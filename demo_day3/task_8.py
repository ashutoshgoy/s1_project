current_users=['ashu','rohan','rajat','ishu','agoyal']

new_users=['Ashu','roshan','sameer','ishu','ankit']

current_users_lower=[]

for user in current_users:
     username=user.lower()
     current_users_lower.append(username)

for  new_user in new_users:
     if new_user.lower() in  current_users_lower:
         print("the person will need to enter a new username")
     else:
         print(f"the  username {new_user} is available")



d = dict((val, range(int(val), int(val) + 2))
				for val in ['1', '2', '3'])














