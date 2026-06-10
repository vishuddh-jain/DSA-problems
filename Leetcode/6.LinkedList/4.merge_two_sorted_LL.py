'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def mergeTwoLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalhead = None
    finaltail = None
    
    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            if finalhead is None:
                finalhead = head1
                finaltail = head1
            else:
                finaltail.next = head1
                finaltail = head1
            head1 = head1.next
                
        elif head1.data >= head2.data:
            if finalhead is None:
                finalhead = head2
                finaltail = head2
            else:
                finaltail.next = head2
                finaltail = head2
            head2 = head2.next
        
    if head1 is not None:
        finaltail.next = head1
        
    if head2 is not None:
        finaltail.next = head2
    
    return finalhead
        
head1 = Node(1)
head1.next = Node(5)
head1.next.next = Node(7)
head2 = Node(4)
head2.next = Node(6)
head2.next.next = Node(8)
head2.next.next.next = Node(10)

print(mergeTwoLists(head1,head2))