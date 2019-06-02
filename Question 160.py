'''
LeetCode Q.160:
Write a program to find the node at which the intersection of two singly linked lists begins.
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLen(givenList):
            l = 0
            while givenList is not None:
                l += 1
                givenList = givenList.next
            return l
        
        
        def makeLenEqual(list1, list2):
            len1 = getLen(list1)
            len2 = getLen(list2)
            
            if len1>len2:
                longList, shortList = list1, list2
                longLen, shortLen = len1, len2
            else:
                longList, shortList = list2, list1
                longLen, shortLen = len2, len1
            
            
            while longLen > shortLen:
                longList = longList.next
                longLen = longLen - 1

            return longList, shortList
        
        
        intersectNode = None
        
        listA , listB = makeLenEqual(headA, headB)
        
        while listA is not None and listB is not None:
            if listA == listB:
                if intersectNode == None:
                    intersectNode = listA
            else:
                intersectNode = None
            listA = listA.next
            listB = listB.next
        
        
        return intersectNode
        
            
                
                