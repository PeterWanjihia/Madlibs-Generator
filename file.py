# Linked Lists
# Singly Lists

# Declare class
from tkinter import N


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Declare linkedlist class
class LinkedList:
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length+=1
            currentNode = currentNode.next
        return length       
            
    
    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head = newNode
        newNode.next = temporaryNode
        del temporaryNode

    
    def insertAt(self,newNode,position):
        if position < 0 or position >self.listLength():
            print('Invalid Position')
            return
        
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while  True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1 
            
                   
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
fifthNode = Node('Felix')
linkedList.insert(firstNode)        
linkedList.insert(secondNode)        
linkedList.insert(thirdNode)  
linkedList.insertHead(fourthNode)
linkedList.insertAt(fifthNode,1)

linkedList.printList()  
 