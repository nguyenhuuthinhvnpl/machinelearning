# goal of the function is to square some number
# input: the number that is  going to squared
# output: the squared number
# there won't be any effects
def square(number):
    # all of the instructions for how to do the squaring thing
    print(type(number))
    answer = number * number
    return answer


def silly_function():
    print("This is a silly function.")
    return
    print("This is a statement after return keyword.")


x = input("What do you want to square ?")
x = float(x)
y = square(x)  # the variable y is assigned the value
# of the result of invoking the function square on the argument x
z = square(7)  # z equals square of 7
print("the squaring number of", x, " is ", y)
print(silly_function())
