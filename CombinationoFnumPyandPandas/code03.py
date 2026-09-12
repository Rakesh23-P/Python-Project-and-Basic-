import numpy as np
array1 = np.array([[[100,200],[300,400],[500,600]]])



# for i in matrix:
#     for j in i:
#         for k in i:
#             print(k)

#----------print for 3d arrays-------------
for i in np.nditer(array1):
    print(i, end=" ")  


