def myFun(arg1, **kwargs):
    print(f"greeting message is {arg1} ")
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')