import csv

count = 0
count_30 = 0
f = 0
s = input('Search for: ')  # 3) поиск книги по автору

with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        count += 1  # 1) счётчик количества записей в файле

        if len(row[1]) > 30:
            count_30 += 1  # 2) счётчик количества записей, у которых в поле "Название" строка длиннее 30 символов

        if s == row[3] and (row[6][6:10] == '2014' or row[6][6:10] == '2016' or row[6][6:10] == '2017'):  # 3') ограничение на выдачу для 3 варианта
            print(row[1])
            f = 1

    if f == 0:
        print('Nothing found')

    print(count)
    print(count_30)

# 4) генератор библиографических ссылок для 20 записей
with open('books.csv') as csvfile:
    tab = csv.reader(csvfile, delimiter=';')
    txt = open('test.txt', 'a')
    k = 0
    n = 0
    for st in list(tab)[1:]:
        n += 1
        txt.write(str(n) + '. ' + st[3] + '. ' + st[1] + ' - ' + st[6][6:10] + '\n')
        k += 1
        if k == 20:
            break
    txt.close()
