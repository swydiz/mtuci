def f(x, y):
    try:
        if y == 'all':
            with open(x, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        elif y == 'line':
            with open(x, 'r', encoding='utf-8') as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print(f"Файл '{x}' не найден. Пожалуйста, проверьте имя файла и попробуйте снова.")

f('example.txt', 'line')
f('example.txt', 'all')