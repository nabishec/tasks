'''
Футбольный комментатор


Раунд плей-офф между двумя командами состоит из двух матчей. Каждая команда проводит по одному матчу «дома» и «в гостях».
Выигрывает команда, забившая большее число мячей. Если же число забитых мячей совпадает, выигрывает команда, забившая больше мячей «в гостях».
Если и это число мячей совпадает, матч переходит в дополнительный тайм или серию пенальти.

Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась). 
Помогите комментатору сообщить, сколько голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.
Формат ввода

В первой строке записан счёт первого мачта в формате G1:G2, где G1 — число мячей, забитых первой командой, а G2 — число мячей, забитых второй командой.

Во второй строке записан счёт второго (текущего) матча в аналогичном формате. Все числа в записи счёта не превышают 5.

В третьей строке записано число 1, если первую игру первая команда провела «дома», или 2, если «в гостях».
Формат вывода

Выведите единственное целое число "— необходимое количество мячей.
'''
#my solution
home = [0,0]
guest = [0,0]
home[0],guest[1] = map(int,input().split(':'))
guest[0],home[1] = map(int,input().split(':'))
flag = True
if int(input()) == 2:
    home[0], guest[0] = guest[0], home[0]
    home[1], guest[1] = guest[1], home[1]
    flag = False
g2 = guest[1] + home[1]
g1 = guest[0] + home[0]
if g1 > g2:
    print(0)
elif g2 == g1:
    if guest[0] <= guest[1]:
        print(1)
    else:
        print(0)
else:
    if flag:
        if g2 - g1 + guest[0] <= guest[1]:
            print(g2 - g1 + 1)
        else:
            print(g2-g1)
    else:
        if guest[0] <= guest[1]:
            print(g2 - g1 + 1)
        else:
            print(g2 - g1)

#solution of yandex
g11, g21 = map(int, input().split(':'))
g12, g22 = map(int, input().split(':'))

where = int(input())

if where == 1:
    score1 = g11 * 100 + g12 * 101
    score2 = g21 * 101 + g22 * 100
    print(score2,score1,score2-score1,(score2-score1)//101)
    print(max(0, (score2 - score1 + 101) // 101))
else:
    score1 = g11 * 101 + g12 * 100
    score2 = g21 * 100 + g22 * 101
    print(max(0, (score2 - score1 + 100) // 100))
'''
Как работает их решение?
Они дают разные значения голам дома и голам в гостях.
Когда в гостях забивают больше то получается отрицательное число,
и при добавлении к оно не дает округлиться так как деление целочиселнное.
Легче показать на примере:
Входные данные:
5:4
5:6
1
тогда 
score1 = 1005
score2 = 1004
score2 - score1 = -1
score2 - score1 + 101 = 100
100 // 101 = 0
Минус их решения в том что если счет может достичь сотни то ответ будет неккоректным
'''