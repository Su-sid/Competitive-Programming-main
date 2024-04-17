class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head: # if self.size == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index and index < self.size:
            node = Node(val)
            count = 0
            current = self.head
            index = index - 1
            while count < index:
                current = current.next
                count = count + 1
            node.next = current.next
            current.next = node
            self.size = self.size + 1
        else: #if out of bound : index < 0 and index > self.size
            return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
