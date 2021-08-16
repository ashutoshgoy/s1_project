list_numbers=[1,5,32,45,88,20]

Square_numbers=list(map(lambda x:x**2,list_numbers))
Square_numbers.sort()
for square in Square_numbers:
    print(square)ch

