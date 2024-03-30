from collections import namedtuple # sravnenie
import bisect
from operator import attrgetter
from matplotlib import pyplot as plt
import random
import redblacktree

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
def start(n):
    for i in range(n):
        x1,y1,x2,y2 = map(int,[random.randint(-10000,10000),random.randint(-10000,10000),random.randint(-10000,10000),random.randint(-10000,10000)])
        events.append(event(min(x1,x2),-1,i))
        events.append(event(max(x1,x2),1,i))
        segments.append(seg(point(x1,y1),point(x2,y2),i))

lude = True
while(lude):
    start(100)


# #считываем значения
# n = int(input())
# for i in range(n):
#     x1,y1,x2,y2 = map(int,input().split())
#     events.append(event(min(x1,x2),-1,i))
#     events.append(event(max(x1,x2),1,i))
#     segments.append(seg(point(x1,y1),point(x2,y2),i))
# events.sort()
# # конец считывания значений


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
                    return new_srt, where[nxt]
                if prev != -1 and intersect(new_srt.seg, where[prev].seg):
                    return new_srt, where[prev]
                bisect.insort_left(where,new_srt,key = attrgetter('y'))
        else:
            nxt = bisect.bisect_left(where,new_srt.y,key=attrgetter('y'))
            prev = nxt - 1
            nxt = nxt + 1
            if prev != -1 and nxt < len(where) and intersect(where[nxt].seg, where[prev].seg):
                return where[nxt],where[prev]
            where.pop(nxt - 1)
    return 0,0


t = redblacktree.RedBlackTree()
def solve3(segments):
    for i in range(len(events)):
        id = events[i].id
        key = segments[id].start.y
        element = segments[id]

        if events[i].type == -1:
            # add in tree
            t.insert(key)
            t[key] = element

            #checking existense of lower and upper values in tree
            try:
                upper = t.predecessor(t.search(key)).value
            except Exception:
                upper = None
            try:
                lower = t.successor(t.search(key)).value
            except Exception:
                lower = None
            #end of checking
            
            #search intersct
            if lower and intersect(lower,element):
                return element, lower
            if upper and intersect(upper,element):
                return element, upper 
            #end serach

            #tracking
            # print(t[key],key)
            # print(lower,upper,element)
            # #end tracking

        else:

            #checking existense of lower and upper values in tree
            try:
                upper = t.predecessor(t.search(key)).value
            except Exception:
                upper = None

            try:
                lower = t.successor(t.search(key)).value
            except Exception:
                lower = None
            #end of checking

            if lower and upper and intersect(lower,upper) and lower != upper:
                return lower, upper
            t.delete(key)

        #tracking
        # print('start Tree')
        # t.print_tree()
        # print('end Tree')
        #end tracking
    return 0, 0








#!!!!!!
# #libraries
# from collections import namedtuple
# from bisect import bisect_left
# #const
# EPS = 1E-9
# #classes
# point = namedtuple('point',['x','y'])
# event = namedtuple('event',['x','type','id'])
# seg = namedtuple('seg',['start','end','id'])
# # class seg:
# #     def __init__(self, start, end, id):
# #         self.start = start
# #         self.end = end
# #         self.id = id
# #Tree
# class Node: #вершины
#     def __init__(self,data):
#         self.data = data
#         self.left = self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def __find(self, node,parent,value):
#         if node is None :
#             return None, parent, False
        
#         if value.start.y == node.data.start.y:
#             return node, parent, True
        
#         if value.start.y < node.data.start.y:
#             if node.left:
#                 return self.__find(node.left, node, value)
            
#         if value.start.y > node.data.start.y:
#             if node.right:
#                 return self.__find(node.right, node, value)
#         return node, parent, False
# #new  
#     def upper(self,node,search):
#         if node is None:
#             return None
#         answer = 1E9
#         ans = 0
#         v = [node]
#         while v:
#             vn = []
#             for x in v:
#                 if search.data.start.y >= x.data.start.y:
#                     answer = min(answer,x.data.start.y)
#                     ans = x
#                 if x.left:
#                     vn += [x.left]
#                 if x.right:
#                     vn += [x.right]
#             v = vn
#         if answer == 1E9:
#             return None
#         else:
#             return ans.data
    
#     def lower(self,node,search):
#         if node is None:
#             return None
#         answer = -1E9
#         ans = 0
#         v = [node]
#         while v:
#             vn = []
#             for x in v:
#                 if search.data.start.y <= x.data.start.y:
#                     answer = max(answer,x.data.start.y)
#                     ans = x
#                 if x.left:
#                     vn += [x.left]
#                 if x.right:
#                     vn += [x.right]
#             v = vn
#         if answer == -1E9:
#             return None
#         else:
#             return ans.data
# #end of new
#     def add(self, obj):
#         if self.root is None:
#             self.root = obj
#             return obj
    
#         s, p, fl_find = self.__find(self.root, None, obj.data)

#         if not fl_find and s:
#             if obj.data.start.y < s.data.start.y:
#                 s.left = obj
#             else:
#                 s.right = obj
#         return obj
    
#     def __del_leaf(self, s, p):
#         if p.left == s :
#             p.left = None
#         elif p.right == s:
#             p.right = None

#     def __del_one_child(self, s, p):
#         if p.left == s:
#             if s.left is None:
#                 p.left = s.right
#             elif s.right is None:
#                 p.left = s.left
#         elif p.right == s:
#             if s.left is None:
#                 p.right = s.right
#             elif s.right is None:
#                 p.right = s.left

#     def __find_min(self, node, parent):
#         if node.left:
#             return self.__find_min(node.left, node)
 
#         return node, parent
 
#     def del_node(self, obj):
#         s, p, fl_find = self.__find(self.root, None, obj.data)
 
#         if not fl_find:
#             return None
#         #new
#         if p is None:
#             s = None
#             return
#         #new
#         if s.left is None and s.right is None:
#             self.__del_leaf(s, p)
#         elif s.left is None or s.right is None:
#             self.__del_one_child(s, p)
#         else:
#             sr, pr = self.__find_min(s.right, s)
#             s.data = sr.data
#             self.__del_one_child(sr, pr)

#     def show_tree(self, node):
#         if node is None:
#             return
#         self.show_tree(node.left)
#         print(node.data)
#         self.show_tree(node.right)

# # end Tree

# #intersect 
# def vec(a,b,c):
#     s = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
#     if abs(s) < EPS:
#         return 0
#     elif s > 0:
#         return 1
#     else:
#         return -1

# def intersected (a,b,c,d):
#     if (a > b):
#         a, b = b, a
#     if (c > d):
#         c, d = d, c
#     return max(a,c) <= min(b,d) + EPS

# def intersect(a, b):
#     return intersected(a.start.x, a.end.x, b.start.x, b.end.x) \
#         and intersected(a.start.y, a.end.y, b.start.y, b.end.y) \
#         and vec(a.start, a.end, b.start) * vec(a.start, a.end, b.end) <= 0 \
#         and vec(b.start, b.end, a.start) * vec(b.start, b.end, a.end) <= 0
   
# #end intersect

# #объявление переменных
# t = Tree()
# #считываем значения
# # конец считывания значений
# # for x in segments:
# #     t.add(Node(x))
# # print(t.upper(t.root,Node(seg(point(1,100),point(1,1),0))))
# # print(*events,sep = '\n')
# def solve1(segments):
#     for i in range(len(events)):
#         id = events[i].id
#         # print('start', segments[id])
#         if events[i].type == -1:
#             # if t.lower(t.root,Node(segments[id])):
#                 # print(t.lower(t.root,Node(segments[id])),'1-lower')
#             # if t.upper(t.root,Node(segments[id])):
#                 # print(t.upper(t.root,Node(segments[id])),'1-upper')
#             if t.lower(t.root,Node(segments[id])) and intersect(t.lower(t.root,Node(segments[id])),segments[id]):
#                 return segments[id],t.lower(t.root,Node(segments[id]))
#             if t.upper(t.root,Node(segments[id])) and intersect(t.upper(t.root,Node(segments[id])),segments[id]):
#                 return segments[id],t.upper(t.root,Node(segments[id]))
#             t.add(Node(segments[id]))
#         else:
#             # if t.lower(t.root,Node(segments[id])):
#             #     print(t.lower(t.root,Node(segments[id])),'7-lower')
#             # if t.upper(t.root,Node(segments[id])):
#             #     print(t.upper(t.root,Node(segments[id])),'7-upper')

#             if t.lower(t.root,Node(segments[id])):
#                 if t.upper(t.root,Node(segments[id])):
#                     if intersect(t.lower(t.root,Node(segments[id])),t.upper(t.root,Node(segments[id]))) and t.lower(t.root,Node(segments[id])) != t.upper(t.root,Node(segments[id])) :
#                         return t.lower(t.root,Node(segments[id])),t.upper(t.root,Node(segments[id]))
#             t.del_node(Node(segments[id]))
#         # print('tree')
#         # t.show_tree(t.root)
#         # print('end')
#     return 0,0

# #!!!!!!!!!!!!!!!!!!!!!


a,b = solve3(segments)
if a == 0:
    print('NO')
else:
    print('YES')
    print(min(a.id,b.id)+1,max(a.id,b.id)+1)
    print(a.start,a.end,a.id)
    print(b.start,b.end,b.id)
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.plot([a.start.x,a.end.x],[a.start.y,a.end.y],color = 'blue')
    ax.plot([b.start.x,b.end.x],[b.start.y,b.end.y],color = 'blue')

    fig.show()
print(*events,sep='\n')
print(*segments,sep='\n')

c,d = solve(segments)
if c == 0:
    print('NO')
else:
    print('YES')
    print(min(c.seg.id,d.seg.id)+1,max(c.seg.id,d.seg.id)+1)
    print(c.seg.start,c.seg.end,c.seg.id)
    print(d.seg.start,d.seg.end,d.seg.id)
    ac = fig.add_subplot(212)
    ac.plot([c.seg.start.x,c.seg.end.x],[c.seg.start.y,c.seg.end.y],color = 'red')
    ac.plot([d.seg.start.x,d.seg.end.x],[d.seg.start.y,d.seg.end.y],color = 'red')
    ac.grid()
    ax.plot([c.seg.start.x,c.seg.end.x],[c.seg.start.y,c.seg.end.y],color = 'red')
    ax.plot([d.seg.start.x,d.seg.end.x],[d.seg.start.y,d.seg.end.y],color = 'red')
    ax.grid()
    plt.show()
    print(events)
