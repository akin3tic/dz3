def analyze_scores(*scores):
    if len(scores) == 0:
            s = 0
            l = 0
            mc = 0
    else:
        s = sum(scores)
        l = len(scores)
        mc = s / l
    return s,l,mc
def print_report(team_name, **info):
    print('Команда:', team_name)
    for i in info:
        print(i, ':', info[i])
print(analyze_scores(8, 10, 7, 9))
print(analyze_scores(5, 5))
print(analyze_scores())
print_report('Комета', coach='Тимур', city='Докшицы')