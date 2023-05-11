class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Lista linkata ordinata in senso crescente
class OrderedLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

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

    def order_statistic(self, k):
        curr_node = self.head
        # cerco il nodo in posizione k
        for i in range(0, k-1):
            curr_node = curr_node.next
        return curr_node.value

    # Metodo per stampare la lista
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
