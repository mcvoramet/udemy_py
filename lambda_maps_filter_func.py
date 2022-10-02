def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]


for item in map(square,my_nums):
    print(item)

print(list(map(square, my_nums)))
#above function give the same result as below one
print(list(map(lambda num: num ** 2, my_nums)))

my_nums = [1, 2, 3, 4, 5]


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


def check_even(num):
    return num%2 == 0


mynums = [1, 2, 3, 4, 5, 6]
for n in filter(check_even, mynums):
    print(n)

print(list(filter(check_even, mynums)))
#above fuction give the same result as nelow one
print(list(filter(lambda num: num % 2 == 0, mynums)))


square = lambda num : num ** 2
print(square(5))
#above function give the same result as below one
print(list(map(lambda num:num ** 2, mynums)))


print(names)    #list of ['Andy', 'Eve', 'Sally']
print(list(map(lambda x:x[0], names)))   #get first letter in the list
print(list(map(lambda x:x[::-1], names))) #get reverse name in the list







