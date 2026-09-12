import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# To Upload CSV file
df = pd.read_csv("EducationDataset_2023-24.csv")
print(df.head())

# Q1.Which district has the highest and lowest number of schools?
highest = df.loc[df["No of Schools - Total"].idxmax()]
lowest = df.loc[df["No of Schools - Total"].idxmin()]

print("\nQ1")
print("Highest Schools:", highest["District"],
      highest["No of Schools - Total"])

print("Lowest Schools:", lowest["District"],
      lowest["No of Schools - Total"])

#Q2. Which district has the highest total student enrollment?
highest_student = df.loc[
    df["No of Students - Total"].idxmax()
]
print("\nQ2")
print("Highest Enrollment:",
      highest_student["District"],
      highest_student["No of Students - Total"])

#Q3. Compare boys and girls across districts. Which district has 
# the largest gender difference?
df["Gender Difference"] = abs(
    df["No of Students - Boys"] -
    df["No of Students - Girls"]
)
gender = df.loc[
    df["Gender Difference"].idxmax()
]
print("\nQ3")
print("Largest Gender Difference:",
      gender["District"])
print("Boys:", gender["No of Students - Boys"])
print("Girls:", gender["No of Students - Girls"])
print("Difference:", gender["Gender Difference"])

#Q4. Which district has the highest Class X pass percentage

x = " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"
highest_x = df.loc[df[x].idxmax()]

print("\nQ4")
print("Highest Class X Pass %:",
      highest_x["District"],
      highest_x[x])

#Q5. Which district has the highest Class XII pass percentage?

xii = "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"
highest_xii = df.loc[df[xii].idxmax()]

print("\nQ5")
print("Highest Class XII Pass %:",
      highest_xii["District"],
      highest_xii[xii])

# Q6. Compare Class X and Class XII pass percentages across districts.
print("\nQ6")
print("Average Class X:",
      np.mean(df[x]))
print("Average Class XII:",
      np.mean(df[xii]))
plt.figure(figsize=(12, 6))

plt.plot(
    df["District"],
    df[x],
    marker="o",
    label="Class X"
)
plt.plot(
    df["District"],
    df[xii],
    marker="o",
    label="Class XII"
)
plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII")
plt.xticks(rotation=90)
plt.legend()
plt.grid()
plt.show()

#Q7. Does the number of schools appear to be related to Class X pass percentage?
corr1 = np.corrcoef(
    df["No of Schools - Total"],
    df[x]
)[0, 1]

print("\nQ7")
print("Correlation:", corr1)
plt.scatter(
    df["No of Schools - Total"],
    df[x]
)
plt.xlabel("Number of Schools")
plt.ylabel("Class X Pass %")
plt.title("Schools vs Class X Pass %")
plt.grid()
plt.show()

#Q8. Does total student enrollment appear to be related to Class X pass percentage?
corr2 = np.corrcoef(
    df["No of Students - Total"],
    df[x]
)[0, 1]

print("\nQ8")
print("Correlation:", corr2)
plt.scatter(
    df["No of Students - Total"],
    df[x]
)
plt.xlabel("Total Students")
plt.ylabel("Class X Pass %")
plt.title("Students vs Class X Pass %")
plt.grid()
plt.show()

#Q9. Calculate students per school. Which district has the highest 
# value, and does it appear related to academic performance?
df["Students Per School"] = (
    df["No of Students - Total"] /
    df["No of Schools - Total"]
)
highest_ratio = df.loc[
    df["Students Per School"].idxmax()
]
print("\nQ9")
print("Highest Students per School:",
      highest_ratio["District"])
print("Students per School:",
      round(
          highest_ratio["Students Per School"],
          2
      ))
corr3 = np.corrcoef(
    df["Students Per School"],
    df[x]
)[0, 1]
print("Correlation with Class X:",
      corr3)
plt.scatter(
    df["Students Per School"],
    df[x]
)
plt.xlabel("Students per School")
plt.ylabel("Class X Pass %")
plt.title("Students per School vs Class X")
plt.grid()
plt.show()

# Q10. Based on at least three visualizations, identify three important 
# observations about the education system represented by this dataset.
plt.figure(figsize=(12, 6))
plt.bar(
    df["District"],
    df["No of Schools - Total"]
)
plt.xlabel("District")
plt.ylabel("Number of Schools")
plt.title("Schools by District")
plt.xticks(rotation=90)
plt.grid(axis="y")
plt.show()


# 2. Boys vs Girls
x_axis = np.arange(len(df))
plt.figure(figsize=(12, 6))
plt.bar(
    x_axis - 0.2,
    df["No of Students - Boys"],
    0.4,
    label="Boys"
)
plt.bar(
    x_axis + 0.2,
    df["No of Students - Girls"],
    0.4,
    label="Girls"
)
plt.xticks(
    x_axis,
    df["District"],
    rotation=90
)
plt.xlabel("District")
plt.ylabel("Students")
plt.title("Boys vs Girls")
plt.legend()
plt.grid(axis="y")
plt.show()

# 3. Class X vs Class XII
plt.figure(figsize=(12, 6))
plt.plot(
    df["District"],
    df[x],
    marker="o",
    label="Class X"
)
plt.plot(
    df["District"],
    df[xii],
    marker="o",
    label="Class XII"
)
plt.xticks(rotation=90)
plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII")
plt.legend()
plt.grid()
plt.show()