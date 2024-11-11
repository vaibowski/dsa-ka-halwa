from typing import Optional

from linked_lists.problems.merge_two_sorted_lists import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None:
            return head
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findKth(groupPrev, k)
            if not kth:
                break

            groupNext, cur = kth.next, groupPrev.next
            prev = groupNext

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def findKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
