def f(x, y=2, z='yes'):
    return (z + '') * (x + y)


f(3)
f(3, 5)
f(3, 5, 'no')
f(3, 5, z='no')
