num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(filter(
    lambda x: x % 2 == 0, num
    )
)
print(even_num)