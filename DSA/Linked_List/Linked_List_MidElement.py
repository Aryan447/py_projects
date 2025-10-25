# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    if (head.val is None):
        return None
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow.val

obj16 = ListNode(17)
obj15 = ListNode(16, obj16)
obj14 = ListNode(15, obj15)
obj13 = ListNode(14, obj14)
obj12 = ListNode(13, obj13)
obj11 = ListNode(12, obj12)
obj10 = ListNode(11, obj11)
obj9 = ListNode(10, obj10)
obj8 = ListNode(9, obj9)
obj7 = ListNode(8, obj8)
obj6 = ListNode(7, obj7)
obj5 = ListNode(6, obj6)
obj4 = ListNode(5, obj5)
obj3 = ListNode(4, obj4)
obj2 = ListNode(3, obj3)
obj1 = ListNode(2, obj2)
head = ListNode(1, obj1)
print(middleNode(head))
