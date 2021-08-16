class computer:
    def __init__(self,make,ram,storage):
        self.make=make
        self.ram=ram
        self.storage=storage



class mobile(computer):
    def __init__(self,make,ram,storage,model):
        super().__int__(make,ram,storage)
        self.model=model



apple=mobile('Apple',4,128,'iphone')
print(f"Make":{apple.})