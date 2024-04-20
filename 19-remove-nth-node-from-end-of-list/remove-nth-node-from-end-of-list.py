# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr= head
        count= 0
        while curr:
            curr= curr.next
            count+=1
        count =count-n

        # print(count)
        dummy= ListNode(0, head)
        curr=dummy
        
        for _ in range(count):
            curr=curr.next

        curr.next= curr.next.next
        return dummy.next 