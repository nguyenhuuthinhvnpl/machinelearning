def dating_range(your_age):
    your_age = int(your_age)
    lower_range = int(your_age / 2) + 7
    upper_range = int(your_age) * 2 - 13
    if your_age >= 14 and lower_range >= 14:
        print("You can date people between", lower_range, "and", upper_range, "years old.")
    else:
        print("Your age is not suitable to folk rules!")


your_age = input("How old are you? ")
dating_range(your_age)
# print(your_age)
