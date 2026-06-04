'''
Given a circular linked list. The task is to find the length of the linked list, 
where length is defined as the number of nodes in the linked list.
'''
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
 
def countNodes(head):

    temp = head
    result = 0

    if (head == None) :
        return 0
    
    while True :
        temp = temp.next
        result = result + 1
        if (temp == head):
            break

    return result
