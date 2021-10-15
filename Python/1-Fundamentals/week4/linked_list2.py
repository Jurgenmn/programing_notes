class Node:  # Linked list
    def __init__(self, value):
        self.value = value
        self.next = None


def iter_linked_list(node):
    while node != None:
        print(node.value)
        node = node.next


head = Node("1st Node")  # Node object
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

iter_linked_list(head)
