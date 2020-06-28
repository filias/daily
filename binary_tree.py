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
            print(f"Path: {path} | Root: {root}")
            path.append(root.value)
            new_path = path[:]

            # Stop condition
            if root.is_leaf():
                print(f"Leaf: {root.value} | Path: {path}")
                return
            else:
                if root.left is not None:
                    print("Going left")
                    minimum_path_sum_aux(root.left, path=path)
                elif root.right is not None:
                    print("Going right")
                    minimum_path_sum_aux(root.right, path=path)

                if root.right is not None and root.left is not None:
                    print("Making a new path")
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
