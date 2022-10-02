#one.py

def func():

    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':   # check if it main or imported
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')

