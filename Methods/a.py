# def methodname():
#     print("This is method")


# #for parametarised


# def Class(name):
#     print(name)
# Class("Rakesh")    

# #create a method to check number is even or odd

# num = int(input("Enter the number: "))
# def evenOdd(number):
#     if(number%2==0):
#         print("even")
#     else:
#         print("Odd")   
# evenOdd(num)     


# #create a function to check number is prime or not

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


#wap for factorial
# num = int(input("Enter a number: "))
# def facto(num):
#     fact = 1
#     for i in range(2, num + 1):
#         fact = fact * i
#     print(fact)
# facto(num)

# #wap for first n natural number

# def natural_sum(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#     print(sum)
# num = int(input("Enter n: "))
# natural_sum(num)



#functions to perform arithmetic operations
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def mathsOperation(a, b):
#     print("Addition: ", a+b)
#     print("Subtraction: ", a-b)
#     print("Multiply: ", a*b)
#     print("Division: ", a/b)
#     print("Modulo division: ", a%b)
#     print("Floor division: ", a//b)
#     print("Power: ", a**b)
# mathsOperation(a,b)    

