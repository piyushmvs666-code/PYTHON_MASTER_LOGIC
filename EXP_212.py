# Reverse a Singly Linked List.
  class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # Step 1: Temporarily store the next node
        curr.next = prev       # Step 2: Reverse the current node's pointer
        prev = curr            # Step 3: Move the prev pointer one step forward
        curr = next_node       # Step 4: Move the curr pointer one step forward
        
    return prev  # prev will be the new head of the reversed list
