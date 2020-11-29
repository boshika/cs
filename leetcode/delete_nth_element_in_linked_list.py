# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head

        while temp is not None:
            temp = temp.next
            length += 1

        k = length - n

        p1 = head
        prev = None

        while k != 0:
            prev = p1
            p1 = p1.next
            k-=1

        if prev is None:
            return head.next
        else:
            prev.next  = p1.next
            p1.next = None
            return head