# Implementation of stack using Python lists
from import_nodes import *
from ds import *

# Stack initialization
stack = Stack()

nodes = import_csv("coordinates2.csv")

# TEST POPPING AN EMPTY STACK
node = stack.pop()

# PUSH ITEMS
for i in range(len(nodes)):
    stack.push(nodes[i])

# Print total number of items in the stack
print("Total number of items in the stack: ", stack.top.num_items)

# POP ITEMS
for i in range(stack.top.num_items):
    node = stack.pop()
    print("Popped: ", node.name)

# Print total number of items in the stack
print("Total number of items in the stack: ", stack.top.num_items)


