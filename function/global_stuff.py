count = 0


def run_count():
    global count
    count += 1
    return count


count += 1
print(run_count())
