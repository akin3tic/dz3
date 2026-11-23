def average_grade(a,b,c):
    return (a+b+c)/3
    print(average_grade)
def grade_message(average):
    if average>=4.5:
        return 'Отлично'
    elif 3.5<=average<4.5:
        return 'Хорошо'
    elif average<3.5:
        return 'Нужно повторить материал'
o1 = average_grade(5, 4, 5)
print(round(o1,2), grade_message(o1))

o2 = average_grade(3, 4, 3)
print(round(o2, 2), grade_message(o2))