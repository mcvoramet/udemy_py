#Guessing Game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
   if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
   print("Out of Guesses, you lose")
else:
    print("You Win")

#------------------------------------------------------------------

#power function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
       result = result * base_num
   return result

print(raise_to_power(2, 4))

#----------------------------------------------------------------


#dealing with list of list

number_grid = [
   [1, 2, 3],
   [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)


# replace aeiou letter with g

def translate(phrase):
    translation = ""
   for letter in phrase:
        if letter in "AEIOUaeiou":
          translation = translation+"g"
       else:
            translation = translation+letter
    return translation

print(translate(input("Enter phrase: ")))

#--------------------------------------------------------------

# try/except

try:
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as val_err:
    print(val_err)
#------------------------------------------------------------------

#read file

mbox_file = open("mbox-short.txt", "r") #"r"=read, "w"=write "a"=append, "r+"=read+write
for data in mbox_file.readlines(): #readlines=give array of all data in file, readline=give 1st line do multiple time to get more line
    print(data)
mbox_file.close()

#-----------------------------------------------

#write to file

mbox_file = open("index.html", "w")
mbox_file.write("<p>This is HTML<p>")
mbox_file.close()
#------------------------------------------------


#to import other library use this syntax below (line92)
#import name_of_the_libray(file that include your .py file or particular .py file


#create your own data type with class in this syntax(this one work with file app.py)
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

#--------------------------------------------------------------------------------


#class example (connect with app.py file)

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



#Dictionaries
my_dict = {'apple': 2.99, 'oranges': 1.99, 'pizza': {'cheese': 129.29}, 'amount': [1, 2, 3]}
my_dict['apple'] = 3.99
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict['apple'])
print(my_dict['pizza']['cheese'])
print(my_dict['amount'][0])


#Tuples
t = (22, 1, 23, 1, 1, 1, 23, 23, 22, 32, 32, 1)
print(t.count(1))
print(t.index(32))


#set
myset = set()
myset.add(1)
print(myset)
mylist=[1,2,3,3,3,32,1,2,1,33,2,2]
print(set(mylist))
print(set('Anaconda'))


#File
myfile = open('mail_list.txt')
print(myfile.read())
print(myfile.read())
myfile.seek(0) #to re-cursor to starting point so it can re-read file again
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
with open('mail_list.txt') as email_list:
    contents = email_list.read()
print(contents)


#sec1 test
print(((((2**3)/4)+18)*6)-19.75)
s = 'hello'
print(s[1])
list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2][2]='goodbye'
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)
d= {'simple_key': 'hello'}
print(d['simple_key'])
e = {'k1':{'k2':'hello'}}
print(e['k1']['k2'])
f={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(f['k1'][2]['k2'][1]['tough'][2][0])
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

square_root = 4**0.5
print(square_root)

x = 'hello'
print(x[::-1]) #backward slicing

list=[0]*3 # = [0,0,0]
print(list)


#forloop through list,tuple,dict
my_bag = ['pen', 'pencil', 'laptop', 'earphone']
my_num = [1,2,3,4,5,6,7,8,9,10]
for thing in my_bag:
    print(thing)
for num in my_num:
    if num%2 == 0:
        print(num)
    else:
        print('...')

list_sum = 0
for num in my_num:
    list_sum = list_sum + num
print("...")
print(list_sum)
print("____")

my_storage = [(21,32), (121,32), (33,545), (65, 483)]
for (a,b) in my_storage:
    print(a)
    print(b)

d = {'k1':1, 'k2':2, 'k3':3}

for key, value in d.items():
    print(key)
    print(value)
    

#Combo basic
x = 0

while x <5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("finish")
    print('\n')

mystring = "Voramet"

for letter in mystring:
    if letter == 'a':
        continue     #if it is equal to a then go back to the loop line 231
    print(letter)
print('\n')
for letter  in mystring:
    if letter == 'a':
        break          #if it is equal to a then go out of the loop
    print(letter)

print("\n")
for num in range(0,11,2):   # (start, end, step)
    print(num)

index_count = 0

print("\n")
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

print("\n")
print('enumerate')
for item in enumerate(word):
    print(item)

print("\n")
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
print('zip')
for item in zip(mylist1, mylist2):
    print(item)
print(list(zip(mylist1,mylist2)))

print('\ncheck whether the thing is in there')
d = {'mykey': 345}
print(345 in d.keys())

print('\n')
mylist1 = [10,20,12,32,21,32,13]
print('max')
print(max(mylist1))
print("min")
print(min(mylist1))

print('shuffle (random library)')
from random import shuffle
mylist1 = [1,2,3,4,5,6,7,8]
shuffle(mylist1)
print(mylist1)

print('\n')
print('random integer(random library)')
from random import randint
x = randint(0,13)
print(x)

print('\n')
mylist1 = 'hello'
mylist = []
for letter in mylist1:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mylist1] #same thing as above one
print(mylist)

coco = [x for x in range(0, 11)]
print(coco)

cococo = [x for x in range(0, 11) if x%2 == 0]
print(cococo)

print("Temperature in Farenheit")
celcius = [0, 10, 25, 38, 40, 100]
farenheit = [((9/5)*temp + 32) for temp in celcius]
print(farenheit)

farenheit = []

for temp in celcius:
    farenheit.append(((9/5)*temp+32))
print('Temperature in Farenheit')
print(farenheit)

print('nested loop')

mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)


#sec2 test
st = 'Print only the words that start with s in this sentence'
sp = st.split()
for s in sp:
    if s[0] == 's':
        print(s)
print("\n")

num = list(range(0, 11))
for i in num:
    if i%2 == 0:
        print(i)
print('\n')

onetoFifty = list(range(0,51))
for i in onetoFifty:
    if i%3 == 0:
        print(i)
print('\n')

st = 'Print every word in this sentence that has an even number of letters'
evst = st.split()

for i in evst:
    if len(i)%2 == 0:
        print("even!")
    else:
        print(i)
print("\n")

onetoHundred = range(0, 101)
for i in onetoHundred:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
print("\n")

st = 'Create a list of the first letters of every word in this string'
nst = st.split()
keep = []
for i in nst:
    keep.append(i[0])
print(keep)
'''

''' 
#Function
def say_hello(name='Default'):    #add default so when there is no name assign to name it will not error
    print('Hello'+ name)
say_hello(' Jack')

def add_num(num1, num2):
    return num1+num2        #use teturn instead of print() in case you want to assign resulty to the variable
result = add_num(12,20)
print(result)

def even_check(number):
    result = number%2 == 0
    return result
print(even_check(21))

def check_even_list(num_list):

    for number in num_list:
        if number%2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([3,5,7]))


def check_even_list(num_list):
    even_numbers =[]

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(check_even_list([1, 2, 3, 4, 5]))


stock_prices = [("APPL",200), ("GOOG",400), ("MSFT", 100)]
for ticker, price in stock_prices:
    print(price+(0.1*price))


work_hours = [('Mc', 300), ('Jayme', 400), ('Phil', 320)]
def employee_check(work_hours):    #check to see who have the most work hour
    current_max = 0
    employee_of_the_month=''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return(employee_of_the_month,current_max)
print(employee_check(work_hours))

name, hours = employee_check(work_hours)
print(name)
print(hours)



#guseeing game (shuffle ball)
example = [1,2,3,4,5,6,7]
mylist = ['','o','']

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0,1 or 2: ")

    return int(guess)
player_guess()

def check_guess(mylist, guess):
    if mylist[guess]== 'o':
        print("Correct!")
    else:
        print("Wrong guesss!")
        print(mylist)
#Initial List
mylist = ['','o','']

#Shuffle List
mixedup_list = shuffle_list(mylist)

#User Guess
guess = player_guess()

#Check Guess
check_guess(mixedup_list, guess)



#  *  argument (add element as much a you want in tuple format)
def myfunc(a,b):
    # Retruns 5% of the sum of a and b
    return sum((a, b)) * 0.05

def myfunc(*args):     #put * onvvariable name then, that variable can take multiple value
    return sum(args)*0.05

print(myfunc(5,4,2,56,3,3))

# ** argument (add element as much a you want in dictionary format)
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='orange', veggie = 'garbage')


#mixed two arguments
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(12,20,30, fruit='orange', food='eggs', animal ='dog')


#lower switch with upper

def myfunc(string):
    new_string = ''
    for x in range(len(string)):
        if (x+1)%2==0:
            new_string += string[x].upper()
        else:
            new_string += string[x].lower()
    print(new_string)

myfunc('voraMet')


# like previous one above
string = 'hello my name is mc'
new_string = ''
for i in range(len(string)):
    if i%2 == 0:
        new_string = new_string + string[i].upper()
    else:
        new_string = new_string + string[i].lower()
print(new_string)

my_string = ''                  # joint string
my_string = my_string + 'Hello'
my_string = my_string + ' '
my_string = my_string + 'World'
print(my_string)
