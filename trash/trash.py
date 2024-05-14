# # import math
# # second = 1
# # minuite = 60 * second
# # hour = 60 * minuite
# # day = 24 * hour
# # month = 30 * day
# # year = 365 * day
# # print(hour)
# # print(math.log2(1152921504606846976))
# # print(float(pow(2,3600)))
# # # def n(z):
# # #     return float(2 ** z)
# # # print('second =',float(n(second)))
# # # print(' minuite =', float(n(minuite)))
# # # print('hour =',float(n(hour)))
# # # print('day =',float(n(day)))
# # # print('month =',float(n(month)))
# # # print('year =',float(n(year)))
# result = pow(2, 50000)
# print(result)

# def n(a,b = [0]):
#     b.append(a)
#     print(b)
# print(n(1))



# from bisect import bisect_left as bis
# a = dict()
# a[1] = 89
# a

n = int(input())
array = [0] * n
sobitia = [0] * n 

for i in range(n):
    array[i],sobitia[i] = map(int,input().split())
    
    