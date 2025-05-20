class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LinkedListNode(Node):
    def __init__(self, node: Node):
        super().__init__(node.id, node.name)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_items = 0

    def add_node(self, node: Node, index: int):
        new_node = LinkedListNode(node)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    return
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.num_items += 1

    def remove_node(self, index: int):
        if self.head is None:
            return None
        if index == 0:
            removed = self.head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None or current.next is None:
                    return None
                current = current.next
            removed = current.next
            current.next = current.next.next if current.next else None
        self.num_items -= 1
        return removed

class Stack:
    def __init__(self):
        self.top = LinkedList()

    def push(self, node):
        self.top.add_node(node, 0)

    def pop(self):
        return self.top.remove_node(0)

    def peek(self):
        return self.top.head

