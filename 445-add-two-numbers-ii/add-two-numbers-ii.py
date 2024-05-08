# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]

        #fill your stacks
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next

        carry= 0
        res= None

        #pop from every stack while adding the values. 
        while stack1 or stack2 or carry:
            add= carry

            if stack1:
                add+=stack1.pop()

            if stack2:
                add+=stack2.pop()
            
            #modulo to get the last digit of a number above 10
            node= ListNode(add%10)

            node.next=res
            res=node

            #get the first digit of a number greater than 10
            carry=add//10
            # print('carry-value:',carry, add%10)
        return res

      
        