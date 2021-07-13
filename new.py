sudoku_1 = [7, [], 3, 2, [], [], 5, [], [],
          [], 9, [], 7, [], 5, [], 1, [],
          1, [], 5, [], [], [], [], [], [],
          3, 2, [], [], 5, 4, 8, 7, [],
          8, [], [], 3, 7, [], [], [], [],
          [], [], [], [], 2, 9, [], 6, [],
          [], 3, [], [], 4, 7, [], 5, 8,
          [], 7, 8, 5, 6, [], [], [], [],
          9, 5, [], [], 3, [], [], [], 7]
for i in sudoku_1:
    if type(i) is list:
        for q in range(1, 10):
            i.append(q)
sudoku = {}
for i in range(1, 82):
    sudoku[i] = sudoku_1[i-1]
def horizon():
    for i in range(9):
        a = []
        for q in range(9*i+1, 9*(i+1)+1):
            a.append(sudoku[q])
        stugum({(i, 'horizon'): a})


def uxxadzig():
    for i in range(9):
        a = []
        for q in range(i*9+1, 82, 9):
            a.append(sudoku[q])
        stugum({(i, 'uxxadziq'): a})


def stugum(o):
    int_1 = []
    list_1 = []
    q = list(o.values())[0]
    for w in range(len(q)):
        if type(q[w]) is int:
            int_1.append(q[w])
        else:
            list_1.append(q[w])
    for a in int_1:
        for q in list_1:
            if a in q:
                q.pop(q.index(a))

def nshum():
    for i in sudoku:
        if type(sudoku[i]) is list:
            if len(sudoku[i]) == 1:
                sudoku[i] = sudoku[i][0]
horizon()
print(sudoku)
uxxadzig()
print(sudoku)
nshum()
print(sudoku)