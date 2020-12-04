#!/bin/python3

def printLinkedList(head):
    node = head
    while(node is not None):
        print(node.data)
        node = node.next