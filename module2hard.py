#      Согласно заданию "В первом поле камни с числом менялись постоянно (от 3 до 20)
#      случайным образом, а второе было всегда пустым.
#      Соответственно в основе порграммы будет цикл

import random                                                                # Вызываем внешнюю функцию

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # Создаем список допустимых значений
number = random.choice(numbers)                                              # Выпадает камень со случайным числом
print("Пароль для цифры - ", number)                                         # Выводим в консоль подсказку
print()                                                                      # Пропускаем строку
for n in range(3, 21):                                                       # Задаем цикл от 3 до 20
    if n == number:                                                          # Если случайное число не равно n, цикл запускается
                                                                             # с сначала, так программа работает быстрее
        print(f'{n} = ', end='')                                             # Выводим в консоль 'n = '
        for x1 in range(1, n):                                               # Вычисления
            for x2 in range(x1 + 1, n):
                if n % (x1 + x2) == 0:
                    print(f"{x1}{x2}", end='')                               # Выводим в консоль пароль
print()


