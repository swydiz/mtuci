def f(x, y):
    if y == 'file':
        with open(x, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    elif y == 'line':
        with open(x, 'r', encoding='utf-8') as file:
            for line in file:
                print(line)

f('example.txt', 'line')
f('example.txt', 'file')
