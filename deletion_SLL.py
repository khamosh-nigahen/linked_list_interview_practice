# Deletion in Single Linked List
# delete the node for given key

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class singleLinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node
            new_node.nextNode = None
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def printLinkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.nextNode

    def deleteNodeGivenkey(self, key):
        temp = self.head
        while(temp.data != key):
            curr = temp
            temp = temp.nextNode
        curr.nextNode = temp.nextNode
        temp = None

    def deleteNodeAtGivenPos(self, pos):
        temp = self.head
        for i in range(pos-1):
            curr= temp
            temp = temp.nextNode
        curr.nextNode = temp.nextNode
        temp = None


if __name__ == "__main__":
    sllist = singleLinkedList()
    # creating 3 nodes of the linked list
    sllist.push(1)
    sllist.push(2)
    sllist.push(3)
    sllist.push(4)

    # DELETE AT GIVEN KEY
    sllist.deleteNodeGivenkey(2)

    # delete a linked list at a given position
    sllist.deleteNodeAtGivenPos(3)
    #print the linked list
    sllist.printLinkedlist()


