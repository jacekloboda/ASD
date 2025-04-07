# returns node with minimal value greater than x.val in bts, x is node in bts

class node:

    def __init__(self, val):

        self.val = val
        self.parent = None
        self.left = None
        self.right = None


def next(x):

    if x.right != None:

        x = x.right

        while x.left != None:

            x = x.left

        return x

    else:  # x.right == None

        while x.parent != None and x.parent.val < x.val:

            x = x.parent

        return x.parent  # x.parent.val > x.val or we are in root and return None because there is no val greater
