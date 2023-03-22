# With the while loop we can execute a set of statements as long as a condition is true....
i = 2
while i < 10:
  print(i)
  i = i + 1

# use break statement to stop Loop

i = 2
while i < 10:
  print(i)
  if i == 3:
    break
  i = i + 1


i = 2
while i < 10:
  print(i)
  i = i + 1
  if i == 6:
    break

# With the continue statement we can stop the current iteration, and continue with the next:
i = 2
while i < 12:
  print(i)
  if i == 5:
    print(i)
  i = i + 1

# With the continue statement we can stop the current iteration, and continue with the next:
i = 1
while i < 12:
  i = i + 1
  if i == 5:
    continue
  print(i)

# use else statement with while

i = 1
while i < 12:
  i = i + 1
  if i == 5:
    continue
  print(i)
else:
  print("out of loop")

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

world = "I love my country"
for x in world:
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:
world = "I love my country"
for x in world:
  if x =="c":
    break
  print(x)

world = "I love my country"
for x in world:
  print(x)
  if x =="c":
    break
  #print(x)

# With the continue statement
world = "I love my country"
for x in world:
  if x =="c":
    continue
  print(x)


world = "I love my country"
for x in world:
  print(x)
  if x =="c":
    continue
# use range
for x in range(6):
  print(x)
for x in range(2,6):
  print(x)
for x in range(2,7,2):
  print(x)

# use else in for loop
for x in range(2,7,2):
  print(x)
else:
  print("loop close")

# A nested loop is a loop inside a loop
company = ["Maruti","Hundai","Tata"]
performance = ["Good","Very Good", "Average"]
for x in company:
  for y in performance:
    print(x,y)
# use pass when we dont have statemnet in for
company = ["Maruti","Hundai","Tata"]
performance = ["Good","Very Good", "Average"]
for x in company:
  for y in performance:
    pass
# display all elemnets of list
team_score = [12,13,14,15,[23,26,29],67,78]
for i in team_score:
    print(i)
# display all elemnets of list and sublist
for i in team_score:
    if type(i) == list:
        for team_score in i:
            print(team_score)
    else:
        print(i)

# sum of all numbers stored in a list
numbers = [2,4,6,8,9,11,34]
sum  = 0
for i in numbers:
    sum = sum + i
print(sum)
# use while loop to sum of all numbered store in list
sum = 0
i = 0
while i < len(numbers):
    sum = sum + numbers[i]
    i = i + 1
print(sum)

# use while loop to sum number from 1 to 10
i = 1
n = 10
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1 # update counter
    print(sum)


