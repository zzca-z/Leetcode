class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if not self.head:
            self.head = LinkedNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = LinkedNode(value)
    
    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return None
    
    def insert(self, value, index):
        current = self.head
        count = 0 
        original_next = None
        if index == 0:
            self.head = LinkedNode(value)
            self.head.next = current
            return
        while current:
            if count == index-1:
                original_next = current.next
                current.next = LinkedNode(value)
            elif count == index and original_next:
                current.next = original_next
            current = current.next
            count += 1
    
    def show(self):
        current = self.head
        output = ""
        if not current:
            output = "None"
        else:
            while current:
                output += f"{current.value} -> "
                current = current.next
        print(output)

ll = LinkedList()
ll.append(10)
ll.append(20)

ll.insert(15,1)
ll.show()
