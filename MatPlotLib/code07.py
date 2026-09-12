import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Students = ["Student1", "Student2"]
Subject = ["Physics", "Chemistry", "Maths"]
Marks = np.array([
    [75, 80, 70],
    [80, 95, 70]
])

#Printing of marks

for i in range(len(Students)):
    print(Students[i], "Marks")
    for j in range(len(Subject)):
        print(Subject[j], Marks[i][j])
    print()    


#For total marks 
total = np.sum(Marks, axis=1)
for i in range(len(Students)):
    print(Students[i], "Total Marks :", total[i])


#For graph    
plt.subplot(2, 2, 1)
plt.plot(Students, total, marker="o")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks Comparison")
plt.grid()


plt.subplot(2, 2, 2)
plt.bar(Students, total)
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks Comparison")
plt.grid()


plt.subplot(2, 2, 3)
plt.plot(Subject, Marks[0], marker="o", label="Student1")
plt.plot(Subject, Marks[1], marker="o", label="Student2")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks Comparison")
plt.legend()
plt.grid()



plt.subplot(2, 2, 4)
plt.bar(Subject, Marks[0], label="Student1")
plt.bar(Subject, Marks[1], label="Student2")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks Comparison")
plt.legend()
plt.grid()
plt.subplots_adjust(wspace=0.5, hspace=0.5)


plt.show()