# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if head contains only one element return the element
        if head.next is None:
            return head

        # slow pointer start with head
        slow = head

        # check if the fast pointer would be none, then return next pointer of slow
        if slow.next.next is None:
            return slow.next

            # fast pointer start with two elements after the slow ==> slow.next.next
        fast = slow.next.next

        # Repeat the while loop until the fast pointer reached to the end
        while fast is not None:

            if fast.next is None:
                break

            slow = slow.next
            fast = fast.next.next

        return slow.next


