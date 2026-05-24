class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def ifCircular(head):
    if head is None:
        return True
    
    temp = head.next
    
    while temp.next is not None and temp != head:
        temp = temp.next
        
    return temp == head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head

print(ifCircular(head))