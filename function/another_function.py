def get_int(msg):
    # some stuff  about the function <- this is ignored by python
    '''
    display msg to the user, return what the user types  as an int
    '''
    text = input(msg)
    number = int(message)
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


print(fused_multiply_add(2, 3, 4))
print(fused_multiply_add(2, 3, '4'))
