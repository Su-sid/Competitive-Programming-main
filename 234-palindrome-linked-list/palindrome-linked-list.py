#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         nums= []
#         while head:
#             nums.append(head.val)
#             head= head.next
#         if nums== nums[::-1]:
#             return True
#         else:
#             return False
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=slow= head
        while fast and fast.next:
            fast=fast.next.next
            slow= slow.next

        #reverse the second half

        prev =None
        while slow:
            tmp= slow.next
            slow.next=prev
            prev=slow
            slow=tmp

        #check palindrome
        left, right= head, prev
        while right:  # use prev pointer for the second half
            if left.val != right.val:
                return False 
            left = left.next 
            right = right.next
        return True


        