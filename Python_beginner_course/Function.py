# Function Example
def my_function():
    print("hello")


my_function()


# add arguments

def model_car(cname):
    print(cname + "Good")


model_car("maruti")


# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that are sent to the function when it is called.

def my_fun(a, b):
    print(a + " " + b)


# a function must be called with the correct number of arguments
my_fun("Maruti", "Red")


# If use incorrect arguments then will get error
# my_fun("Maruti")

# If the number of arguments is unknown, add a * before the parameter name:This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_family(*kids):
    print("My younger son" + " " + kids[2])


my_family("Ram", "Rahul", "Honey")


# we can also send argument with key=Value

def team_run(player1, player2, player3):
    print("Highest runner in all match" + " " + player2)


team_run(player1="Rohit", player2="Virat", player3="raina")


# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_family1(**kids):
    print("My younger son" + " " + kids["lname"])


my_family1(fname="Ram", lname="Kapoor")


# How to use the default parameter Value

def my_family2(country="Italy"):
    print("My favourite country" + " " + country)


my_family2()
my_family2(country="Rome")


# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

def my_food(fruits):
    for x in fruits:
        print(x)


fruits_local = ["Banana", "mango", "apple"]
my_food(fruits_local)


# To let a function return a value, use the return statement:

def addition_3number(a, b, c):
    return print(a * b * c)


addition_3number(2, 3, 4)


# recursion my_function
def recursion_exp(k):
    if k > 0:
        result = k + recursion_exp(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nrecursive Example")
recursion_exp(7)
