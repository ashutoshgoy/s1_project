class Calculator:
    def add(self,a,b):
       print("add two number",a+b)
    def subtract(self,a,b):
        print("subtract two number",a-b)
    def multiply(self,a,b):
        print("multiply two number",a*b)
    def divide(self,a,b):
        print("divide two number",a/b)

calculator=Calculator()
calculator.add(2,3)
calculator.subtract(5,4)
calculator.multiply(3,4)
calculator.divide(10,5)

class Car:
     def __init__(self,color,engine):
         self.color_of_car=color
         self.engine_type=engine

     def print_car_info(self):
         print(f"Color Of Car={self.color_of_car}")
         print(f"Type of Engine={self.engine_type}")
mercedes=Car('silver','petrol')
audi=Car('black','diesel')
print("Today is Thrusday")