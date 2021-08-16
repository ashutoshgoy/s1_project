class Pizza_Makers:
    def __init__(self,size,crust):
      self.size_of_pizza=size
      self.crust_value=crust
    def pizza_info(self):
        print(f"Pizza is {self.size_of_pizza} inches  in size with {self.crust_value} crust")

@staticmethod

small_pizza=Pizza_Makers(8,"thin")
small_pizza.pizza_info()

