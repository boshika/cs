# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        ptr = l3

        while True:
            if l1 is None:
                ptr.next = l2
                break
            elif l2 is None:
                ptr.next = l1
                break
            elif l1 is None and l2 is None:
                break
            else:
                small_value = 0

                if l1.val < l2.val:
                    small_value = l1.val
                    l1 = l1.next
                else:
                    small_value = l2.val
                    l2 = l2.next

                new_node = ListNode(small_value)
                ptr.next = new_node
                ptr = ptr.next

        return l3.next

