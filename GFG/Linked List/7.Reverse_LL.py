'''
Reverse a Linked List
Given the head of a linked list, 
reverse the list and return the new head.

Example:
Input: 1->2->3->4->5

Output: 5->4->3->2->1
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def reverse_ll_iteratively(head):
    if head is None or head.next is None:
        return head
    
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(reverse_ll_iteratively)