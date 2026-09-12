import numpy as np
array = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print(array)
# print("-----------------------------")
# for i in array:
#     for j in i:
#         print(j, end=" ")

# print("------------for n dimensional array-----------------")
# for i in np.nditer(array):
#     print(i, end=" ") 
# 
# 
# Transpose a matrix

# print(array.T)

# Sum of all element present in matrix
print("Sum :", np.sum(array))
print("Row wise sum :", np.sum(array, axis=1))
print("Column wise sum :", np.sum(array, axis=0))
print("Max :", np.max(array))
print("Min :", np.min(array))
