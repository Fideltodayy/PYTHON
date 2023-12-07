#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

a = 4
b = 5

if a>b:
    print("a is greater than b")
elif a==b:
    print("b is equal a")
else:
    print("a is NOT equal to b")


#THe shorthand if statement
#This technique is known as Ternary Operators, or Conditional Expressions.

a = 15
b = 8
print("A is bigger than B") if a>b else print(" Bis bigger than A")