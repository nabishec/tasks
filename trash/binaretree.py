#Tree
class Node: #вершины
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node,parent,value):
        if node is None :
            return None, parent, False
        
        if value.start.y == node.data.start.y:
            return node, parent, True
        
        if value.start.y < node.data.start.y:
            if node.left:
                return self.__find(node.left, node, value)
            
        if value.start.y > node.data.start.y:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False
#new  
    def upper(self,node,search):
        if node is None:
            return None
        answer = 1E9
        ans = 0
        v = [node]
        while v:
            vn = []
            for x in v:
                if search.data.start.y >= x.data.start.y:
                    answer = min(answer,x.data.start.y)
                    ans = x
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
        if answer == 1E9:
            return None
        else:
            return ans.data
    
    def lower(self,node,search):
        if node is None:
            return None
        answer = -1E9
        ans = 0
        v = [node]
        while v:
            vn = []
            for x in v:
                if search.data.start.y <= x.data.start.y:
                    answer = max(answer,x.data.start.y)
                    ans = x
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
        if answer == -1E9:
            return None
        else:
            return ans.data
#end of new
    def add(self, obj):
        if self.root is None:
            self.root = obj
            return obj
    
        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data.start.y < s.data.start.y:
                s.left = obj
            else:
                s.right = obj
        return obj
    
    def __del_leaf(self, s, p):
        if p.left == s :
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
 
        return node, parent
 
    def del_node(self, obj):
        s, p, fl_find = self.__find(self.root, None, obj.data)
 
        if not fl_find:
            return None
        #new
        if p is None:
            s = None
            return
        #new
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

# end Tree