'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        if vals == vals[::-1]:
            return True
        return False
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
print(isPalindrome(head))