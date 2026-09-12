class Parent:
    def display(self):
        print("This is Parent class")

class Child(Parent):
    def display2(self):
        print("This is Child class")

obj = Child()
obj.display()
obj.display2()



class Animal:
    def eat(self):
        print("Animal eat the food")

class Deer(Animal):
    def eat1(self):
        print("Deer also eat the food")

obj = Deer()
obj.eat() 
obj.eat1()               