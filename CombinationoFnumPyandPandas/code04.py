import numpy as np
#------------------------Bitwise Operator------------------------------------
a = 10
b = 15
result1 = np.bitwise_and(a,b)
result2 = np.bitwise_or(a,b)
result3 = np.bitwise_not(a)
result4 = np.left_shift(a, 3)
result5 = np.right_shift(b, 2)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

