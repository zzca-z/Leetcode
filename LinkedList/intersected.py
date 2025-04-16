class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None
    def show(self):
        output = ''
        current =self
        while current:
            output += f'{current.value} -> '
            current = current.next
        print(output)

class Solution:
    def getIN_2loop(self, headA:ListNode, headB:ListNode) -> ListNode:
        currentA = headA
        currentB = headB
        intersection = None
        while currentA != None and currentB != None:
            while currentA != None:
                if currentA == currentB:
                    intersection = currentA
                    break
                currentA = currentA.next
            if intersection != None:
                break
            currentA = headA
            currentB = currentB.next
        
        return intersection
    def getIN_1loop(self, headA:ListNode, headB:ListNode) -> ListNode:
        lenthA = 0
        currentA = headA
        while currentA:
            lenthA += 1
            currentA = currentA.next
        
        lenthB = 0
        currentB = headB
        while currentB:
            lenthB += 1
            currentB = currentB.next

        currentA = headA
        currentB = headB

        if lenthA > lenthB:
            for _ in range(abs(lenthA-lenthB)):
                currentA = currentA.next
        else:
            for _ in range(abs(lenthA-lenthB)):
                currentB = currentB.next
        
        intersection = None
        while currentA:
            if currentA == currentB:
                intersection = currentA
                break
            currentA = currentA.next
            currentB = currentB.next
        
        return intersection
                       

class LinkedList:
    def __init__(self, *args):
        if args:
            self.head = ListNode(args[0])
            current = self.head
            for i in range(1,len(args)):
                current.next = ListNode(args[i])
                current = current.next


la = LinkedList(1,2,3)
lb = LinkedList(4)
lb.head.next=la.head.next

la.head.show()
lb.head.show()

s = Solution()

print(s.getIN_1loop(la.head, lb.head).value)


'''
1. In 2 layers loop, remember to break both layers once criteria is fullfilled.
2. For linkedlist with intersection, the intersection must not be longer than the shorter list, so we can 
    move the pointers to the head of shorter one and the corresponding place of the longer one, and then
    move the two pointers together, avoiding 2 layers loop.
'''