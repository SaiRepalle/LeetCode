# Remove Duplicates from sorted linked list
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        currNode = head.next
        prev = head

        while currNode:
            if currNode.val == prev.val:
                prev.next = currNode.next
            else:
                prev = currNode

            currNode = currNode.next

        return head
