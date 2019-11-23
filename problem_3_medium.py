"""This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

Leet 297: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""


class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_left_child(self):
        return self.left

    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right

    def set_right_child(self, node):
        self.right = node

    def has_left(self):
        return self.left != None

    def has_right(self):
        return self.right != None


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        return self.q.pop()

    def __len__(self):
        return len(self.q)


def serializer(root):
    l1 = []
    q = Queue()
    q.enq(root)
    while len(q) > 0:
        node = q.deq()
        if not node:
            l1.append(None)
            continue
        l1.append(str(node.value))
        q.enq(node.get_left_child())
        q.enq(node.get_right_child())

    return l1


def deserializer(data):
    q = Queue()
    tree3 = Tree(data[0])
    node = tree3.get_root()
    q.enq(node)
    i = 1
    while len(q) > 0:
        node = q.deq()
        if node.value:
            node.left = Node(data[i])
            node.right = Node(data[i + 1])
            q.enq(node.left)
            q.enq(node.right)
            i = i + 2

    return tree3


tree2 = Tree("A")
tree2.get_root().set_left_child(Node("B"))
tree2.get_root().set_right_child(Node("C"))
tree2.get_root().get_left_child().set_left_child(Node("D"))
tree2.get_root().get_left_child().set_right_child(Node("E"))
tree2.get_root().get_right_child().set_right_child(Node("G"))

data = serializer(tree2.get_root())
print(f"Serialized Tree: {data}")

tree4 = deserializer(data)
node = tree4.get_root()
print(f"Deserialized tree : {tree4}")
print(node.right.right.value)
print(node.right.left.value)


""" ANALYSIS

Time Complexity: O(n)
traversal complexity
and then going through each point in data


Space Complexity: O(n+n)
"""
