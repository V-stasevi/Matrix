import numpy as np

def transpose(cols, rows, args):
    try:  # проверка ввода строк
        rows = int(rows)
        if rows < 1:
            return "Ошибка! Введите значение ROWS больше нуля!"
    except Exception as e:
        return "Ошибка! Значение ROWS должно быть числом!"

    try:  # проверка ввода столбцов
        cols = int(cols)
        if cols < 1:
            return "Ошибка! Введите значение COLS больше нуля!"
    except Exception as e:
        return "Ошибка! Значение COLS должно быть числом!"

    matrix = []  # создание пустого массива

    try:  # проверка ввода значений
        args = [int(x) for x in args.split('_')]
    except Exception as e:
        return "Ошибка! ARGS введены неверно!"

    if len(args) != cols * rows:
        return "Ошибка! Кол-во ARGS не соответствует размарам матрицы!"

    for i in range(int(rows)):  # массив в матрицу
        matrix.append(args[i * cols: (i + 1) * cols])
        print(matrix[i])  # печать в терминал

    return np.transpose(np.array(matrix))  # вывод транспонированной матрицы