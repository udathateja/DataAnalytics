# Condition Example
a = 20
b = 30
c = 50
if a > b:
    print("a is false")
elif b > c:
    print("b is false")
elif c > a:
    print("this is correct")
else:
    print("nothing")

if a > b:
    print("a is false")
elif b > c:
    print("b is false")
elif c < a:
    print("this is correct")
else:
    print("nothing")

# If you have only one statement to execute, you can put it on the same line as the if statement
a = 30
b = 20
if a > b: print("good")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

a = 330
b = 380
c = 390
print("a") if a > b else print("b") if b > c else print("c") if c < a else print("none")

# use logical operator
a = 330
b = 380
c = 390
print("a") if a > b and b < c else print("b") if b > c else print("c") if c < a else print("none")

# use logical operator
a = 330
b = 380
c = 390
print("a") if a > b or b < c else print("b") if b > c else print("c") if c < a else print("none")

# nested if statements
a = 20
if a > 10:
    print("ab")
    if a > 21:
        print("false")
    else:
        print("bb")
else:
    print("none")

# if you have no content for if then can use print
# nested if statements
a = 20
if a > 10:
    print("ab")
    if a > 21:
        print("false")
    else:
        print("bb")
else:
    print("none")
