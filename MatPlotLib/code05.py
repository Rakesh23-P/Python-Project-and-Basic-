import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
y = [0,1,0,1,0,1,0]

x1 = [0,1,2,3,4,5,6]
y1 = [1,0,1,0,1,0,1]


plt.subplot(1,2,1)
plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("0,1 graph")
plt.grid()

plt.subplot(1,2,2)
plt.plot(x1,y1)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("0,1 graph")
plt.grid()
plt.show()