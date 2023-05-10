class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.cnt = 0
        self.target = None  # Usato in ricerca

    def insert(self, val):
        z = Node(val)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z

    def print_tree(self):
        self.print_tree_rec(self.root)

    def print_tree_rec(self, node):
        if node is not None:
            self.print_tree_rec(node.left)
            print(node.val)
            self.print_tree_rec(node.right)

    def get_kesimo(self, node, k):
        self.cnt = k
        self.target = None
        self.get_kesimo_it(node)
        if self.target is None:
            return None
        return self.target.val

    def get_kesimo_it(self, node):
        if node is not None:
            self.get_kesimo_it(node.left)
            self.cnt = self.cnt - 1
            if self.cnt == 0:
                self.target = node
                return
            self.get_kesimo_it(node.right)

    def root(self):
        return self.root
