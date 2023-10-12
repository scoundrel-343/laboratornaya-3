# Ввод данных
flag = False
while flag == False:
    k = int(input('Введите номер вертикали для фигуры №1: '))
    l = int(input('Введите номер горизонтали для фигуры №1: '))
    m = int(input('Введите номер вертикали для фигуры №2: '))
    n = int(input('Введите номер горизонтали для фигуры №2: '))
    if (max(k, l, m, n) > 8) or (min(k, l, m, n) < 1):
        print('----------------------------------\n !Ошибка! Вводите числа от 1 до 8 \n----------------------------------')
    else:
        flag = True
figure = input('Введите название фигуры №1 (ферзь, ладья, слон или конь): ')

# Являются ли поля полями одного цвета
color_1 = k + l
color_2 = m + n
if (color_1 // 2) == (color_2 // 2):
    print('Поля одного цвета')
else: 
    print('Поля разного цвета')

# Функция для проверки угрозы фигурой №1
def is_threatened(k, l, m, n, figure):
    # Проверяем, угрожает ли фигура любым своим ходом полю (m, n)
    if figure == "ферзь":
        if k == m or l == n or abs(k - m) == abs(l - n):
            return True
    elif figure == "ладья":
        if k == m or l == n:
            return True
    elif figure == "слон":
        if abs(k - m) == abs(l - n):
            return True
    elif figure == "конь":
        if abs(k - m) == 2 and abs(l - n) == 1:
            return True
        elif abs(k - m) == 1 and abs(l - n) == 2:
            return True

    return False

# Функция для проверки угрозы фигурой №1 за два хода
def is_threatened_in_two_moves(k, l, m, n, figure):
    # Проверяем все возможные поля для первого хода
    for i in range(1, 9):
        for j in range(1, 9):
            # Проверяем, можно ли попасть на поле (i, j) за один ход
            if is_threatened(k, l, i, j, figure) and is_threatened(i, j, m, n, figure):
                return (i, j)
            else:
                return False

# Проверяем, угрожает ли фигура №1 полю
if is_threatened(k, l, m, n, figure):
    print("Фигура угрожает полю")
else:
    print("Фигура не угрожает полю")

# Проверяем, угрожает ли фигура №1 полю за два хода
if is_threatened_in_two_moves(k, l, m, n, figure):
    result = is_threatened_in_two_moves(k, l, m, n, figure)
    if len(result) > 1:
        print("Можно попасть на поле за два хода, первый ход в поле ({}, {})".format(result[0], result[1]))
    else: 
        print("Нельзя попасть на поле за два хода")
else:
    print("Нельзя попасть на поле за два хода")
