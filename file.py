# Linked Lists
# Singly Lists

# Declare class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Declare linkedlist class
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
        
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            
    def printList(self):
        currentNode = self.head
        print(currentNode)
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
            
linkedList = LinkedList()
firstNode = Node('John')
secondNode = Node('Ben')
thirdNode = Node('Matthew')
fourthNode = Node('Peter')
linkedList.insert(firstNode)        
linkedList.insert(secondNode)        
linkedList.insert(thirdNode)  
linkedList.insertHead(fourthNode)

linkedList.printList()      