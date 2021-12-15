import csv

school_number, class_number = map(lambda x: x.rjust(2, '0'), input().split())
with open('../MW/rez.csv', 'r', encoding='utf-8') as csvfile:
    table = csv.reader(csvfile, delimiter=',', quotechar='"')
    students = []
    next(table)
    for row in table:
        login = row[2].split('-')
        sc_n, cl_n = login[-3], login[-2]
        if sc_n == school_number and cl_n == class_number:
            students.append((row[1].split()[3], row[-1]))
    for student in sorted(students, key=lambda x: (int(x[1]), x[0]), reverse=True):
        print(*student)
