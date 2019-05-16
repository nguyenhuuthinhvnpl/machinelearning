count_of_times_used = 0


def times_used():
    # global count_of_times_used
    count_of_times_used = 0
    count_of_times_used += 1
    return count_of_times_used


x = 5
for i in range(x):
    print(times_used())
