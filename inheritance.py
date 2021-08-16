class B:
    def season(self):
        print("It is summer season")
 
class C:
   def pizza(self):
       print("Pizza is delicious")
class A(B,C):
    def week(self):
        print("It is thr first week of july")




a=A()
a.week()
a.pizza()
a.season()