# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = cur

            if prev:
                prev.next = nxt
            else:
                head = nxt

            prev = cur
            cur = cur.next

        return head
