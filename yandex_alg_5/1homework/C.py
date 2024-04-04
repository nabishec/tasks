answer = 0
for i in range(int(input())):
    number_space = int(input())
    print(answer,number_space,'--1')
    tubs = number_space // 4
    answer += tubs
    number_space -= tubs * 4
    print(answer,number_space,'--2')
    backspaces = number_space // 3
    answer += 2 * backspaces 
    number_space -= backspaces * 3
    print(answer,number_space,'--3')
    answer += number_space
    print(answer,number_space,'--4')