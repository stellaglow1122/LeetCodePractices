"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from queue import Queue

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        q = Queue()
        q.put(node)
        nodeCreatedList = {node.val:Node(node.val, [])}
        while not q.empty():
            nodeToCopy = q.get()
            currentNode = nodeCreatedList[nodeToCopy.val]

            for neighbor in nodeToCopy.neighbors:
                if neighbor.val not in nodeCreatedList.keys():
                    nodeCreatedList[neighbor.val] = Node(neighbor.val, [])
                    q.put(neighbor)
                currentNode.neighbors.append(nodeCreatedList[neighbor.val])
        
        return nodeCreatedList[1]
