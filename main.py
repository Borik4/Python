# sudoku = [[2, 6, 3, 1, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 5, 8],
#           [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 5, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9],
#           [9, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
#           [[1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8, 9, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
#           [1, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 3],
#           [4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 3, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 1],
#           [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9, 8, 7],
#           [8, 9, 1, 7, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 7, 8, 9]],
#           [5, [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8, 9, 3, 6, 1, 2]]
sudoku = [[7, [], 3, 2, [], [], 5, [], []],
          [[], 9, [], 7, [], 5, [], 1, []],
          [1, [], 5, [], [], [], [], [], []],
          [3, 2, [], [], 5, 4, 8, 7, []],
          [8, [], [], 3, 7, [], [], [], []],
          [[], [], [], [], 2, 9, [], 6, []],
          [[], 3, [], [], 4, 7, [], 5, 8],
          [[], 7, 8, 5, 6, [], [], [], []],
          [9, 5, [], [], 3, [], [], [], 7]]
for i in sudoku:
    for w in i:
        if type(w) is list:
            for q in range(1, 10):
                w.append(q)

print(sudoku)
print()
print()
def sxal():
    print('anything is wrong')

def stugum():
    for i in range(len(sudoku)):
        for o in range(len(sudoku[i])):
            if type(sudoku[i][o]) is list:
                if len(sudoku[i][o]) == 1:
                    f = sudoku[i][o][0]
                    sudoku[i][o] = f
                elif len(sudoku[i][o]) == 0:
                    sxal()


def horizon():
    for i in range(len(sudoku)):
        stugum_9(sudoku[i])


def uxxadzig():
    for i in range(9):
        q = []
        for a in sudoku:
            q.append(a[i])
        stugum_9(q)


def stugum_9(q):
    int_1 = []
    list_1 = []
    for w in range(len(q)):
        if type(q[w]) is int:
            int_1.append(q[w])
        else:
            list_1.append(q[w])
    for a in int_1:
        for q in list_1:
            if a in q:
                q.pop(q.index(a))

def kubik():
    for i in range(3):
        for a in range(3):
            q = []
            for s in range(3*a, 3*(a+1)):
                for t in range(3*i, 3*(1+i)):
                    q.append(sudoku[s][t])
            stugum_9(q)

kubik()
horizon()
uxxadzig()
stugum()
kubik()
horizon()
uxxadzig()
stugum()
kubik()
horizon()
uxxadzig()
stugum()
kubik()
horizon()
uxxadzig()
stugum()
kubik()
horizon()
uxxadzig()
stugum()
kubik()
horizon()
uxxadzig()
stugum()
print(sudoku, '          ygygyg')