# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy= ListNode()
        newList=dummy
        heap=[]
        for alist in lists:
            while alist:
                heappush(heap,alist.val)
                alist=alist.next
        # print(heap)

        for _ in range(len(heap)):
            node = ListNode(heappop(heap))
            newList.next= node
            newList=node
            # print(node)

        return dummy.next
