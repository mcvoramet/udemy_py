# LEGB rules
# Python will look through the program from this order L->E->G->B

# G (GLOBAL)
name = 'THIS IS A GLOBAL STRING'

def greet():
    # E (ENCLOSING)
    name = 'Sammy'


    def hello():
        # L (LOCAL)
        print('Hello ' +name)

    hello()


greet()
print('\n')


#Scope
x = 50

def func(x):

    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X TO {x}')
    return x

print(x)

func(x)

x = func(x)

print(x)
