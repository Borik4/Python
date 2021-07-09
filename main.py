def a(q):
    if q > 1:
        return q + a(q - 1)
    return 1
for i in range(11):
    print(a(i), end=",    ")
print('all')
