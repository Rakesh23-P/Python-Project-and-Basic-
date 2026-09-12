
# #constructor method
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)


# s = Student("Rakesh", 90)

# s.display()



my_list = [1, 2, 3, 4, 5]
my_tuple = ("Apple", "Orange", "Banana")
class Student1:
    def __init__(self, my_list, my_tuple):
        self.my_list = my_list
        self.my_tuple = my_tuple

    def display1(self):
        print("List:")
        for i in self.my_list:
            print(i)

        print("Tuple:") 
        for i in self.my_tuple:
            print(i)
result = Student1(my_list, my_tuple)
result.display1()