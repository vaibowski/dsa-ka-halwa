import heapq
from typing import List, Optional

from linked_lists.problems.merge_two_sorted_lists import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ls in lists:
            cur = ls
            while cur:
                heapq.heappush(heap, cur.val)
                cur = cur.next

        head = None
        cur = None
        while len(heap) > 0:
            ele = heapq.heappop(heap)
            node = ListNode(ele)
            if head is None:
                head = node
                cur = head
            else:
                cur.next = node
                cur = node

        return head
