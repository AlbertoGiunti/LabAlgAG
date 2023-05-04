# Albero rosso nero

class ARNNodo:
    def __init__(self, key, parent, color):
        self.key = key
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None


class ARN:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = ARNNodo(value, None, "BLACK")
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.key:
            if node.left is None:
                node.left = ARNNodo(value, node, "RED")
                self._balance(node.left)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = ARNNodo(value, node, "RED")
                self._balance(node.right)
            else:
                self._insert(value, node.right)

    def _balance(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._leftRotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._rightRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rightRotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._leftRotate(node.parent.parent)
        self.root.color = "BLACK"

    def _leftRotate(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left is not None:
            temp.left.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def _rightRotate(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right is not None:
            temp.right.parent = node
        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return False
        elif node.key == value:
            return True
        elif value < node.key:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def print(self):
        if self.root is not None:
            self._print(self.root)

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(node.key)
            self._print(node.right)



