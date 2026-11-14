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

        #calling methods
        mydog.sit()
        mydog.roll_over()

        ##creating multiple instances
        yourdog=Dog('lucy',3)
        print(f"your dog name if is {yourdog.name}")
        print(f"lucy age is {yourdog.age}")
        yourdog.roll_over()
        


