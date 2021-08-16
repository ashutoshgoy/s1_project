class Car:
    def __init__(self,color,engine,tyre_color):
        self.color_of_car=color
        self.engine_type=engine
        self.color_of_tyre=tyre_color
    #we are generalizing the object

    def print_car_info(self):
        print(f"Color of Car={self.color_of_car}")
        print(f"Type of Engine={self.engine_type}")
        print(f"Color of tyres={self.color_of_tyre}")

        @staticmethod
        def number_of_steering_wheels():
            print("This Car has 1 steering wheel")




list_of_object=[]
list_of_object.append(Car("red","petrol","black"))
list_of_object.append(Car("green","diesel","white"))

for list in list_of_object:
    list.print_car_info()

