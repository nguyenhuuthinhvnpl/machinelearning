from function import another_function

# money = input("How many dollars is in your pocket?")
# amount = float(money)
amount = another_function.get_int("How many dollars in your pocket?")
print("Here, takes this $", str(amount), " now you have $", str(2 * amount))
