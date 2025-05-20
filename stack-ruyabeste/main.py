# Implementation of stack using Python lists
from import_nodes import *

# Stack initialization
stack = []

nodes = import_csv("coordinates.csv")

# Add the nodes to the stack using Python lists
for i in range(len(nodes)):
    stack.append(nodes[i])

# Pop the nodes from the stack using Python lists
for i in range(len(nodes)):
    node = stack.pop()
    print("Removed Node")
    print("ID: {}, Name: {}".format(node.id, node.name))




