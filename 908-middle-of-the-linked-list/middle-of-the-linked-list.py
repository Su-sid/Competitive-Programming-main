# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast= head, head 

        # while fast and fast.next:
        #     fast=fast.next.next
        #     slow=slow.next
        # return slow
             
        counter= 0

        while fast:
            counter+=1
            fast=fast.next

        print(counter)

        for _ in range(counter//2):
            slow=slow.next
        return slow