'''
Given a singly linked list, 
the task is to convert it into a circular linked list.
Example:

Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

Output: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 1

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None        
    
def singly_to_circular(head):
    if head is None:
        return None
    
    temp = head
    
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(singly_to_circular(head))