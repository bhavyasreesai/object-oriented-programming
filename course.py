item='phone'
item1_price=100
item1_quantity=5
item_price_total=item1_price*item1_quantity

print(type(item))
print(type(item1_price))
print(type(item1_quantity))
print(type(item_price_total))
#<class 'str'>
#<class 'int'>
#<class 'int'>
#<class 'int'>

class Item:#class
    pass

item1=Item()#object
#creating attributes
item1.name='phone'
item1.price=100
item1.quantity=5
print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))
#<class '__main__.Item'>
#<class 'str'>
#<class 'int'>
#<class 'int'>

random_str='aaa'
print(random_str.upper())
#AAA

#functions are defined outside the class
#methods are defined inside the class
class Item:
    def calculate_total_price(self,x,y):
        return x*y
        pass
item1=Item()
item1.name='phone'
item1.price=100
item1.quantity=5
print(item1.calculate_total_price(item1.price,item1.quantity)) #500
item2=Item()
item2.name='laptop'
item2.price=1000
item2.quantity=3
print(item2.calculate_total_price(item2.price,item2.quantity))#3000



class Item:
    def __init__(self):
        print("I AM CREATED")
    def calculate_total_price(self,x,y):
     return x*y
    pass
item1=Item()
item1.name='phone'
item1.price=100
item1.quantity=5
item2=Item()
item2.name='laptop'
item2.price=1000
item2.quantity=3

