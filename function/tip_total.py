from function import another_function

print("Hello", "Goodbye", sep=' and then ', end='\n This is rhe end \n')
cost = float(input("How much was your meal ?"))
tip = another_function.calc_tip(cost, max_value=1)
total = cost + tip
print("You should pay the total of ", total)
pig_total = another_function.calc_tip(cost, 25, 1)
print("If you were really impressed, you should pay", cost + pig_total)
