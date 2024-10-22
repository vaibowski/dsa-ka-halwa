from typing import Optional

from linked_lists.problems.merge_two_sorted_lists import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast and slow:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return False
