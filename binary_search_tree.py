class BSTNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        z = BSTNode(val)
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

    # Metodo che restituisce il k-esimo nodo più piccolo dell'albero
    def get_kesimo(self, node, k):
        stack = []
        current = node
        count = 0

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                break

        return None

    # Metodo che restituisce la posizione di un nodo nell'albero binario di ricerca con un attraversamento in ordine
    def get_rank(self, node):
        r = self.tree_size(node.left) + 1
        y = node
        while y != self.root:
            if y == y.parent.right:
                r = r + self.tree_size(y.parent.left) + 1
            y = y.parent
        return r

    # Metodo che restituisce la dimensione dell'albero versione iterativa
    def tree_size(self, node):
        if node is None:
            return 0

        size = 0
        stack = []
        current = node

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                size += 1
                current = current.right
            else:
                break

        return size

    '''
        # Metodo che restituisce la dimensione dell'albero ricorsivamente
        def tree_size(self, node):
            if node is None:
                return 0
            else:
                return self.tree_size(node.left) + 1 + self.tree_size(node.right)
        '''

    def root(self):
        return self.root

    # Ricerca di un nodo nell'albero binario di ricerca
    def search(self, node, val):
        while node is not None and val != node.val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return node
