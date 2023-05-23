class OLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Lista linkata ordinata in senso crescente
class OrderedLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = OLLNode(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None and new_node.value > curr_node.next.value:
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node

    # Metodo che restituisce il k-esimo nodo più piccolo dell'albero
    def order_statistic(self, x, k):
        curr_node = x
        # cerco il nodo in posizione k
        for i in range(0, k - 1):
            curr_node = curr_node.next
        return curr_node.value

    # Metodo che restituisce la posizione di un nodo nella lista con un attraversamento in ordine
    def oll_rank(self, x):
        curr_node = self.head
        r = 1
        while curr_node is not None:
            if curr_node.value == x:
                return r
            else:
                r += 1
                curr_node = curr_node.next
        return None

    # Metodo che restituisce un nodo con valore x se presente nella lista
    def search(self, start, x):
        curr_node = start
        while curr_node is not None:
            if curr_node.value == x:
                return curr_node
            else:
                curr_node = curr_node.next
        return None
