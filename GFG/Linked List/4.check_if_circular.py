'''
Given the head of a singly linked list, the task is to find if given linked list is circular or not. A linked list is called circular if its last node points back to its first node.

Note: The linked list does not contain any internal loops.

Example:

Input: LinkedList: 2->4->6->7->5
Output: true
Explanation: As shown in figure the first and last node is connected, i.e. 5 -> 2

Input: LinkedList: 2->4->6->7->5->1
Output: false
Explanation: As shown in figure this is not a circular linked list.
'''


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

def IfCircular(head):
    if head is None:
        return True

    temp = head
    while True:
        temp = temp.next
        if temp == head:
            return True
        else:
            continue
    return False
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head

print(ifCircular(head))
print(IfCircular(head))