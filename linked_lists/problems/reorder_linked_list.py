from typing import Optional
from linked_lists.problems.merge_two_sorted_lists import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev

        list2 = reverse(slow.next)
        list1 = head
        slow.next = None
        while list1 and list2:
            temp1 = list1.next
            list1.next = list2
            temp2 = list2.next
            list2.next = temp1
            list1 = temp1
            list2 = temp2

        if list1:
            list1.next = None

        return head