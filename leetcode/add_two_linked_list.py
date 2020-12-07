# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = cur = ListNode(0)
        carry = 0

        print(l1.val, l2.val, carry)

        while l1 or l2 or carry:

            current_val = carry
            current_val += 0 if l1 is None else l1.val
            current_val += 0 if l2 is None else l2.val

            if current_val >= 10:
                current_val -= 10
                carry = 1
            else:
                carry = 0

            print('--------:', current_val, carry)

            cur.next = ListNode(current_val)
            cur = cur.next

            # Add base cases for iterating linked lists.
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        return head.next


# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    else:
        return str(l.val) + '---->' + linked_list_str(l.next)


# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(6)
print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(linked_list_str(l2))

# Add linked lists.
s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(linked_list_str(l3))

