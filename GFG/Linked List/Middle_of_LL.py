'''
Given the head of singly linked list, find middle node of the linked list.

If the number of nodes is odd, return the middle node.
If the number of nodes is even, there are two middle nodes, so return the second middle node.
Example:

input:
head -> 1 -> 2 -> 3 -> 4 -> 5 -> Null 
 
Output: 3 
Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.

Input:
head -> 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> Null 
 
Output: 40
Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def getMiddle(self, head):
        l = self.length_of_ll(head)
        middle = l//2
        temp = head
        count = 0
        
        while count < middle:
            temp = temp.next
            count+=1
        return temp.data
    
    def length_of_ll(self, head):
        temp = head
        i=0
        while temp != None:
            temp = temp.next
            i+=1
        return i

obj = Solution()
obj.getMiddle()
