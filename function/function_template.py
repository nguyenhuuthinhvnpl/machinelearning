def square(number):
    """
    Squares a number. e.g., square(11) returns 121
    :param number:
    :return:
    """
    answer = number * number
    return answer


print('a =', square(11))
print('b =', square(9 + 2))
x = 11
y = square(x)
print('c =', y)
square(x)
print(x)
