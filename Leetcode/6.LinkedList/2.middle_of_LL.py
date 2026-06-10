'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def middleNode(head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
        return slow
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(middleNode(head))