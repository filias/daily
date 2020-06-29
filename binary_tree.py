from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return f"{self.value} -> left: {self.left}, right: {self.right}"

    def is_leaf(self):
        return self.left is None and self.right is None


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def minimum_path_sum(self, root) -> int:
        """Returns the minimum path sum from root to a leaf.
        For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
          10
         /  \
        5    5
         |   |
          2   1
             /
            -1
        """

        def minimum_path_sum_aux(root, path=None):
            path.append(root.value)
            new_path = path[:]

            # Stop condition
            if root.is_leaf():
                return
            else:
                if root.left is not None:
                    minimum_path_sum_aux(root.left, path=path)
                elif root.right is not None:
                    minimum_path_sum_aux(root.right, path=path)

                if root.right is not None and root.left is not None:
                    paths.append(new_path)
                    minimum_path_sum_aux(root.right, path=new_path)

        paths = [[]]

        minimum_path_sum_aux(root, path=paths[0])
        return min([sum(path) for path in paths])


root = Node(
    10, left=Node(5, right=Node(2)), right=Node(5, right=Node(1, left=Node(-1)))
)
tree = BinaryTree(root)
assert tree.minimum_path_sum(tree.root) == 15
root = Node(10, left=Node(3), right=Node(2))
tree = BinaryTree(root)
assert tree.minimum_path_sum(tree.root) == 12


"""
Given the root to a binary tree, implement serialize(root), which serializes the tree 
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


def serialize(node):
    if node.left is None and node.right is None:
        return "{}".format(node.value)

    if node.left is not None and node.right is not None:
        return "{}({},{})".format(
            node.value, serialize(node.left), serialize(node.right)
        )
    if node.left is not None and node.right is None:
        return "{}({},)".format(node.value, serialize(node.left))
    if node.left is None and node.right is not None:
        return "{}(,{})".format(node.value, serialize(node.right))


def deserialize(str):
    try:
        new_str = str.split("(", 1)
        value = new_str[0]
        new_str = new_str[1][:-1].rsplit(",", 1)
        left = new_str[0]
        right = new_str[1]
        return Node(value, deserialize(left), deserialize(right))
    except IndexError:
        return Node(value)


node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.value == "left.left"
