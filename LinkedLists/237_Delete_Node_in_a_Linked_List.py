# Delete Node in a Linked List
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
# instead you will be given access to the node to be deleted directly.
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

