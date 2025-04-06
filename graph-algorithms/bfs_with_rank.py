# node class havs additional variable that represents size of its left subtree
# aplication of basic functions for operating on BST

class Node:

    def __init__(self, val, left_size=0, parent=None, left=None, right=None):

        self.val = val
        self.left_size = left_size
        self.parent = parent
        self.left = left
        self.right = right


def insert(root, x):  # normal insert but at the end add +1 to every parent.left_size if new node is in his left subtree

    if root == None:
        return Node(val=x)

    p = root
    prev = root
    path = []  # stores parents that have new_node in its left subtree

    while True:

        if p == None:  # reached destined place for new node

            new_node = Node(val=x, parent=prev)
            if x < prev.val:
                prev.left = new_node

            else:
                prev.right = new_node

            for node in path:
                node.left_size += 1

            return root

        prev = p

        if x < p.val:
            path.append(p)
            p = p.left

        else:
            p = p.right

    return


def find(root, n):  # returns (n+1)th smallest node in BST

    p = root

    while True:

        if p.left_size == n:
            return p

        elif p.left_size > n:
            p = p.left

        else:  # p.left_size < n
            n -= (p.left_size+1)
            p = p.right

    return


def ord_in_BST(root, node):  # returns number of nodes with values lesser whan x.val

    if node == None:
        return 0

    p = node
    cnt = node.left_size

    while True:

        if p.parent == None:
            return cnt

        elif p == p.parent.right:
            cnt += (p.parent.left_size+1)

        p = p.parent

    return
