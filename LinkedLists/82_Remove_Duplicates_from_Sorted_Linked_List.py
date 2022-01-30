# Remove duplicates from the sorted linked list
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        currNode = head
        prev = None
        deleted_node = ListNode(101)  # reference node for comparison

        while currNode is not None:
            # End of the node handle
            if currNode.next is None:
                if currNode.val == deleted_node.val:
                    if prev and prev.next and prev.next.val == deleted_node.val:
                        prev.next = None
                    else:
                        head = prev
                break
            # if currNode and next Node are equal
            if currNode.val == currNode.next.val or currNode.val == deleted_node.val:
                deleted_node = currNode
                if currNode == head:
                    head = currNode.next
                    currNode = currNode.next
                else:
                    if prev is not None:
                        prev.next = currNode.next
                    else:
                        prev = currNode.next
                    currNode = prev.next
            # if currNode not equal, move to next node
            else:
                prev = currNode
                currNode = currNode.next

        return head