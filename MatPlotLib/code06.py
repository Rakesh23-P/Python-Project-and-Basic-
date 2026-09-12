import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
y = [0,1,0,1,0,1,0]

x1 = [0,1,2,3,4,5,6]
y1 = [1,0,1,0,1,0,1]

p = [1,3,5,7,9]
q = [2,4,6,9,10]

r = [1,2,3,4,5]
s = [1,3,5,7,9]

plt.subplot(2,2,1)
plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph-1")
plt.grid()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.subplot(2,2,2)
plt.plot(x1,y1)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph-2")
plt.grid()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.subplot(2,2,3)
plt.plot(p, q)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph-3")
plt.grid()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.subplot(2,2,4)
plt.plot(r, s)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Graph-4")
plt.grid()
plt.show()