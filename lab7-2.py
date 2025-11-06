def rotatee(table):
    n = len(table)
    for i in range(n):
        for j in range(i + 1, n):
            table[i][j], table[j][i] = table[j][i], table[i][j]
    for i in range(n):
        table[i].reverse()

def col_reverse(table):
    table.reverse()

def Row_reverse(table):
    for row in table:
        row.reverse()

n = int(input().strip())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

comm = input().strip()


for op in comm:
    if op == 'R':
        rotatee(table)
    elif op == 'H':
        col_reverse(table)
    elif op == 'V':
        Row_reverse(table)

for row in table:
    print(' '.join(map(str, row)))