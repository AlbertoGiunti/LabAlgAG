class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class OrderedLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None and value > curr_node.next.value:
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node

            if new_node.next is None:
                self.tail = new_node

    def order_statistic(self, k):
        curr_node = self.head
        i = 1
        while curr_node is not None and i < k:
            curr_node = curr_node.next
            i += 1

        if curr_node is not None:
            return curr_node.value
        else:
            return None
