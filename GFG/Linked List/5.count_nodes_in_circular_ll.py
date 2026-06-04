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

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head
print(countNodes(head))