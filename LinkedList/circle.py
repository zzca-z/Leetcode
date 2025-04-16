from typing import Optional
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def cycle(self, head:Optional[ListNode]) -> Optional[ListNode]:
        cyclepoint = None
        current = head
        nodes =[]
        while current:
            if current in nodes:
                cyclepoint = current
                break
            nodes.append(current)
            current = current.next
        
        return cyclepoint