# Albero rosso nero
class Color:
    RED = 'RED'
    BLACK = 'BLACK'


class Node:
    def __init__(self, val, s=1, col=None):
        self.val = val  # the value of the node
        self.size = s  # the size of the subtree rooted at this node
        self.left = None  # the left child of the node
        self.right = None  # the right child of the node
        self.parent = None  # the parent of the node
        self.color = col  # the color of the node


class RedBlackTree:
    def __init__(self):
        nil = Node(None, 0, col=Color.BLACK)
        self.root = nil
        self.nil = nil

    def os_select(self, x, i):
        """
        Select the i-th order statistic in the tree.
        :param x: node to start the search from
        :param i: the i-th order statistic to select
        :return: the node containing the i-th order statistic, or None if not found
        """
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i - r)

    def insert(self, val):
        """
        Insert a new node into the tree.
        """
        z = Node(val)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Color.RED
        self.insert_fix_up(z)

    def insert_fix_up(self, z):
        """
        Fix up the tree after inserting a new node.
        :param z: the node that was just inserted
        """
        while z.parent.color == Color.RED and z.parent != self.nil:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = Color.BLACK

    def left_rotate(self, x):
        """
        Perform a left rotation around the given node.
        :param x: the node to rotate around
        """
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, x):
        """
        Perform a right rotation around the given node.
        :param x: the node to rotate around
        """
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def root(self):
        return self.root
