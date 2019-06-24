def new_abs(number):
    """
    return the absolute value of the argument
    :param number:
    :return:
    """
    if number > 0:
        return number
    else:
        return -1 * number


print(new_abs(8))
print(new_abs(-8))
print(new_abs(8.0))
print(new_abs(-8.0))
print(new_abs(0.0))
print(new_abs(-0.0))
