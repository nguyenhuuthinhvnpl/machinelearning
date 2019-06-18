def get_int(msg):
    # some stuff  about the function <- this is ignored by python
    '''
    display msg to the user, return what the user types  as an int
    '''
    text = input(msg)
    number = int(text)
    return number


def fused_multiply_add(a, b, c):
    return a * b * c


def sphere_volume(radius):
    '''
    calculate the volume of a sphere
    :param radius: the radius of the sphere
    :return: the volumn of that sphere
    '''
    import math
    radius = float(input("What is the radius of your sphere ?"))
    volume = (4 / 3) * math.pi * (radius ** 3)
    print("The volume of your sphere is", volume)


# print(fused_multiply_add(2, 3, 4))
# print(fused_multiply_add(2, 3, '4'))


def amount_to_be_fancy(age):
    price = age // 2 + 20 + age - 3
    return price


def calc_tip(cost, percent=20, max_value=500):
    # percent = 20
    tip = cost * (percent / 100)
    return min(tip, max_value)


def leap_year(year):
    '''years divisible by 4,
       unless they divisible by 100,
       unless they divisible by 400'''

    div4 = (year % 4) == 0
    div100 = (year % 100) == 0
    div400 = (year % 400) == 0

    if div400 or (div4 and not div100):
        return True
    else:
        return False
