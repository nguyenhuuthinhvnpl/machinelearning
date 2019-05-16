def five_grade(student, grade):
    """
    This is a example of a bad function. It ignores the arguments, using input() instead. Never do it
    :param student:
    :param grade:
    :return:
    """
    student = input('Which student ?')
    grade = input('What grade ?')
    print('The grade of', student, 'is', grade)


five_grade('Brunelle', 'A+')
