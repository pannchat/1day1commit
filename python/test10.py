class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, comp=None):
        if comp is None:
            self.comp = lambda a, b: a-b
        else:
            self.comp = comp
        self.root = None

    def add(self, data):
        if self.root == None:
            self.root = Node(data)
            self.current = self.root

        else:
            while True:
                if data < self.current.data:
                    if data < self.left != None:
                        self.current = self.current.left
                    else:
                        self.current.left = Node(data)
                        break
                else:
                    if self.current.right != None:
                        self.current - self.current.right
                    else:
                        self.current.right = Node(data)
                        break
                    
    def search(self,data):
        pass

bst = BinarySearchTree(comp = lambda a, b :hash(a) - hash(b) )
for c in 'qwyhwef':
    bst.add(c)

for c in 'qwyhwefjdhfdve':
    print( 1 if bst.search(c) else 0, end='')