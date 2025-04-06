# inserting new node with value x to BST

class Node:

    def __init__(self, val, parent=None, left=None, right=None):

        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


def insert_to_BST(root, x):  # root of BST, x is value you want to insert

    if root == None:  # if there is no graph make one
        return Node(x)

    p = root
    prev = root

    while p != None:

        prev = p

        if x < p.val:
            p = p.left

        else:  # x >= p.val
            p = p.right

    new_node = Node(val=x, parent=prev)

    if x < prev.val:
        prev.left = new_node

    else:  # x >= prev.val
        prev.right = new_node

    return root
