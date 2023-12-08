def say_hi(name):
    print("Hello " + name)
say_hi("Fidel")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")