list1 = [1,2,3,4,5,6]
print(list1)

#finding position of the element
print(list1[3])

#for updating the value
list1[5] = 100
print(list1)

#for traversing the list
for number in list1:
    print(number, end=" ")

#for count even and odd element
for number in list1:
    even_count = 0
    if(number%2==0):
        even_count +=1
print(even_count)
print(len(list1) - even_count)       

#average of list
average = sum(list1)/len(list1)
print(average)        

#append
#insert()
#remove()
#pop()
#len()
#extend()
#reverse()
#sort()
#clear()
#copy()
#count()


list3 = [30, 10, 20, 10]

# append()
list3.append(40)
print("append():", list3)

# insert()
list3.insert(1, 15)
print("insert():", list3)

# remove()
list3.remove(10)      
print("remove():", list3)

# pop()
x = list3.pop()       
print("pop() removed:", x)
print("After pop():", list3)

# len()
print("len():", len(list3))

# extend()
list3.extend([50, 60])
print("extend():", list3)

# reverse()
list3.reverse()
print("reverse():", list3)

# sort()
list3.sort()
print("sort():", list3)

# count()
print("count(10):", list3.count(10))

# copy()
new_list = list3.copy()
print("copy():", new_list)

# clear()
list3.clear()
print("clear():", list3)