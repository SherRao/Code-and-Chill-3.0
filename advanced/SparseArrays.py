#!/bin/python3

def matchingStrings(strings, queries):
    n = len(queries)
    ar = []
    l = len(strings)
    for i in range(n):
        ar.append(0)
        for j in range(l):
            if( queries[i].lower() == strings[j].lower() ):
                ar[i] += 1
   
    return ar;