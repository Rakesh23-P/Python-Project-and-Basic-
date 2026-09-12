import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    "Semester": [
        "Sem 1", "Sem 1", "Sem 1", "Sem 1","Sem 1", "Sem 1", "Sem 1", "Sem 1","Sem1",
        "Sem 2", "Sem 2", "Sem 2", "Sem 2","Sem 2", "Sem 2", "Sem 2", "Sem 2","Sem2","Sem2",
        "Sem 3", "Sem 3", "Sem 3", "Sem 3","Sem 3", "Sem 3", "Sem 3", "Sem 3","Sem3","Sem3",
        "Sem 4", "Sem 4", "Sem 4", "Sem 4","Sem 4", "Sem 4", "Sem 4", "Sem 4","Sem 4", "Sem 4",
        "Sem 5", "Sem 5", "Sem 5", "Sem 5","Sem 5", "Sem 5", "Sem 5", "Sem 5","Sem 5", "Sem 5",
        "Sem 6", "Sem 6", "Sem 6", "Sem 6","Sem 6", "Sem 6", "Sem 6", "Sem 6","Sem 6"
    ],

    "Subject": [
        "Engineering Physics", "Engineering Mathematics-1", 
        "Fundamnetals of Electronics Engineering", 
        "Fundamnetals of Mechanical Engineering", 
        "Soft Skills","Engineering Physics Lab",
        "Basics Electronics Engineering Lab", 
        "English Language Lab", "Workshop Practice Lab",



        "Engineering Chemistry", "Engineering Mathematics-2",
        "Fundamnetals of Electrical Engineering", 
        "Programming for Problem Solving", "Environment and Ecology", 
        "Engineering Chemistry Lab", "Basic Electrical Engineering",
        "Programming for Problem Solving Lab",
        "Engineering graphics and design lab",
        "Sports and Yoga",



        "Material Science", "Technical Communication","Data Structure",
        "Computer Organization and architecture", "Discrete structure and Theory of Logic",
        "Cyber Security", "Data Structure lab", "Computer Organization and architecture lab",
        "Web Desigining lab","Project",




        "Mathematics-IV", "	Universal Human Values and Professional Ethics", 
        "Operating System",
        "Theory of Automata and Formal Languages","	Object Oriented Programming with Java",
        "Python programming","Operating System Lab","	Object Oriented Programming with Java Lab",
        "Cyber Security Workshop","	Sports and Yoga - II",



        "Database Management System", "Web Technology", "Design and Analysis of Algorithm",
        "Object Oriented System Design with C++","Application of Soft Computing",
        "Database Management System Lab","	Web Technology Lab","Design and Analysis of Algorithm Lab",
        "Mini Project or Internship Assessment","Constitution of India",


        "Software Engineering", "Compiler Design", "Computer Networks","Blockchain Architecture Design",
        "IDEA TO BUSINESS MODEL","Software Engineering Lab","Compiler Design Lab",
        "Computer Networks Lab","	Essence of Indian Traditional Knowledge"
    ],

    "Marks": [
        89,97, 88,73,69,97,97,97,98,
        85, 89, 91, 81,80,98,97,98,98,95,
        69, 80, 78, 80,83,86,99,99,99,74,
        79, 66, 64, 73,80,93,98,98,98,99,
        82, 65, 79, 92,82,100,100,100,100,86,
        81, 87, 66, 87,76,100,100,100,81
    ]
}


df = pd.DataFrame(data)

print(df)



#----------------------------------


# Semester-wise Total Marks

df["Semester"] = df["Semester"].str.replace("Sem1", "Sem 1")
df["Semester"] = df["Semester"].str.replace("Sem2", "Sem 2")
df["Semester"] = df["Semester"].str.replace("Sem3", "Sem 3")

# Total obtained marks
semester_total = df.groupby("Semester")["Marks"].sum()

# Maximum marks for each semester
max_marks = {
    "Sem 1": 900,
    "Sem 2": 1000,
    "Sem 3": 1000,
    "Sem 4": 1000,
    "Sem 5": 1000,
    "Sem 6": 900
}

max_marks = pd.Series(max_marks)

# Graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    semester_total.index,
    semester_total.values
)

plt.xlabel("Semester")
plt.ylabel("Total Marks")
plt.title("Semester-wise Total Marks")

# Marks on top of bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 5,
        str(int(bar.get_height())),
        ha="center",
        fontweight="bold"
    )

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()
plt.show()