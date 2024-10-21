from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # interweave and store new nodes attached to the old nodes
        cur = head
        while cur:
            newNode = Node(cur.val, cur.next)
            cur.next = newNode
            cur = newNode.next

        # set random references for the new nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # separate the old and new lists
        oldHead = head
        newHead = head.next
        oldCur = oldHead
        newCur = newHead
        while oldCur:
            oldCur.next = oldCur.next.next
            newCur.next = newCur.next.next if newCur.next else None
            oldCur = oldCur.next
            newCur = newCur.next

        return newHead
