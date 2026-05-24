'''
Given a singly linked list and a key, the task is to count the number of occurrences of the given key in the linked list.

Example :

Input : head: 1->2->1->2->1->3->1 , key = 1
Output : 4
Explanation: key equals 1 has 4 occurrences.

Input : head: 1->2->1->2->1, key = 3
Output : 0
Explanation: key equals to 3 has 0 occurrences.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def count(head, key):
        temp = head
        count = 0
        while temp is not None:
            if temp.data == key:
                count +=1
                temp = temp.next
            else:
                temp = temp.next
        return count

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print(count(head, 2))
# Time complexity 0.3 ms