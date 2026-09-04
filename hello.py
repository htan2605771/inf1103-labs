print("==============================================")
print("Welcome here!")
print("My first post!")
print("==============================================")

## a. Yes
## b. top to bottom
## c. the output appears in the python terminal

## Activity 2
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

## activity 2 answers:
## a. they are storing data so i can reuse the value multiple times without retyping it.
## b. yes if i were to change the cool_creator to just creator, run it again, the output will print Username: creator

## Activity 3 
followers += 50
print("day 1:", followers)

followers += 20
print("day 2:", followers)

followers -= 10
print("day 3:", followers)

## activity 3 answers
## a. no the += and -= does the reassignment for me
## b. each operation builds on whatever followers currently holds not the original 100 thats why the numbers keep climbin
## c. it updates a variable based on its current value 

## Activity 4
username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("=====================")
print("Username:", username)
print("Age:", age)
print("Category:", category)

## activity 4 answers
## a. displays as a prompt then pauses until user types something and presses Enter then displays the entered value at the end of the program
## b. dynamic. 

## Activity 5
if age>40 and category == "fun":
    print("you are old what is fun for you??")

## activity 5 answers
## a. always returns a string even if the user types numbers
## b. if statement uses and to check 2 conditions at once. both conditions must be true for the message to print
