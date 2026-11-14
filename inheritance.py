#when one class inherits from another class , it takes on attributes and methods of the first class
#the child class can inherit any or all the attributes and methods pf its parent class and it is also free to create new attribues and  methods of its own
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.model} {self.make} {self.year}"
        return long_name.title()
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer=mileage
        else:
            print("you can not roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    def __init__(self,make,model,year)
        super().__init__(make,model,year)
        self.battery_size=40
# my_leaf=ElectricCar('nissan','leaf',2023)
# print(my_leaf.get_descriptive_name())

# @@@@ defining attributes and methods for child class
def describe_battery(self):
    print(f"this car has a {self.battery_size} -kwh battery")
# my_leaf=ElectricCar('nissan','leaf',2023)
# print(my_leaf.get_descriptive_name())
# my_leaf.discribe_battery()

# @@@@@ overriding method from parent class
    def fill_gas_tank(self):
        print("this car does not have gas tank")
my_leaf=ElectricCar('nissan','leaf',2023)
print(my_leaf.get_descriptive_name())
my_leaf.discribe_battery()
#
