# Design Hash Set
# https://leetcode.com/problems/design-hashset/
# Design the solution without using the programming language buit-in hash set
# Below solution is brute force approach and it does searches in O(n)
#https://leetcode.com/problems/design-hashset/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyHashSet:

    def __init__(self):
        self.root = None

    def add(self, key: int) -> None:
        node = Node(key)
        if not self.root:
            self.root = node
        else:
            if not self.contains(key):
                currNode = self.root
                while currNode.next:
                    currNode = currNode.next
                currNode.next = node

    def remove(self, key: int) -> None:
        if self.contains(key):
            currNode = self.root
            prev = None

            while currNode:
                if currNode.data == key:
                    if currNode == self.root:
                        self.root = currNode.next
                    elif currNode.next is not None:
                        prev.next = currNode.next
                    else:
                        prev.next = None
                    break
                prev = currNode
                currNode = currNode.next

    def contains(self, key: int) -> bool:
        currNode = self.root
        while currNode:
            if currNode.data == key:
                return True
            currNode = currNode.next
        return False

    # Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


