#!/bin/python3

def removeDuplicates(head):
    node = head
    if(head is None):
        return None
    
    else:
        while(head.next != None):
            if(head.data == head.next.data):
                head.next = head.next.next
                
            else:
                head = head.next
                
    return node