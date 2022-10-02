# udemy function practive exercise

# LESSER OF TWO EVENS: Write a function that returns
# the lesser of two given numbers
# if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_of_two_events(a,b):
    if a%2 == 0 and b%2 == 0:
        ans = min(a, b)
    else:
        ans = max(a, b)
    print(ans)

lesser_of_two_events(2,5)
print("\n")

# ANIMAL CRACKERS: Write a function takes a two-word
# string and returns True if both words begin with same letter

def animal_crackers(test):
    first = test[0]
    for i in range(len(test)):
        if test[i] == ' ':
            last = test[i+1]
    if last.upper() == first.upper():
        print(True)
    else:
        print(False)


animal_crackers('Jasper Chun')
print("\n")

# MAKES TWENTY: Given two integers, return True if the sum of the
# integers is 20 or if one of the integers is 20. If not, return False¶

def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        print(True)
    elif n1 == 20 or n2 == 20:
        print(True)
    else:
        print(False)

makes_twenty(3, 17)

def makes_twenty_sol (n1, n2):
    return n1+n2 == 20 or n1 == 20 or n2 ==20

print (makes_twenty_sol(3,17))
print("\n")

# OLD MACDONALD: Write a function that capitalizes
# the first and fourth letters of a name

def old_macdonald(name):
    new_name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    print(new_name)

old_macdonald('voramet')


def old_macdonald_sol(name):
    first_half = name[:3]
    second_half = name[3:]

    print(first_half.capitalize() + second_half.capitalize())
    print("\n")

old_macdonald_sol("voramet")


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join()
# method allows you to join together strings in a list
# with some connector string. For example, some uses of the .join() method:
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted
# to turn back into a sentence, you could just join them
# with a single space string:
# >>> " ".join(['Hello','world'])
# >>> "Hello world"
# I am home
# 012345678

def master_yoda(text):
    word = []
    word_list = text.split()
    a = -1
    for i in word_list:
        word.append(word_list[a])
        a = a - 1

    print(" ".join(word))

master_yoda("I am home")


def master_yoda_sol(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    print(" ".join(reverse_word_list))

master_yoda_sol('I am home')
print("\n")

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(n):
    list_num = []
    list_ans = []
    for i in range(0, 11):
        if n + i == 100 or n - i == 100 or n + i == 200 or n - i == 200:
            list_num.append(True)
        else:
            list_num.append(False)

    for j in list_num:
        if j == True:
            list_ans.append(j)

    list_ans.append(0)
    if list_ans[0] == True:
        print(True)
    else:
        print(False)

almost_there(209)

def almost_there_sol(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there_sol(209))
print('\n')


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    result_list = []
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3, 3]:
            result_list.append(True)
    result_list.append(0)
    if result_list[0] == True:
        print(True)
    else:
        print(False)

has_33([3,3,1])

def has_33_sol(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3, 3]:
            return True
    return False

print(has_33_sol([3,3,1]))
print('\n')


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = []
    for i in range(0, len(text)):
        result.append(text[i]*3)
    print("".join(result))

paper_doll('Hello')


def paper_doll_sol(text):
    result = ''

    for char in text:
        result += char*3
    return result


print(paper_doll_sol('Hello'))
print('\n')


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(a, b, c):

    if a > 11 or b > 11 or c > 11 or a < 1 or b < 1 or c < 1:
        print('Invalid the valid value should be in range from 1 to 11')
    elif a + b + c <= 21:
        print(a + b + c)
    elif a + b + c > 21:
        if a == 11 or b == 11 or c == 11:
            print((a + b + c) - 10)
        else:
            print('BUST')


blackjack(5, 6, 7)
blackjack(9, 9, 9)
blackjack(9, 9, 11)


def blackjack_dol(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return 'BUST'


print(blackjack_dol(5, 6, 7))
print(blackjack_dol(9, 9, 9))
print(blackjack_dol(9, 9, 11))
print('\n')


# SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting
# with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(arr):
    list_69 = []
    list_no_69 = []
    for i in range(0, len(arr)):
        if arr[i] == 6 or arr[i] == 7 or arr[i] == 8 or arr[i] == 9:
            list_69.append(arr[i])
        else:
            list_no_69.append(arr[i])
    ans = 0
    for j in list_no_69:
        ans = ans + j
    print(ans)


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])


def summer_69_sol(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69_sol([1, 3, 5]))
print(summer_69_sol([4, 5, 6, 7, 8, 9]))
print(summer_69_sol([2, 1, 6, 9, 11]))
print('\n')



# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    james_bond = []
    result = []
    x = 0
    for i in nums:
        if i == 0 or i == 7:
            james_bond.append(i)
    for j in range(0, len(james_bond)-1):
        if james_bond[j:j+3] == [0, 0, 7]:
            result.append(True)
    result.append(0)
    if result[0] == True:
        print(True)
    else:
        print(False)


spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 7, 2, 0, 4, 5, 0])


def spy_game_sol(nums):

    code = [0, 0, 7, 'x']
    # .pop --> if it match then pop it out of the lsit
    # [0, 7, 'x']
    # [7, 'x']
    # ['x'] length = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game_sol([1, 2, 4, 0, 0, 7, 5]))
print(spy_game_sol([1, 0, 2, 4, 0, 5, 7]))
print(spy_game_sol([1, 7, 2, 0, 4, 5, 0]))
print('\n')


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(num):

    # Check for 0 or 1 input
    if num < 2:
        return 0
    # Store our prim numbers
    primes = [2]
    # Count going up through every number up to input num
    x = 3

    # x is going through every number up to input num
    while x <= num:
        # Check if x is prime
        for y in range(3, x, 2): #can replace rage(3, x, 2) with primes (list)
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
print('\n')


# Print Big Letter

def print_big(letter):
    patterns = {1:'  *  ', 2:' * * ', 3:'*   *', 4:'*****', 5:'**** ',
                6:'   * ', 7:' *   ', 8:'*  * ', 9:'*    '}
    alphabet = {'A':[1, 2, 4, 3, 3], 'B':[5, 3, 5, 3, 5], 'C':[4, 9, 9, 9, 4],
                'D':[5, 3, 3, 3, 5], 'E':[4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')
print(' ')
print_big('b')
print(' ')
print_big('c')
print(' ')
print_big('d')
print(' ')
print_big('e')




























































