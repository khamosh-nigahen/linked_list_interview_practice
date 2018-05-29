# Three types of insertion in Single Linked List
# ->insert node at front
# ->insert Node after a given node
# ->insert Node at the tail

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

    def pushAtBegining(self, data):
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node

    def insertAfterNode(self, data, prev_node):
        new_node = Node(data)
        new_node.nextNode = prev_node.nextNode
        prev_node.nextNode = new_node

    def pushAttail(self, data):
        new_node = Node(4)
        third.nextNode = new_node
        new_node.nextNode = None


if __name__ == "__main__":
    sllist = singleLinkedList()
    # creating 3 nodes of the linked list
    first = Node(1)
    second  = Node(2)
    third = Node(3)
    third.nextNode = None
    sllist.head = first
    first.nextNode = second
    second.nextNode = third

    #inserting the node at head
    sllist.pushAtBegining(0)

    #insert after particular Node
    sllist.insertAfterNode(2.5, second)

    #insert after tail
    sllist.pushAttail(4)

    #print the linked list
    sllist.printLinkedlist()