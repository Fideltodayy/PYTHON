# #recu

# def printnum(n):
#     if n==0:
#         return
#     print(n)
#     printnum(n-1)

# printnum(10)


#def star(n):
#    if n==0:
#        return "*"
#    else:
#        return star(n-1) + star(n-1)
#    
#
#print(star(5))
#


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler)

# username = input("Enter username:")
# print("Username is: " + username)


price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))