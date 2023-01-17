titanic_data_list = [
    (3, 21.0, 'M', 0, 'Assaf, Mr.Gerios'),
    (3, 23.0, 'M', 0, 'Assam, Mr.Ali'),
    (3, 17.0, 'F', 0, 'Attalah, Miss.Malake'),
    (3, 30.0, 'M', 0, 'Attalah, Mr.Sleiman'),
    (3, 23.0, 'M', 0, 'Augustsson, Mr.Albert'),
    (3, 13.0, 'F', 1, 'Ayoub, Miss.Banoura'),
    (2, 25.0, 'M', 0, 'Stokes, Mr.Philip Joseph'),
    (2, 18.5, 'M', 0, 'Swane, Mr.George'),
    (1, 18.5, 'F', 1, 'Swane, Mr.George'),
    (3, 20.0, 'M', 1, 'Abrahamsson, Mr. Abraham August Johannes')
]

cabin_three_count = 0
male_survival_count = 0
female_survival_count = 0

for row in titanic_data_list:
    if row[0] == 3:
        cabin_three_count += 1

    if row[2] == 'M' and row[3] == 1:
        male_survival_count += 1

    if row[2] == 'F' and row[3] == 1:
        female_survival_count += 1

print('Cabin three count: ', cabin_three_count)
print('Male survival count: ', male_survival_count)
print('Female survival count: ', female_survival_count)
