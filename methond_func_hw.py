# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (rad**3)*(4/3)*3.14

print(vol(2))
print("\n")

# Write a function that checks whether
# a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if num in range(low, high+1):
        print(f'{num} is in range of low and high')
    else:
        print('not in range')

print(ran_check(4,3,7))
print("\n")

# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.

def up_low(s):
    d = {"upper": 0, "lower": 0}
    lowercase = 0
    uppercase = 0

    for char in s:
        if char.isupper():
            d['upper'] +=1
        elif char.islower():
            d['lower']+=1
        else:
            pass

    print(f"Original String: {s}")
    print(f'Lowercase Count: {d["lower"]}')
    print(f'Uppercase Count: {d["upper"]}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
print("\n")


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers

print(unique_list([1,1,1,1,2,2,3,4,5,5]))
print("\n")

# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total

print(multiply([1,2,3,-4,10]))
print("\n")

# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    # remove spaces string
    s = s.replace(' ', '')
    # check if string is == reversed version of the string
    return s == s[::-1]

print(palindrome('nurses run'))
print("\n")

# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet = string.ascii_lowercase):

    # create a set of alphabet
    alphaset = set(alphabet)

    print(alphaset)
    # remove any spaces from the input string
    str1 = str1.replace(" ", "")
    print(str1)
    # covert into all lowercase
    str1 = str1.lower()
    print(str1)
    # grab all unique letters from the string set()
    str1 = set(str1)
    print(str1)
    # alphabet ser == string set input
    return str1 == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))