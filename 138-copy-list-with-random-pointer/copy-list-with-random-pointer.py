"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a dictionary to map original nodes to their copies
        nodedict = {}
        nodedict[None]= None # add this so if we try to reference None, we get None back
        current = head
        # If the list is empty, return None
        if not current:
            return 
        # Traverse the original list to create copies of all nodes
        while current:
            # Create a new node with the same value as the current node
            copy = Node(current.val)
            # Add the new node to the dictionary
            nodedict[current] = copy
            # Move to the next node in the original list
            current = current.next
            
        # Reset current to the head of the original list
        current = head
        # Traverse the original list again to set the next & random pointers in the copied list
        while current:
            # Get the new node corresponding to the current node
            newCurrent = nodedict[current]
            # Set the next pointer of the new node to the new node corresponding to the next node in the original list
            newCurrent.next = nodedict[current.next]
            # If the current node has a random pointer, set the random pointer of the new node to the new node corresponding to the random node in the original list
            if current.random:
                newCurrent.random = nodedict[current.random]
            # Move to the next node in the original list
            current = current.next
            
        # Return the new node corresponding to the head of the original list
        return nodedict[head] 