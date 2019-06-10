# cost = int(input("How much is it ?"))
# if cost > 10:
#     cost -= 5
#     print("I'll give you", cost, "for it.")
#
# if  cost > 500:
#     print("I will be paying with a check.")
# else:
#     if cost > 20:
#      print("I will be paying with cash.")
#     else:
#         if cost <= 200:
#            print("I will be paying with a visa.")
#         else:
#             print("I will be paying with American express.")
#
#

cost = int(input("How much is it ?"))
if cost > 10:
    cost -= 5
    print("I'll give you", cost, "for it.")

if cost > 500:
    print("I will be paying with a check.")
elif cost > 20:
    print("I will be paying with cash.")
if cost <= 200:
    print("I will be paying with a visa.")
else:
    print("I will be paying with American express.  ")
