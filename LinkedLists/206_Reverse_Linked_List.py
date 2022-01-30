# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None

        # logic is to store the next element
        # change the current next element to previous
        # set the previous to the current element
        # set the next element
        # once done, change the head to the final previous element
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head = prev

        return head


