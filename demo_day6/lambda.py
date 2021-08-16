#list as a parameter
#function as a paramater

from collections import Counter

numbers=[20,23,1,4,99,21,32,44,67,98,80]
greater_number=list(filter(lambda x:x>10,numbers))

for greater_no in greater_number:
    print(greater_no)



