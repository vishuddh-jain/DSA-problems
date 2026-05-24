'''
Given a singly linked list, the task is to remove every kth node of the linked list. Assume that k is always less than or equal to the length of the Linked List.

Examples : 

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
Output: 1 -> 3 -> 5 
Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
'''


class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


def deleteK(head, k):
    i = 1
    temp = head
    prev = None
        
    if head is None:
        return None
            
    while temp is not None:
        if i == k:
            prev.next = temp.next
            i = 1
            temp = temp.next
        else:
            prev = temp
            temp = temp.next
            i+=1
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print(deleteK(head, k=2))
# print(deleteK(head=123456, k=2)) It will throw error if you include this line as the input head can't be an integer,
# for that you can use input function to take input as linked list
