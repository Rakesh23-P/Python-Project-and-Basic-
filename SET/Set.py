# 1. Create a Set
s = {10, 20, 30, 40}
print(s)


# 2. Empty Set
s = set()
print(s)


# 3. Add an element
s = {10, 20, 30}
s.add(40)
print(s)


# 4. Add multiple elements
s = {10, 20}
s.update([30, 40, 50])
print(s)


# 5. Remove an element
s = {10, 20, 30, 40}
s.remove(30)
print(s)


# 6. Discard an element
s = {10, 20, 30}
s.discard(20)
print(s)


# 7. Pop an element
s = {10, 20, 30}
x = s.pop()
print(x)
print(s)


# 8. Clear Set
s = {10, 20, 30}
s.clear()
print(s)


# 9. Length of Set
s = {10, 20, 30, 40}
print(len(s))


# 10. Check element
s = {10, 20, 30}
print(20 in s)


# 11. Check element not present
s = {10, 20, 30}
print(50 not in s)


# 12. Traverse Set
s = {10, 20, 30, 40}

for x in s:
    print(x)


# 13. Remove duplicates from List
lst = [10, 20, 10, 30, 20, 40, 30]
s = set(lst)
print(s)


# 14. Set to List
s = {10, 20, 30}
lst = list(s)
print(lst)


# 15. List to Set
lst = [10, 20, 10, 30]
s = set(lst)
print(s)


# 16. Tuple to Set
t = (10, 20, 10, 30)
s = set(t)
print(s)


# 17. Set to Tuple
s = {10, 20, 30}
t = tuple(s)
print(t)


# 18. Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))


# 19. Union using |
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


# 20. Intersection
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))


# 21. Intersection using &
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)


# 22. Difference
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a.difference(b))


# 23. Difference using -
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a - b)


# 24. Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))


# 25. Symmetric Difference using ^
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)


# 26. Subset
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


# 27. Subset using <=
a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)


# 28. Superset
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))


# 29. Superset using >=
a = {1, 2, 3, 4}
b = {1, 2}

print(a >= b)


# 30. Disjoint Sets
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))


# 31. Copy Set
a = {10, 20, 30}
b = a.copy()

print(b)


# 32. Find maximum
s = {10, 50, 20, 40, 30}
print(max(s))


# 33. Find minimum
s = {10, 50, 20, 40, 30}
print(min(s))


# 34. Sum of Set
s = {10, 20, 30, 40}
print(sum(s))


# 35. Sort Set
s = {50, 20, 40, 10, 30}
print(sorted(s))


# 36. Count even numbers
s = {1, 2, 3, 4, 5, 6}

count = 0
for x in s:
    if x % 2 == 0:
        count += 1

print(count)


# 37. Count odd numbers
s = {1, 2, 3, 4, 5, 6}

count = 0
for x in s:
    if x % 2 != 0:
        count += 1

print(count)


# 38. Find even numbers
s = {1, 2, 3, 4, 5, 6}

for x in s:
    if x % 2 == 0:
        print(x)


# 39. Find odd numbers
s = {1, 2, 3, 4, 5, 6}

for x in s:
    if x % 2 != 0:
        print(x)


# 40. Set Comprehension
s = {x for x in range(1, 11)}
print(s)


# 41. Square using Set Comprehension
s = {x*x for x in range(1, 6)}
print(s)


# 42. Even numbers using Set Comprehension
s = {x for x in range(1, 11) if x % 2 == 0}
print(s)


# 43. Remove duplicate characters from String
text = "programming"

s = set(text)
print(s)


# 44. Find common elements in two Lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a) & set(b)
print(common)


# 45. Find unique elements from two Lists
a = [1, 2, 3]
b = [3, 4, 5]

unique = set(a) | set(b)
print(unique)


# 46. Elements present in A but not B
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a - b)


# 47. Elements present in B but not A
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(b - a)


# 48. Check two Sets are Equal
a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)


# 49. Update Set using Union
a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)
print(a)


# 50. Intersection Update
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.intersection_update(b)
print(a)


# 51. Difference Update
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)
print(a)


# 52. Symmetric Difference Update
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)
print(a)