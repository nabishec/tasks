# lists
from collections import namedtuple
import bisect 
from operator import attrgetter
import random

EPS = 1E-9

point = namedtuple('point',['x','y'])
event = namedtuple('event',['x','type','id'])
seg = namedtuple('seg',['start','end','id'])
srt = namedtuple('srt',['seg','y'])

#intersect with abc

def vec(a,b,c):
    s = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if abs(s) < EPS:
        return 0
    elif s > 0:
        return 1
    else:
        return -1

def intersected (a,b,c,d):
    if (a > b):
        a, b = b, a
    if (c > d):
        c, d = d, c
    return max(a,c) <= min(b,d) + EPS

def intersect(a, b):
    return intersected(a.start.x, a.end.x, b.start.x, b.end.x) \
        and intersected(a.start.y, a.end.y, b.start.y, b.end.y) \
        and vec(a.start, a.end, b.start) * vec(a.start, a.end, b.end) <= 0 \
        and vec(b.start, b.end, a.start) * vec(b.start, b.end, a.end) <= 0
 
    
#end intersect

segments = []
events = []
#считываем значения
n = int(input())
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    events.append(event(min(x1,x2),-1,i))
    events.append(event(max(x1,x2),1,i))
    segments.append(seg(point(x1,y1),point(x2,y2),i))
events.sort()
# конец считывания значений
where = []
#new
def solve(segments):
    for i in range(len(events)):
        id = events[i].id
        new_srt = srt(segments[id],segments[id].start.y)
        if events[i].type == -1:
            if len(where) == 0:
                where.append(new_srt)
            else:
                nxt = bisect.bisect_left(where,new_srt.y,key = attrgetter('y'))
                prev = nxt - 1
                if nxt != len(where) and intersect(new_srt.seg, where[nxt].seg):
                    return new_srt.seg.id, where[nxt].seg.id
                if prev != -1 and intersect(new_srt.seg, where[prev].seg):
                    return new_srt.seg.id, where[prev].seg.id
                bisect.insort_left(where,new_srt,key = attrgetter('y'))
        else:
            nxt = bisect.bisect_left(where,new_srt.y,key=attrgetter('y'))
            prev = nxt - 1
            nxt = nxt + 1
            if prev != -1 and nxt < len(where) and intersect(where[nxt].seg, where[prev].seg):
                return where[nxt].seg.id,where[prev].seg.id
            # print('START')
            # print(where)
            # print('END')
            # print(len(where), '-LEN')
            # print(new_srt,'-ELEMENT')
            # print(bisect.bisect_left(where,new_srt.y,key=attrgetter('y')),'-BISECT')
            # print(nxt,'-NEXT')
            where.pop(nxt - 1)
    return 0,0

a,b = solve(segments)
if a == 0:
    print('NO')
else:
    print('YES')
    print(min(a,b)+1,max(a,b)+1)
