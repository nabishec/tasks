'''
Форматирование файла
Петя - начинающий программист. Сегодня он написал код из n строк.

К сожалению оказалось, что этот код трудно читать.
Петя решил исправить это, добавив в различные места пробелы. А точнее, для i-й строки ему нужно добавить ровно ai пробелов.

Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace.
При нажатии на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела. При нажатии на Backspace в строке удаляется один пробел.

Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов в каждую строку. Помогите ему!

Формат ввода
Первая строка входных данных содержит одно целое положительное число n(1≤n≤105) – количество строк в файле.

Каждая из следующих n строк содержит одно целое неотрицательное число ai(0≤ai≤109) – количество пробелов, которые нужно добавить в i-ю строку файла.
Формат вывода
Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов. '''
# my solution
answer = 0
for i in range(int(input())):
    number_space = int(input())
    # print(answer,number_space,'--1')
    tubs = number_space // 4
    answer += tubs
    number_space -= tubs * 4
    # print(answer,number_space,'--2')
    backspaces = number_space // 3
    answer += 2 * backspaces 
    number_space -= backspaces * 3
    # print(answer,number_space,'--3')
    answer += number_space
    # print(answer,number_space,'--4')
print(answer)

# solution of yandex
n = int(input())
ans = 0
for i in range(n):
    a = int(input())
    ans += a // 4
    if a % 4 == 1 or a % 4 == 2:
        ans += a % 4
    if a % 4 == 3:
        ans += 2
print(ans)
'''
Решение яндекса лучше, так как использует меньше памяти
'''
