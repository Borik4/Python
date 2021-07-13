def a(q):
    if q > 1:
        return q + a(q - 1)
    return 1


for i in range(11):
    print(a(i), end=",    ")
hell = 'hello world'
print(hell)
for i in range(123):
    print(i)
print('hello')`
