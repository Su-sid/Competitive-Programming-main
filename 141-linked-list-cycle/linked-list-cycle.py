# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast= head, head


        while fast and fast.next:
            slow= slow.next
            fast=  fast.next.next

            if fast==slow:
                # print(fast)
                return True
        return False

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         hashmap = set()
#         while head:
#             if head in hashmap:
#                 return True
#             hashmap.add(head)
#             head = head.next
#         return False
