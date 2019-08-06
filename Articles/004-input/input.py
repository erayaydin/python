# get input from user
print('Please type your name: ', end='')
name= input()
print('Hello', name)

# define a function
def hello(name):
    print('Hello', name)

# use user's input on function's parameter
hello(name)

# changing type of input (Normally, user input is str)
print('Please type your age: ', end='')
age=input()
print(type(age))
age = int(age)
print(type(age))
year = 2017 - age
print('Your birth year:', str(year))
