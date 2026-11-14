class Car:
  def __init__(self,make,model,year):
    self.make=make
    self.model=model
    self.year=year 
    self.odometer_reading=0   #deafult value
  def get_discriptive_name(self):
    long_name=f"{self.year} {self.make} {self.year}"
    return long_name.title()

# mynewcar=Car('a4',"audi",2024)
# print(mynewcar.get_discriptive_name())

#@@@@@ setting deafult value for attribute
  def read_odometer(self):
    print(f"this car has {self.odometer_reading} miles on it")

#  mynewcar=Car('a4',"audi",2024)
#  print(mynewcar.get_discriptive_name())
# mynewcar.read_odometer()

# @@@@@ modifing attribute values
#@@@@@@  type1-modifing attribut directly

# mynewcar.odometer_reading=23
# mynewcar.read_odometer()


#@@@@@@  modifing sn attribues vslue through a method
  def update_odometer(self,mileage):
    #self.odometer_reading=mileage
    if mileage>=self.odometer_reading:
      self.odometer_reading=mileage
    else:
      print("ypu cant roll back to an odometer")

#mynewcar=Car('a4',"audi",2024)
#print(mynewcar.get_discriptive_name())

#mynewcar.update_odometer(23)
#mynewcar.read_odometer()

#@@@@@ incermenting an attribute value through a method
def increment_odometer(self,miles):
  self.odometer_reading+=miles
myusedcar=Car('tata','outback',2019)
print(myusedcar.get_discreptive_name()) 
myusedcar.update_odometer(2300)
myusedcar.read_odometer()

myusedcar.increment_odometer(100)
myusedcar.read_odometer()






