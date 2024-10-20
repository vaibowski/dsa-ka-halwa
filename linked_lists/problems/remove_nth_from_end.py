from typing import Optional

from linked_lists.problems.merge_two_sorted_lists import ListNode


class Solution:
    def removeNthFromEndIterative(self, head: ListNode, n: int) -> ListNode:
        ptr, length = head, 0
        while ptr:
            ptr, length = ptr.next, length + 1
        if length == n : return head.next
        ptr = head
        for i in range(1, length - n):
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head
