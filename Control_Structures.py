# Booleans

my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello") #basically just true and false. Uses the equal == operator. 

# Note:  Python is case sensitive so typing true and True are two different things.

# Comparison

print(1 != 1)

print("eleven" != "seven")

print(2 != 10)  # != is the not equal operator. With this operator True = not equal // False = equal.

print(7 > 5)

print(10 < 10) # Basically greater than > and smaller than < .

# Note in the example 7 > 7.0 this equals to false because they are the same therfore the output is False.

print(7 <= 8) # Just examples of "greather or equal to", and "smaller than or equal to".

print (9 >= 9.0) # This would be True because 9 is equal to 9.0

# if Statements


if 10 > 5:
    print("10 greater than 5")

print("Program ended")

# To perform more complex checks, if statements can be nested, one inside the other.
# This means that the inner if statement is the statement part of the outer one. This is one way to see whether multiple conditions are satisfied. 

num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")   # Note: Indentation is used to define the level of nesting.

num = 7

if num > 3:

   print("3")

   if num < 5:

      print("5")

      if num ==7:       # In this example the output will be 3. The reason it does not output 7 is because since the first if statement is
                        # true  and the second is false python ignores the ones after it.
         print("7")     

# else Statements

x = 4
if x == 5:
    print("Yes")
else:
    print("No") # The else statement can be used to run statements when the condition of the if satement is False

# Every if condition block can have only one else statement.
# In order to make multiple checks, you can chain if and else statements. 

num = 3 
if num == 1:
    print("One")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")     # In this example the program checks and outputs the num variable's value as text

# Note: Indentation determines which if/else statements the code blocks belong to.

# elif Statements

# Multiple if/else statements make the code long and not very readable.
# The elif (short for else if) statement is a shortcut to use when chaining if and else statements, making the code shorter. 

num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")  # The same example from before can be rewritten using elif statements

# A series of if elif statements can havea final else block, which is called if none of the if or elif expressions is True

# Boolean Logic 

print(1 == 1 and 2 == 2)

print(1 == 1 and 2 == 3)

print(1 != 1 and 2 == 2)

print(2 < 1 and 3 > 6)      # The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. Otherwise, it evaluates to False. 

# Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition.
# Python's Boolean operators are and, or, and not.

print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 >  6)      # The or operator also takes two arguments. It evaluates to True if either (or both) of its arguments are True, and False if both arguments are False

# Unlike other operators we've seen so far, not only takes one argument, and inverts it.
# The result of not True is False, and not False goes to True

print(not 1 == 1 )

print(not 1 > 7)

# Note: You can chain multiple conditional statements in an if statement using the Boolean operators.

# The below code shows that == has a higher precedence than or
print(False == False or True)

print(False == (False or True))

print((False == False) or True)    

# Operator precedence is a very important concept in programming. It is an extension of the mathematical idea of 
# order of operations (multiplication being performed before addition, etc.) to include other operators, such as those in Boolean logic.

# Note: Python's order of operations is the same as that of normal mathematics: parentheses first, then exponentiation, then multiplication/division, and then addition/subtraction.

grade = 88
if (grade >= 70 and grade <= 100):      # You can chain multiple conditional statements in an if statement using the Boolean operators. 
    print("Passed!")

# Lists

words = ["hello", "world", "!"]     # Lists are used to store items. A list is created using square brackets with commas separating items.
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)       # Sometimes you need to create an empty list and populate it later during the program.

number = 3 
things = ["string", 0, [1,2,number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])         # Typically, a list will contain items of a single item type, but it is also possible to include several different types. 
# Lists can also be nested within other lists. 

# Nested lists can be used to represent 2D grids, such as matrices.

m = [
    [1,2,3],
    [4,5,6]
]

print(m[1][2])
# A matrix-like structure can be used in cases where you need to store data in row-column format. For example, when creating a ticketing program, 
# the seat numbers can be stored in a matrix, with their corresponding rows and numbers. 

# Note: The code above outputs the 3rd item of the 2nd row.

str = "Hello world!"
print(str[6])       # Some types, such as strings, can be indexed like lists. Indexing strings behaves as though you are indexing a list containing each character in the string.

# Note: Space (" ") is also a symbol and has an index. 

