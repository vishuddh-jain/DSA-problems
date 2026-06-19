'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def length(head):
        count = 0
        if head is None:
            return 0
        while head :
            count +=1
            head = head.next
        return count

def removeNthFromEnd(head, n):
        l = length(head)

        dummy = ListNode(0)
        dummy.next = head

        temp = dummy
        for _ in range(l-n):
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next

