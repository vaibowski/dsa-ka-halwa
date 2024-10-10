from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # trick is to get a head pointer to return the linked list at the end, and a current pointer to build the merged
    # linked list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        cur = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    cur = head
                else:
                    cur.next = list1
                    cur = cur.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    cur = head
                else:
                    cur.next = list2
                    cur = list2
                list2 = list2.next
        if not list1:
            cur.next = list2
        else:
            cur.next = list1
        return head
