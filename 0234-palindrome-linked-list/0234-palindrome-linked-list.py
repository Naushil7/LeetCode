# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # length = 0
        # temp = head
        # while temp:
        #     length += 1
        #     temp = temp.next
        
        # stack = []
        # temp = head
        # for i in range(length // 2):
        #     stack.append(temp.val)
        #     temp = temp.next

        # if length % 2 == 1:
        #     temp = temp.next

        # while temp:
        #     if not stack or temp.val != stack.pop():
        #         return False
        #     temp = temp.next

        # return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True