# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
    
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

input_values = [3,2,0,-4]
head = create_linked_list(input_values)

# Creating a cycle for testing: Connecting the last node to the node at index 1
# This creates a cycle where -4 points back to 2
cycle_start_node = head.next  # Node with value 2
current = head
while current.next:
    current = current.next
current.next = cycle_start_node

print(Solution().hasCycle(head))