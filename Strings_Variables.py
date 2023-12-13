## Strings


print("Hello world!")

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!') # backlash for quotes within string quote

print('One\nTwo\nThree') # \n represents a new line

print("""this
is a
multiline
text""") # Newlines will be automatically added for strings that are created using three quotes. 

# Concatenation

print("Spam" + "eggs") # Output will be Spameggs
print("2" + "2") # output will be 22

# String Operations

print("spam *3") # output is spamspamspam

## Variables


user = "James" # A variable allows you to store a value by assigning it to a name
# example of working with variable
x = 7
print(x)

print(x+3)
print(x)

# Variables can be reassigned as many times as you want, in order to change their value. 
x = 123.456
print(x)

x = "This is a string"
print(x + "!")
# First output will be 123.456, Second output will be "This is a string!"

# Input: Getting input from the user

x = input()
print (x)

name = input("Enter your name: ") # You can provide a string in the parentheses to produce a prompt message
print("Hello, " + name) 

age = int(input()) # this is used to convert to Integer, since the input returns a String
print(age) 

age = 42
print("His age is " + str(age)) # Similarly, in order to convert a number to a string, the str() function is used. 

name = input()
age = input()
print(name + " is " + age)   # You can use input() multiple times to take multiple user inputs. 


x = 2
print(x)

x += 3
print(x)
# In-place operators allow you to write code like 'x = x + 3' more concisely, as 'x += 3'. 
# The same thing is possible with other operators such as -, *, / and % as well. 

x = "spam"
print(x)

x += "eggs"
print(x) # These operators can be used on types other than numbers, as well, such as strings

num = int(input())
print(num)
    #|      Walrus operator := allows you to assign values to variables within an expression, including variables that do not exist yet. 
    #V      The walrus operator accomplishes these operations at once: 
print(num:=int(input()))
