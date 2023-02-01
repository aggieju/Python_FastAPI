print("Hello, Python")


# declaring variables

name = "Guido van Rossum"
age = 67
created_python = True

print(name, age, created_python)
print(type(name), type(age), type(created_python))

# creating functions 

def my_function():
  print("Hello, function")

my_function()

def say_hi(name):
  print("Hi, " + name)

say_hi("AggieS")

def add(x, y):
  return x + y