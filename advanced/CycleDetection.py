#!/bin/python3

def has_cycle(head):
    seenNodes = []
    
    cur = head
    while cur.next:
        cur = cur.next
        
        if cur in seenNodes:
            return 1
        else:
            seenNodes.append(cur)          
            
    return 0