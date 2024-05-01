# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self):
        self.new_list = None

    def reverser(self, current):
        if current == None:
            return self.new_list

        if current != None:
            next_node = current.next
            current.next = self.new_list
            self.new_list = current
            current = next_node

        return self.reverseList(current)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        final = self.reverser(current)
        return final
        # while current:
        #     next_node= current.next
        #     current.next= new_list
        #     new_list=current
        #     current=next_node
        # return new_list
