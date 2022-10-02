list1 = [1, 2, 3, 4, 5]
eg = map(lambda x: x*2, list1)
print(list(eg))

list2 = [2, 4, 6, 8, 10]
eg2 = map(lambda x, y: x+y, list1, list2)
print(list(eg2))

eg3 = [2, 3, 4]
z = map(str, eg3)
print(list(z))

list3 = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = filter(lambda x: x < 5, list3)
print(list(filtered))