# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#using pointers 

        # dummy = ListNode()
        # dummy.next = head
        # prev = dummy
        # cur = head
        # while cur and cur.next:

        #     if cur.next.val == cur.val:
        #         while cur.next and cur.next.val == cur.val:
        #             cur = cur.next
        #         cur.next, cur = None, cur.next
        #         prev.next = cur
        #     else:
        #         prev = cur
        #         cur = cur.next

        # return dummy.next

#using hashmap
       
        dic=defaultdict(int)
        cur=head
        while cur:
            dic[cur.val]+=1
            cur=cur.next
        
        # ans=[]
        newLi=ListNode(0)
        dummy=newLi
        for i in dic:
            if dic[i]==1:
                newNode=ListNode(i)
                newLi.next=newNode
                newLi=newLi.next
        return dummy.next


