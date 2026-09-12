import pandas as pd
#---------------for cheking ---------------------
print("Success")

#--------------- print in series ----------------
data = pd.Series([1,2,3,4,5])
print(data)

#-------------- print of student details ---------
student = pd.Series({
    "Name" : ["Rakesh", "Kumar", "Patel"],
    "Age"  : [22, 23, 24],
    "State" : ["Uttarpradesh", "Maharashtra", "Vadodra"],
    "Course" :["CSE", "AIML", "Civil"],
    "Marks" :[88, 89, 97]
})
print(student)
df = pd.DataFrame(student)
print(df)
print(df.info())
print(df.describe())
df.to_csv("tech4b.csv")
print(student.shape)
print(student.size)
ab = pd.read_csv("TECH-4B.csv")
print(ab)
dataF = pd.DataFrame(ab)
print(dataF.head())
print(dataF.tail())


#-----------For print all marks-------------------------------
for i in student["Marks"]:
    print(i)

for i in range(len(student["State"])):
    if student["State"][i] == "Maharashtra":
        print(student["Name"][i])    


for i in range(len(student["Marks"])):
    if student["Marks"][i] > 95:
        print(student["Name"][i])