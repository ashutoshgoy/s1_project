# separate modules is equivalent to separates python files

from b import  B

class A(B):
    def monday(self):
        print("Today is Monday")



a=A()
a.monday()
a.tuesday()
a.wednesday()
