# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        reversedList = dummy
        array= deque()
        reversedList=dummy

        while head:
            array.appendleft(head.val)
            head= head.next
        
        # print(array)
        # print(reversedList)
        
        for num in array:
            node = ListNode(num)
            reversedList.next= node
            reversedList=node

        return dummy.next

            





            
        