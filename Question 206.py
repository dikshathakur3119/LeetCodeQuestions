#206. Reverse Linked List 
#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currnode = head
        prevnode = None
        
        while currnode is not None:
            temp = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = temp
            
        
        return prevnode
        
        
        
      
            
            
            
        