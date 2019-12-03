"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

Leet 250: https://leetcode.com/articles/count-univalue-subtrees/
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

# METHOD 1 : Time complexity : O(n^2)
# Leet 965: https://leetcode.com/problems/univalued-binary-tree/


def is_unival(root):
    if root is None:
        return True
    if root.left is not None and root.left.value != root.value:
        return False
    if root.right is not None and root.right.value != root.value:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True

# Time Complexity of is_unival O(n)


def count_unival(root):
    if root is None:
        return 0

    count = count_unival(root.left) + count_unival(root.right)
    if is_unival(root):
        count += 1

    return count
# Time Complexity of count_unival O(n^2)


# METHOD 2
# Time complexity:  O(n)
def count_unival2(root):
    total_count, is_unival = helper(root)
    return total_count


def helper(root):
    if root is None:
        return 0, True
    left_count, left_is_unival = helper(root.left)
    right_count, right_is_unival = helper(root.right)

    is_unival = True

    if root.left is not None and root.left.value != root.value:
        is_unival = False

    if root.right is not None and root.right.value != root.value:
        is_unival = False

    if is_unival:
        return left_count + right_count + 1, True

    else:
        return left_count + right_count, False



# Test Tree
tree = Tree(0)
tree.get_root().set_left_child(Node(1))
tree.get_root().set_right_child(Node(0))
tree.get_root().get_right_child().set_left_child(Node(1))
tree.get_root().get_right_child().set_right_child(Node(0))
tree.get_root().get_right_child().get_left_child().set_left_child(Node(1))
tree.get_root().get_right_child().get_left_child().set_right_child(Node(1))

print(count_unival2(tree.get_root()), 'should be 5')

# explanation : https://www.youtube.com/watch?v=7HgsS8bRvjo&t=286s
