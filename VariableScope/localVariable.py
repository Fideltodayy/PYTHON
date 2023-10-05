#here we define our global variable
x = "Javascript"

#function to show local scope of variable x
def localScope():
    #x becomes our local variable that can only be used within this function's scope
    x = "Python"
    print(x + " is my best language")

#we call our function to display the local scope of x
localScope()
#our global x variable remains just as it was in the outer scope
print(x + " is my best language")
