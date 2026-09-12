import numpy as np

#-------------1D Array ------------------------------------------
a = np.array([1,2,3,4,5])
for i in a:
    print(i)
print( "Sum of 1D Array: ",np.sum(a))    


#-------------2D Array ------------------------------------------
b = np.array([[1,2,3,4],[2,3,4,5]])
for i in b:
    print(b)
print("Sum of 2D Array: ",np.sum(b))    


#------------3D Array --------------------------------------------
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(c)
print(a.ndim)
for i in c:
    for j in i:
        print(j)
        
print("Sum of 3D Array: ",np.sum(c))


#------------- even odd --------------------------------------------
for i in c:
    for j in i:
        if j % 2 == 0:
            print(j)  

#size of elemnt             
print(a.shape)
print(a.size)


#-------------- max --------------------------------------------------

d = np.array([1,2,3,4,5])
print("Maximum of number in array: ", np.max(d))    

#-------------- min ---------------------------------------------------
e = np.array([1,2,3,4,5])
print("Minimum of number in array: ", np.min(e)) 

#-------------- Average -----------------------------------------------

f = np.array([1,2,3,4,5])
print("Average of number in array: ", np.mean(f)) 


#------------------Traverse the array ----------------------------------

a = np.array([1,2,3,4,5])
for i in a:
    print("Traverse of the array: ",i)


#------------------full ---------------------------------------------------
print(np.full(1,2))

#------------------ones ---------------------------------------------------
print(np.ones(4))

#------------------Zeroes -------------------------------------------------
print(np.zeros(5))
    