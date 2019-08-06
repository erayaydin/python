# define new user function
def hello():
    # Say hello to user
    pass

# call the created function
hello()

# get type of function
print(hello)

# get arguments in functions
def hello(name):
    print('Hello', name)

hello('Eray')

# return a value
def plus(number, other):
    return number + other

print('3+2=' + str(plus(3,2)))

# use another function
def avg(number, other):
    total = plus(number, other)
    return total / 2

print('average of 3 and 5 is', avg(3,5))

# return multiple value
def plusAndAverage(number, other):
    total = plus(number, other)
    avg = total / 2
    return total, avg


tot, average = plusAndAverage(3,5)
print('total of 3 and 5 is', tot)
print('average of 3 and 5 is', average)
