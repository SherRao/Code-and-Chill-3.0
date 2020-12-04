#!/bin/python3

def check_binary_search_tree_(root):
    if root == None or (root.left == None and root.right == None):
        return True

    elif root.right == None:
        return root.left.data <= root.data and check_binary_search_tree_(root.left)

    elif root.left == None:
        return root.right.data >= root.data and check_binary_search_tree_(root.right)

    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)

