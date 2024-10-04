"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        # creating a dictionary to store all created clones against the node values
        clones = {}
        return self.dfs(node, clones)

    def dfs(self, node, clones):
        # if there is a clone already created for the val, we return its reference
        if node.val in clones:
            return clones[node.val]

        # else create a new node, and iterate over the original nodes neighbors and add them to the clone's neighbors
        newNode = Node(node.val)
        clones[node.val] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.dfs(neighbor, clones))
        return newNode
