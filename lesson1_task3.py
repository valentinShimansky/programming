print('please enter a pair of numbers, to stop the programm enter exit')

result = set()
while True:
    a = input()
    if a == 'exit':
        break
    a = a.split()
    temp = {i for i in range(int(a[0]), int(a[1]) + 1)}
    result = set.union(temp, result)
    print('result coverage:', len(result))