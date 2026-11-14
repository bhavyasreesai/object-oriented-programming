#making an object from class is called instantiation
#class
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is sitting now")
    def roll_over(self):
        print(f"{self.name} if rolling over")
        mydog=Dog('willie',6)
        print(f"my dog name is {mydog.name}")
        print(f"my dog is {mydog.age} years old")
