from ds import *

'''def bubble_sort( theSeq ):
    if(isinstance(theSeq, list)):
        n = len( theSeq )
        for i in range( n - 1 ):
            for j in range( n-(i+1) ):
                if (theSeq[j] > theSeq[j + 1]):
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
            #print(theSeq)
        return theSeq'''

from ds import *

def bubble_sort(theSeq):
    if isinstance(theSeq, list):
        n = len(theSeq)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if theSeq[j] > theSeq[j + 1]:
                    theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
        return theSeq

    elif isinstance(theSeq, LinkedList):
        for i in range(theSeq.num_items - 1):
            current = theSeq.head
            for j in range(theSeq.num_items - i - 1):
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
        return theSeq


