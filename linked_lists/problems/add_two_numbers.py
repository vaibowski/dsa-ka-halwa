from typing import Optional

from linked_lists.problems.merge_two_sorted_lists import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        cur = l1
        count = 0
        while cur:
            num1 += 10 ** count * (cur.val)
            count += 1
            cur = cur.next

        cur = l2
        count = 0
        while cur:
            num2 += 10 ** count * (cur.val)
            count += 1
            cur = cur.next

        num = num1 + num2
        head, cur = None, None
        if num == 0:
            return ListNode(0)
        while num != 0:
            node = ListNode(num % 10)
            num //= 10
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = cur.next

        cur.next = None
        return head
