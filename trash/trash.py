def group(n):
    if n <= 1:
        return 0
    count = 0
    quaer = 1
    while n > quaer:
        count += 1
        quaer *= 2
    return count
print(group(int(input())))
    