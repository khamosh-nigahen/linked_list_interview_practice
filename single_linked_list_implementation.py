# Implementation of Single Linked List

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class singleLinkedList(object):

    def __init__(self):
        self.head = None

    def printLinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.nextNode

if __name__ == "__main__":
    sllist = singleLinkedList()
    first = Node(1)
    second  = Node(2)
    third = Node(3)
    sllist.head = first
    first.nextNode = second
    second.nextNode = third
    sllist.printLinkedlist()


