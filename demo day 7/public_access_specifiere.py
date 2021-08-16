class Car:
    def __init__(self,color,engine,tyre_color):
        self.__color_of_car=color
        self.__engine_type=engine
        self.color_of_tyre=tyre_color

    def print_car_info(self):
        print(self.color_of_car)
        print(self.engine_typr)
        print(self.color_of_tyre)

class Test:
       mercedes=Car('silver','petrol','black')


mercedes=Car('silver','petrol','black')

