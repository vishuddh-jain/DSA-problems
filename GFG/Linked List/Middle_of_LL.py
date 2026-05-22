
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
