#informing people

lists=['donald duck ','mickey_mouse','Ben 10']
print("Hey evwryone,we found a bigger table")

lists.insert(2,'goffy')
lists.append('scooby doo')



print(f"{lists[0].title()} you are invited to dinner tonight ,Please be there by 8PM")
print(f"{lists[1].title()} you are invited to dinner tonight,Please be there by 8PM")
print(f"{lists[2].title()} you are invited to dinner tonight,Please be there by 8 PM")

print(f"{lists[3].title()} you are invited to dinner tonight,Please be there by 8 PM")
print(f"{lists[4].title()} you are invited to dinner tonight,Please be there by 8 PM")
#until two people left
removed_list1=lists.pop()

print(f" {removed_list1.title()} you are sorry you cannot  invite them to dinner")

removed_list2=lists.pop()
print(f"{removed_list2.title() } you are sorry you cannot invite them to dinner")
removed_list3=lists.pop()
print(f"{removed_list3} you are sorry you cannot invite them to dinner")
print(f"{lists[0].title()} you are invited")
print(f"{lists[1].title()} you are invited")
