# 1. Create Tuple
t = (10, 20, 30, 40)
print(t)


# 2. Single Element Tuple
t = (10,)
print(t)


# 3. Tuple without brackets
t = 10, 20, 30
print(t)


# 4. Empty Tuple
t = ()
print(t)


# 5. Tuple using tuple()
t = tuple([10, 20, 30])
print(t)


# 6. Access element
t = (10, 20, 30, 40)
print(t[0])


# 7. Access last element
t = (10, 20, 30, 40)
print(t[-1])


# 8. Negative Indexing
t = (10, 20, 30, 40)
print(t[-2])


# 9. Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])


# 10. First 3 elements
t = (10, 20, 30, 40, 50)
print(t[:3])


# 11. Last 3 elements
t = (10, 20, 30, 40, 50)
print(t[-3:])


# 12. Reverse Tuple
t = (10, 20, 30, 40, 50)
print(t[::-1])


# 13. Traverse Tuple
t = (10, 20, 30, 40)

for x in t:
    print(x)


# 14. Traverse using Index
t = (10, 20, 30, 40)

for i in range(len(t)):
    print(t[i])


# 15. Length of Tuple
t = (10, 20, 30, 40)
print(len(t))


# 16. Check element
t = (10, 20, 30, 40)

print(20 in t)


# 17. Check element not present
t = (10, 20, 30, 40)

print(50 not in t)


# 18. Count element
t = (10, 20, 20, 30, 20)

print(t.count(20))


# 19. Find index
t = (10, 20, 30, 40)

print(t.index(30))


# 20. Concatenate two tuples
a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)


# 21. Repeat Tuple
t = (1, 2, 3)

print(t * 3)


# 22. Tuple to List
t = (10, 20, 30)

lst = list(t)
print(lst)


# 23. List to Tuple
lst = [10, 20, 30]

t = tuple(lst)
print(t)


# 24. String to Tuple
s = "Python"

t = tuple(s)
print(t)


# 25. Find Maximum
t = (10, 50, 20, 40, 30)

print(max(t))


# 26. Find Minimum
t = (10, 50, 20, 40, 30)

print(min(t))


# 27. Sum of Tuple
t = (10, 20, 30, 40)

print(sum(t))


# 28. Sort Tuple
t = (50, 20, 40, 10, 30)

print(sorted(t))


# 29. Sort Tuple and convert back to Tuple
t = (50, 20, 40, 10, 30)

t = tuple(sorted(t))
print(t)


# 30. Find Even Numbers
t = (1, 2, 3, 4, 5, 6)

for x in t:
    if x % 2 == 0:
        print(x)


# 31. Find Odd Numbers
t = (1, 2, 3, 4, 5, 6)

for x in t:
    if x % 2 != 0:
        print(x)


# 32. Count Even Numbers
t = (1, 2, 3, 4, 5, 6)

count = 0

for x in t:
    if x % 2 == 0:
        count += 1

print(count)


# 33. Count Odd Numbers
t = (1, 2, 3, 4, 5, 6)

count = 0

for x in t:
    if x % 2 != 0:
        count += 1

print(count)


# 34. Find Largest Element without max()
t = (10, 50, 20, 40, 30)

largest = t[0]

for x in t:
    if x > largest:
        largest = x

print(largest)


# 35. Find Smallest Element without min()
t = (10, 50, 20, 40, 30)

smallest = t[0]

for x in t:
    if x < smallest:
        smallest = x

print(smallest)


# 36. Remove Duplicate Values
t = (10, 20, 10, 30, 20, 40)

t = tuple(set(t))
print(t)


# 37. Copy Tuple
t1 = (10, 20, 30)

t2 = t1

print(t2)


# 38. Nested Tuple
t = ((1, 2), (3, 4), (5, 6))

print(t)


# 39. Access Nested Tuple
t = ((1, 2), (3, 4), (5, 6))

print(t[1][0])


# 40. Tuple Unpacking
t = (10, 20, 30)

a, b, c = t

print(a)
print(b)
print(c)


# 41. Swap using Tuple
a = 10
b = 20

a, b = b, a

print(a, b)


# 42. Multiple Tuple Unpacking
t = (10, 20, 30, 40, 50)

a, *b, c = t

print(a)
print(b)
print(c)


# 43. Check Tuple is Empty
t = ()

if not t:
    print("Tuple is empty")
else:
    print("Tuple is not empty")


# 44. Compare Two Tuples
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)


# 45. Find Common Elements
a = (1, 2, 3, 4)
b = (3, 4, 5, 6)

common = tuple(set(a) & set(b))

print(common)


# 46. Tuple Comprehension alternative
t = tuple(x * x for x in range(1, 6))

print(t)


# 47. Even Numbers Tuple
t = tuple(x for x in range(1, 11) if x % 2 == 0)

print(t)


# 48. Odd Numbers Tuple
t = tuple(x for x in range(1, 11) if x % 2 != 0)

print(t)


# 49. Tuple inside List
lst = [(1, 2), (3, 4), (5, 6)]

print(lst)


# 50. List of Tuples
students = (
    ("Rakesh", 85),
    ("Amit", 90),
    ("Rahul", 78)
)

for name, marks in students:
    print(name, marks)