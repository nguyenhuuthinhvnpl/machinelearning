# set up: need to make a dict, but no need to make anything to have variables
# d = {}
#
# print(' create and access '.center(50, '-'))
#
# # create with name x
# x = 23
# d['x'] = 34
#
# # access name x
# print('x =', x)
# print("d['x'] =", d['x'])
#
#
# print(' create second and access '.center(50, '-'))
#
# # create name xyxxy based on x
# xyxxy = x + 45
# d['xyxxy'] = d['x'] + 56
#
# # access names x and xyxxy
# print('x, xyxxy =', x, xyxxy)
# print("d['x'], d['xyxxy'] =", d['x'], d['xyxxy'])
#
#
# print(' change value of '.center(50, '-'))
#
# # update an old name
# print('x was', x, end=' ')
# x = 0
# print('and became', x)
#
# print('x was', d['x'], end=' ')
# d['x'] = -1
# print('and became', d['x'])


### if you are curious: uncomment to see under the hood ###
print(locals())
print('x' in locals(), 'w' in locals())
print('variable w:', w)  # this is an error
locals()['w'] = 'Inserted! Ha!'
print('x' in locals(), 'w' in locals())
print('variable w:', w)  # this is not an error
