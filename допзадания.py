import csv

tags = []
popular = []

with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        popular.append([int(row[8]), row[1]])

        tags.append(row[12])
        t = ''.join(tags)

    c = []
    d = list(t.split('#')[1:])
    for i in range(len(d)):
        c.append(str.strip(d[i]))
    a = 0
    g = sorted(list(set(c)))
    for j in range(len(g)):
        a += 1
        print(a, g[j])

    pop = sorted(popular, reverse=True)
    w = 0
    while w < 20:
        print(pop[w][1])
        w += 1
