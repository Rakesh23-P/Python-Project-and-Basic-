import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE DATASET
data = {
    "Semester": [
        "Sem 1", "Sem 1", "Sem 1", "Sem 1", "Sem 1",
        "Sem 1", "Sem 1", "Sem 1", "Sem 1",

        "Sem 2", "Sem 2", "Sem 2", "Sem 2", "Sem 2",
        "Sem 2", "Sem 2", "Sem 2", "Sem 2", "Sem 2",

        "Sem 3", "Sem 3", "Sem 3", "Sem 3", "Sem 3",
        "Sem 3", "Sem 3", "Sem 3", "Sem 3", "Sem 3",

        "Sem 4", "Sem 4", "Sem 4", "Sem 4", "Sem 4",
        "Sem 4", "Sem 4", "Sem 4", "Sem 4", "Sem 4",

        "Sem 5", "Sem 5", "Sem 5", "Sem 5", "Sem 5",
        "Sem 5", "Sem 5", "Sem 5", "Sem 5", "Sem 5",

        "Sem 6", "Sem 6", "Sem 6", "Sem 6", "Sem 6",
        "Sem 6", "Sem 6", "Sem 6", "Sem 6"
    ],

    "Subject": [
        "Engineering Physics",
        "Engineering Mathematics-1",
        "Fundamnetals of Electronics Engineering",
        "Fundamnetals of Mechanical Engineering",
        "Soft Skills",
        "Engineering Physics Lab",
        "Basics Electronics Engineering Lab",
        "English Language Lab",
        "Workshop Practice Lab",

        "Engineering Chemistry",
        "Engineering Mathematics-2",
        "Fundamnetals of Electrical Engineering",
        "Programming for Problem Solving",
        "Environment and Ecology",
        "Engineering Chemistry Lab",
        "Basic Electrical Engineering",
        "Programming for Problem Solving Lab",
        "Engineering graphics and design lab",
        "Sports and Yoga",

        "Material Science",
        "Technical Communication",
        "Data Structure",
        "Computer Organization and architecture",
        "Discrete structure and Theory of Logic",
        "Cyber Security",
        "Data Structure lab",
        "Computer Organization and architecture lab",
        "Web Desigining lab",
        "Project",

        "Mathematics-IV",
        "Universal Human Values and Professional Ethics",
        "Operating System",
        "Theory of Automata and Formal Languages",
        "Object Oriented Programming with Java",
        "Python programming",
        "Operating System Lab",
        "Object Oriented Programming with Java Lab",
        "Cyber Security Workshop",
        "Sports and Yoga - II",

        "Database Management System",
        "Web Technology",
        "Design and Analysis of Algorithm",
        "Object Oriented System Design with C++",
        "Application of Soft Computing",
        "Database Management System Lab",
        "Web Technology Lab",
        "Design and Analysis of Algorithm Lab",
        "Mini Project or Internship Assessment",
        "Constitution of India",

        "Software Engineering",
        "Compiler Design",
        "Computer Networks",
        "Blockchain Architecture Design",
        "IDEA TO BUSINESS MODEL",
        "Software Engineering Lab",
        "Compiler Design Lab",
        "Computer Networks Lab",
        "Essence of Indian Traditional Knowledge"
    ],

    "Marks": [
        89, 97, 88, 73, 69, 97, 97, 97, 98,

        85, 89, 91, 81, 80, 98, 97, 98, 98, 95,

        69, 80, 78, 80, 83, 86, 99, 99, 99, 74,

        79, 66, 64, 73, 80, 93, 98, 98, 98, 99,

        82, 65, 79, 92, 82, 100, 100, 100, 100, 86,

        81, 87, 66, 87, 76, 100, 100, 100, 81
    ]
}

df = pd.DataFrame(data)

# CLEAN DATA

# Remove extra spaces
df["Semester"] = df["Semester"].str.strip()
df["Subject"] = df["Subject"].str.strip()

# Display Dataset
print("\n================ DATASET ================\n")
print(df)

# 2. HOW MANY SEMESTERS?
print("\n2. Number of Semesters:")
number_of_semesters = df["Semester"].nunique()
print(number_of_semesters)

# 3. HOW MANY SUBJECTS STUDIED IN TOTAL?
print("\n3. Total Subjects:")
total_subjects = len(df)
print(total_subjects)

# 4. HIGHEST MARKS
print("\n4. Highest Marks:")
highest_marks = df["Marks"].max()
print(highest_marks)


# 5. LOWEST MARKS
print("\n5. Lowest Marks:")
lowest_marks = df["Marks"].min()
print(lowest_marks)

# 6. SEMESTER WITH HIGHEST TOTAL MARKS
semester_total = df.groupby("Semester")["Marks"].sum()
print("\n6. Semester with Highest Total Marks:")
print(semester_total.idxmax(), "=", semester_total.max())

# 7. SEMESTER WITH LOWEST TOTAL MARKS
print("\n7. Semester with Lowest Total Marks:")
print(semester_total.idxmin(), "=", semester_total.min())

# 8. DISPLAY FIRST FIVE RECORDS
print("\n8. First Five Records:")
print(df.head())

# 9. AVERAGE MARKS FOR EACH SEMESTER
semester_average = df.groupby("Semester")["Marks"].mean()

# Correct order
semester_order = [
    "Sem 1",
    "Sem 2",
    "Sem 3",
    "Sem 4",
    "Sem 5",
    "Sem 6"
]

semester_average = semester_average.reindex(semester_order)
print("\n9. Average Marks for Each Semester:")
print(semester_average)

# 10. LINE GRAPH - SEMESTER-WISE AVERAGE
plt.figure(figsize=(8, 5))
plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

plt.title("Semester-wise Average Marks")
plt.xlabel("Semester")
plt.ylabel("Average Marks")

plt.grid(True)
plt.tight_layout()
plt.show()

# 11. BAR GRAPH - SUBJECT-WISE AVERAGE
subject_average = df.groupby("Subject")["Marks"].mean()
plt.figure(figsize=(14, 7))
plt.bar(
    subject_average.index,
    subject_average.values
)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 12. HIGHEST-PERFORMING SUBJECT
highest_subject = subject_average.idxmax()
highest_subject_marks = subject_average.max()

print("\n12. Highest Performing Subject:")
print(highest_subject, "=", highest_subject_marks)

# 13. LOWEST-PERFORMING SUBJECT
lowest_subject = subject_average.idxmin()
lowest_subject_marks = subject_average.min()

print("\n13. Lowest Performing Subject:")
print(lowest_subject, "=", lowest_subject_marks)

# 14. BEST AND WORST SEMESTER
best_semester = semester_average.idxmax()
worst_semester = semester_average.idxmin()

print("\n14. Best Semester:")
print(best_semester, "=", round(semester_average.max(), 2))
print("\nWorst Semester:")
print(worst_semester, "=", round(semester_average.min(), 2))

# 15. IMPROVEMENT BETWEEN SEMESTER 1 AND SEMESTER 6
sem1_avg = semester_average["Sem 1"]
sem6_avg = semester_average["Sem 6"]
improvement = sem6_avg - sem1_avg

print("\n15. Improvement between Semester 1 and Semester 6:")
print(round(improvement, 2), "marks")

# 16. NUMPY STATISTICS
marks = np.array(df["Marks"])

print("\n16. NumPy Statistics:")
print("Mean:", round(np.mean(marks), 2))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard Deviation:", round(np.std(marks), 2))


# 17. PERFORMANCE OF EACH SUBJECT
plt.figure(figsize=(14, 7))

for semester in semester_order:
    semester_data = df[df["Semester"] == semester]
    plt.plot(
        semester_data["Subject"].values,
        semester_data["Marks"].values,
        marker="o",
        label=semester
    )
plt.title("Subject Performance Across Semesters")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 18. TARGET = 75%
plt.figure(figsize=(8, 5))
plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o",
    label="My Average"
)

# Target line
plt.axhline(
    y=75,
    linestyle="--",
    label="Target = 75%"
)
plt.title("Semester Performance with Academic Target")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 19. MY PERFORMANCE VS CLASS AVERAGE

class_average = [72, 74, 73, 75, 76, 78]
my_average = semester_average.values
plt.figure(figsize=(8, 5))
plt.plot(
    semester_order,
    my_average,
    marker="o",
    label="My Average"
)
plt.plot(
    semester_order,
    class_average,
    marker="o",
    label="Class Average"
)
plt.title("My Performance vs Class Average")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 20. 2 x 2 MATPLOTLIB DASHBOARD
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Figure 1 - Semester-wise Average
ax[0, 0].plot(
    semester_order,
    semester_average.values,
    marker="o"
)
ax[0, 0].set_title("Semester-wise Average")
ax[0, 0].set_xlabel("Semester")
ax[0, 0].set_ylabel("Average Marks")
ax[0, 0].grid(True)

# Figure 2 - Subject-wise Average
ax[0, 1].bar(
    subject_average.index,
    subject_average.values
)
ax[0, 1].set_title("Subject-wise Average")
ax[0, 1].set_xlabel("Subject")
ax[0, 1].set_ylabel("Average Marks")
ax[0, 1].tick_params(axis="x", rotation=90)

# Figure 3 - Semester-wise Total
semester_total = semester_total.reindex(semester_order)
ax[1, 0].bar(
    semester_order,
    semester_total.values
)
ax[1, 0].set_title("Semester-wise Total Marks")
ax[1, 0].set_xlabel("Semester")
ax[1, 0].set_ylabel("Total Marks")

# Figure 4 - My Performance vs Class Average
ax[1, 1].plot(
    semester_order,
    my_average,
    marker="o",
    label="My Average"
)
ax[1, 1].plot(
    semester_order,
    class_average,
    marker="o",
    label="Class Average"
)
ax[1, 1].set_title("My Performance vs Class Average")
ax[1, 1].set_xlabel("Semester")
ax[1, 1].set_ylabel("Average Marks")
ax[1, 1].legend()
ax[1, 1].grid(True)


plt.tight_layout()
plt.show()

# 21. FIVE OBSERVATIONS
print("\n21. FIVE OBSERVATIONS:")
print(
    "1. Semester 2 has the highest average marks among the six semesters."
)
print(
    "2. Semester 3 has the lowest average marks among the six semesters."
)
print(
    "3. The highest individual marks obtained are 100."
)
print(
    "4. The lowest individual marks obtained are 64 in Operating System."
)
print(
    "5. The average performance in all six semesters is above the 75% target."
)