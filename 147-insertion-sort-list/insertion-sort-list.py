# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy= ListNode(0, next=head)
        curr= head.next
        prev=head

        while curr:
            if curr.val >= prev.val:
                prev=curr
                curr= curr.next
                continue
            temp= dummy
            while temp.next.val < curr.val:
                temp= temp.next
            prev.next=curr.next
            curr.next= temp.next
            temp.next= curr
            curr=prev.next
        return dummy.next
