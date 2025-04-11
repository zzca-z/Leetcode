from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def show(self):
        output = ''
        current = self
        while current:
            output += f"{self.value} -> "
            current = current.next
        print(output)
    def llen(self):
        count = 0
        current = self
        while current:
            count += 1
            current = current.next
        return count

class LinkedList:
    def __init__(self, *args):
        self.head = None
        count = 1
        if args:
            self.head = ListNode[args[0]]    
        current = self.head
        while count < len(args):
            current.next = ListNode[args[count]]
            count += 1
            current = current.next            



class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n:int) -> Optional[ListNode]:
        length = head.llen()
        count = 0
        temphead = ListNode
        temphead.next = head
        current = temphead
        while count < length-n:
            current = current.next
            count +=1
        current.next = current.next.next
        head = temphead.next
        
        return head


'''
1. To decide  <, <=, length-n or length-n+1, we can use simple examples like 2 nodes to try. Because the formular must hold at 2 nodes and the format of it is fixed.
'''