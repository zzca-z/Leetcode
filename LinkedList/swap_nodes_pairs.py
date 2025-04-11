# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def show(self):
        current = self
        output = ''
        while current:
            output += f"{current.val} -> "
            current = current.next
        print(output)

class Solution:
    def len_ll(self, head):
        count = 0 
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp_head = ListNode()
        temp_head.next = head
        current = temp_head
        lenth = self.len_ll(head)
        while count + 2 <= lenth:
            first = current.next
            second = current.next.next
            new_first = current.next.next.next
    
            second.next = first
            first.next = new_first
            current.next = second
            current = current.next.next
            count += 2

        head = temp_head.next
        
        return head
    

class LinkedLikst:
    def __init__(self, *args):
        self.head = None
        if args:
            self.head = ListNode(args[0])
            count = 1
            current = self.head
            while count < len(args):
                current.next = ListNode(args[count])
                current = current.next
                count +=1
    def show(self):
        current = self.head
        output = ""
        while current:
            output += f"{current.val} -> "
            current = current.next
        print(output)

ll = LinkedLikst()
ll.head.show()
s = Solution()
s.swapPairs(ll.head).show()

'''
1. assignment: when processing swap, backup the to be changed value firsh, so that the originial relationship can be maintained. And the assignment only align the left to the right, thus the new assignment to the left won't affect the right but not verce vice. Use the one that remians unchanged or changed last to be the assignment value at the right, this could avoid chain effection.
2. becareful about the loop termination condition in case it get modified in the loop. make it a certain value instead of an expression could be safer.
3. checking the main aspects first, like the loop times, then samller aspects.
'''