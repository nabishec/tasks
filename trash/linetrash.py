def group(n):
    if n <= 1:
        return 0
    count = 0
    quaer = 1
    while n > quaer:
        count += 1
        quaer *= 2
    return count

def movements_number(people_number):
    number = 0
    while people_number > 2 ** number:
        number += 1
    return number

for i in range(100):
    print(group(i), '-', movements_number(i), '----', i)