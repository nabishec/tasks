a = input()
b = input()
index = -1
spec  = ''
flag = False
answer = ''
for i in range(len(b)):
    if flag:
        spec += b[i]

    if b[i] == '<':
        flag = True
    elif b[i] == '>':
        flag = False

        if spec == 'bspace>':
            if index > -1:
                answer = answer[:index] + answer[index + 1:]
                index -= 1
        elif spec == 'delete>':
            answer = answer[:index + 1] + answer[index + 2:]
        elif spec == 'left>': 
            if index > -1:
                index -= 1
        elif spec == 'right>':
            if index < len(answer) - 2:
                index += 1
        else:
            answer += spec
            index += len(spec)
        spec = ''

    if not flag and b[i] != '>':
        answer = answer[:index + 1] + b[i] + answer[index + 1:]
        index += 1
print('YES') if answer == a else print('NO')