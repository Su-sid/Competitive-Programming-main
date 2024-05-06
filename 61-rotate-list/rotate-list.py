# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         length=0
#         curr, present= head,head
#         empty= ListNode(0)

#         while curr:
#             length+=1
#             curr= curr.next

#         # print(length)
#         for _ in range(length-k):
#             present=present.next
#         present.next=None
#         print(present)
#         print(curr)


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = head
        
        k %= length
        
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head        