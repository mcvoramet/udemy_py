my_invest = input("Principal Amount: ")
my_interest = input("Interest(%): ")
my_time = input("How many month?: ")
invest = float(my_invest)
interest = float(my_interest)/100
time = int(my_time)
year = 12
# equation: my_invest[0]*(1+(my_interest[0]/year)**(my_time[1]))
your_year = time
end_year = str(your_year)
x = (interest/year)
y = 1 + x
z = y**time
my_networth = invest*z
my_nw = str(my_networth)
print("Your net worth in " + end_year + " month will be equal to " + my_nw + " baht.")



