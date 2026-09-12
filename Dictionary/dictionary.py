
# 1. CREATE AND PRINT DICTIONARY
student = {
    "name": "Rakesh",
    "age": 20,
    "course": "B.Tech"
}
print(student)

for i in student:
    print(i);

# 2. ACCESS VALUES
student = {"name": "Rakesh", "age": 20}
print(student["name"])
print(student["age"])


# 3. get()
student = {"name": "Rakesh", "age": 20}
print(student.get("name"))
print(student.get("city", "Not Found"))


# 4. ADD NEW KEY-VALUE
student = {"name": "Rakesh"}
student["age"] = 20
student["course"] = "B.Tech"
print(student)


# 5. UPDATE VALUE
student = {"name": "Rakesh", "age": 20}
student["age"] = 21
print(student)


# 6. update()
student = {"name": "Rakesh", "age": 20}
student.update({"age": 21, "city": "Lucknow"})
print(student)


# 7. del
student = {"name": "Rakesh", "age": 20}
del student["age"]
print(student)


# 8. pop()
student = {"name": "Rakesh", "age": 20}
x = student.pop("age")
print(x)
print(student)


# 9. popitem()
student = {
    "name": "Rakesh",
    "age": 20,
    "city": "Lucknow"
}
student.popitem()
print(student)


# 10. clear()
student = {"name": "Rakesh", "age": 20}
student.clear()
print(student)


# 11. keys()
student = {"name": "Rakesh", "age": 20}
print(student.keys())


# 12. values()
student = {"name": "Rakesh", "age": 20}
print(student.values())


# 13. items()
student = {"name": "Rakesh", "age": 20}
print(student.items())


# 14. TRAVERSE DICTIONARY
student = {
    "name": "Rakesh",
    "age": 20,
    "city": "Lucknow"
}

for key in student:
    print(key, student[key])


# 15. TRAVERSE USING items()
student = {
    "name": "Rakesh",
    "age": 20,
    "city": "Lucknow"
}

for key, value in student.items():
    print(key, ":", value)


# 16. CHECK KEY EXISTS
student = {"name": "Rakesh", "age": 20}

if "name" in student:
    print("Key exists")
else:
    print("Key does not exist")


# 17. LENGTH OF DICTIONARY
student = {"name": "Rakesh", "age": 20}
print(len(student))


# 18. COPY DICTIONARY
student = {"name": "Rakesh", "age": 20}
new_student = student.copy()
print(new_student)


# 19. dict() FUNCTION
student = dict(
    name="Rakesh",
    age=20,
    city="Lucknow"
)
print(student)


# 20. DICTIONARY FROM TWO LISTS
keys = ["name", "age", "city"]
values = ["Rakesh", 20, "Lucknow"]

student = dict(zip(keys, values))
print(student)


# 21. COUNT FREQUENCY OF ELEMENTS
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)


# 22. COUNT CHARACTERS IN STRING
s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# 23. FIND MAXIMUM VALUE
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Rakesh": 88
}

maximum = max(marks.values())
print(maximum)


# 24. STUDENT WITH HIGHEST MARKS
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Rakesh": 88
}

student = max(marks, key=marks.get)

print(student)
print(marks[student])


# 25. SORT DICTIONARY BY KEYS
d = {
    "c": 3,
    "a": 1,
    "b": 2
}

result = dict(sorted(d.items()))
print(result)


# 26. SORT DICTIONARY BY VALUES
d = {
    "A": 50,
    "B": 20,
    "C": 80
}

result = dict(sorted(d.items(), key=lambda x: x[1]))
print(result)


# 27. REVERSE DICTIONARY
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

reverse = {}

for key, value in d.items():
    reverse[value] = key

print(reverse)


# 28. MERGE TWO DICTIONARIES
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)


# 29. DICTIONARY COMPREHENSION
square = {
    x: x * x
    for x in range(1, 6)
}

print(square)


# 30. EVEN NUMBER DICTIONARY
d = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(d)


# 31. NESTED DICTIONARY
students = {
    "student1": {
        "name": "Rakesh",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students["student1"]["name"])


# 32. FIND DUPLICATE ELEMENTS
arr = [1, 2, 3, 2, 4, 3, 5]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

for key, value in freq.items():
    if value > 1:
        print(key)


# 33. FIRST NON-REPEATING CHARACTER
s = "aabbcde"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break


# 34. TWO SUM USING DICTIONARY
arr = [2, 7, 11, 15]
target = 9

d = {}

for i in range(len(arr)):
    complement = target - arr[i]

    if complement in d:
        print(d[complement], i)
        break

    d[arr[i]] = i


# 35. GROUP WORDS BY LENGTH
words = ["cat", "dog", "apple", "bat", "mango"]

d = {}

for word in words:
    length = len(word)

    if length not in d:
        d[length] = []

    d[length].append(word)

print(d)


# 36. setdefault()
d = {}

d.setdefault("name", "Rakesh")
d.setdefault("age", 20)

print(d)


# 37. fromkeys()
keys = ["name", "age", "city"]

d = dict.fromkeys(keys, "Unknown")

print(d)


# 38. CHECK VALUE EXISTS
student = {
    "name": "Rakesh",
    "age": 20
}

if 20 in student.values():
    print("Value exists")
else:
    print("Value does not exist")


# 39. SUM OF ALL VALUES
marks = {
    "Math": 90,
    "Science": 85,
    "English": 80
}

total = sum(marks.values())

print(total)


# 40. AVERAGE OF VALUES
marks = {
    "Math": 90,
    "Science": 85,
    "English": 80
}

average = sum(marks.values()) / len(marks)

print(average)


# 41. MINIMUM VALUE
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Rakesh": 88
}

print(min(marks.values()))


# 42. STUDENT WITH LOWEST MARKS
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Rakesh": 88
}

student = min(marks, key=marks.get)

print(student)
print(marks[student])


# 43. REMOVE ALL DUPLICATE VALUES
d = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

result = {}

for key, value in d.items():
    if value not in result.values():
        result[key] = value

print(result)


# 44. FIND KEY HAVING GIVEN VALUE
d = {
    "a": 10,
    "b": 20,
    "c": 30
}

search = 20

for key, value in d.items():
    if value == search:
        print(key)


# 45. SWAP KEYS AND VALUES
d = {
    "a": 1,
    "b": 2,
    "c": 3
}

result = {
    value: key
    for key, value in d.items()
}

print(result)


# 46. MERGE USING | OPERATOR
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = d1 | d2

print(d3)


# 47. DICTIONARY FROM USER INPUT
n = int(input("Enter number of elements: "))

d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print(d)


# 48. COUNT WORD FREQUENCY
sentence = "python is easy and python is powerful"

words = sentence.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


# 49. FIND MOST FREQUENT ELEMENT
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

answer = max(freq, key=freq.get)

print(answer)


# 50. CHARACTER WITH MAXIMUM FREQUENCY
s = "programming"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

answer = max(freq, key=freq.get)

print(answer)