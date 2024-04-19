# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         count = 0
#         curr= head

#         #get the count of nodes of the linked list
#         while curr:
#             count+=1
#             curr = curr.next

#         n = count -(count % k) # n is 4 as ( 5 - 5 % 2)

#         #dummy node with head as next
#         dummy = ListNode(0,head)
#         reversable_linked_list= dummy

#         #get the new node we are to reverse
#         for _ in range(n):
#             reversable_linked_list= reversable_linked_list.next

#         remaining_nodes= reversable_linked_list.next
#         reversable_linked_list.next= None
#         #reverse loop function
#         curr= head
#         start_head= dummy

#         while curr:
#             prev= None
#             starter= curr
#             for i in range(k):
#                 temp= curr.next
#                 curr.next= prev
#                 prev=curr
#                 curr=temp
#             starter.next=curr
#             start_head.next= prev
#             start_head= starter
#         #join the remaining nodes to the reversed one.
#         start_head.next=remaining_nodes

#         return dummy.next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = prevEnd = ListNode(next=head)
        curr = currEnd = head
        prev = None
        cnt = 1
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
            if cnt%k==0:
                prevEnd.next,prevEnd,currEnd,prev = prev,currEnd,curr,None
            cnt += 1

        curr = prev
        prev = None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        prevEnd.next = prev

        return dummy.next        