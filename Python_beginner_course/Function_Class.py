# Lambda Function example and class
# This can take any number of arguments, but can only have one expression
lambda arguments: expression

# add number
result = lambda x: x + 10

print(result(6))

# using 2 arguments

result1 = lambda a, b: a * b
print(result1(2, 3))


# use in def--make a function that always doubles the number you send in:

def myfunc(a):
    return lambda x: x * a


doubler = myfunc(2)

print(doubler(8))


# use in def--make a function that always doubles the number you send in:

def myfunct1(x):
    return lambda a: a * x


trippler = myfunct1(3)
print(trippler(11))


# Mix both above functions

def myfunct2(x):
    return lambda a: a * x


doubler1 = myfunct1(2)
trippler1 = myfunct1(3)

print(doubler1(11))
print(trippler1(11))


# An array is a special variable, which can hold more than one value at a time.

class myclass:
    x = 10


print(myclass)

# Now we can use the class named MyClass to create objects:Create an object named p1, and print the value of x:
p1 = myclass()
print(p1.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('john', 36)
print(p1.age)
print(p1.name)


# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(myself, name, age):
        myself.name = name
        myself.age = age

    def myfunc(myself1):
        print("Hello my name is " + myself1.name)


p1 = Person("Raam", 40)
p1.myfunc()

# Modify Object Properties
# set age of p1 to 50

p1.age = 50

print(p1.age)

# Delete the age property from the p1 object:
del p1.age
print(p1.age)

# delete object
del p1
print(p1)


# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Create Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x_object = Person("atul", "patel")
x_object.printname()


# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a child class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass


# Now the Student class has the same properties and methods as the Person class.

y_object = Student("Ravi", "Taneja")
y_object.printname()


# We want to add the __init__() function to the child class (instead of the pass keyword).

class Student(Person):
    def __init__(self, firstname, lastname):
        pass


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
    def __init__(self, stdname, age):
        self.stdname = stdname
        self.age = age

    def printstd_name_age(self):
        print(self.stdname, self.age)


x_std = Student("Atul", 36)
x_std.printstd_name_age()


# Note- The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)


x_std1 = Student("Raam", "Taja")
x_std1.printname()


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)


x_std2 = Student("Raama", "Ta")
x_std2.printname()


# Add a property
# called graduationyear to the Student class:

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduationyear = 1999


x_std3 = Student("Raama", "Taaaa")
print(x_std3.graduationyear)


# In the example below, the year 1999 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year


x_std3 = Student("Raama", "Taaaa", 1995)
print(x_std3.graduationyear)


# Add method
# Add a method called welcome to the Student class:

class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x_stud4 = Student("Rishav", "Malhora", 2002)
x_stud4.welcome()