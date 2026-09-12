import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
y = [0,1,0,1,0,1,0]

x1 = [0,1,2,3,4,5,6]
y1 = [1,0,1,0,1,0,1]



plt.plot(x, y)
plt.plot(x1,y1, linestyle=":", color="Pink", marker="s")
plt.axhline(y=1.5, linestyle="--", linewidth="3", marker="o")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("0,1 graph")
plt.grid()
plt.scatter(x,y)
plt.show()