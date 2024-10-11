# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        reversed_list = dummy

        array = []
        while head:
            heapq.heappush(array, head.val)  
            head = head.next

     
        current = dummy
        while array:
            new_node = ListNode(heapq.heappop(array))  # Create a new node with the smallest value
            current.next = new_node
            current = current.next

        return dummy.next