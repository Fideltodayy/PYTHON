#here we declare the variable outside the function and in the global scope
x = "Amazing"

def globalScope():
    #here we access the global variable that is declared outside of this function
    print("Python is " + x)

#we call our function here
globalScope()
#we are globaly accessing our global variable in the same scope for clarity
print("Python is " + x)