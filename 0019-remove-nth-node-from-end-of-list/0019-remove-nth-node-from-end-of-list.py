# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        temp = head

        # First pass: count total nodes
        while temp:
            counter += 1
            temp = temp.next

        # If we need to remove the head
        if counter == n:
            return head.next

        # Second pass: stop at the node just before the one to remove
        temp = head
        for _ in range(counter - n - 1):
            temp = temp.next

        # Skip the node
        if temp.next:
            temp.next = temp.next.next

        return head