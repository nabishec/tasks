
def answer(count,n):
    mnoj = 2
    while n >= mnoj:
        if n % mnoj == 0:
            n = n // mnoj
            mnoj = mnoj * 2
            count += 1
        else:
            n = n - 1
            count +=1
        print(n)

    if n > 1 :
        return answer(count,n)
    else:
        return count
n = int(input())


count = 0


print(answer(count,n))