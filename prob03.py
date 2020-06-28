"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

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


class Node:
    val = ""
    left = None
    right = None

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node.left is None and node.right is None:
        return "{}".format(node.val)

    if node.left is not None and node.right is not None:
        return "{}({},{})".format(node.val, serialize(node.left), serialize(node.right))
    if node.left is not None and node.right is None:
        return "{}({},)".format(node.val, serialize(node.left))
    if node.left is None and node.right is not None:
        return "{}(,{})".format(node.val, serialize(node.right))


def deserialize(str):
    try:
        new_str = str.split("(", 1)
        val = new_str[0]
        new_str = new_str[1][:-1].rsplit(",", 1)
        left = new_str[0]
        right = new_str[1]
        print(val, left, right)
        return Node(val, deserialize(left), deserialize(right))
    except IndexError:
        return Node(val)


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    assert deserialize(serialize(node)).left.left.val == "left.left"
    # return 'root(left(left.left,None),right)'
