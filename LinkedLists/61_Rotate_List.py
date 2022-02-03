# https://leetcode.com/problems/rotate-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # if empty or single element
        if not head or not head.next:
            return head

            # get the count of the linked list
        count = 0
        currNode = head
        while currNode:
            count += 1
            currNode = currNode.next

        # get the total number of rotations by taking the input modulo with the count
        rotations = k % count

        # rotate the array based on the rotations
        fast = head
        for i in range(rotations):
            while fast.next:
                if fast.next.next:
                    prev = fast.next
                    fast = fast.next.next
                else:
                    prev = fast
                    fast = fast.next
            prev.next = None
            fast.next = head
            head = fast

        return head
