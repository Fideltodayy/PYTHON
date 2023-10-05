#here we define our global variable
x = "Python"

#accessing global x before it gets overriden
print(x + " is my best language")

#function that illustrates how we make the local variable to be global
def localToGlobal():
    #using the global keyword to make the local variable global
    global x 
    x = "Javascript"
    print(x + " is my favourite language")

#we call the function 
localToGlobal()

#here we see that variable x was overriden globally using the global keyword
print(x + " is my favourite language")