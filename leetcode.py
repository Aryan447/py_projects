'''
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
'''
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        dummy = head
        while dummy.next:
            dummy = head.next
            length += 1

        position =


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

mylist = node1

mysol = Solution()
print(mysol.rotateRight(node1, 2))
