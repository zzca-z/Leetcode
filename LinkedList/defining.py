class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,*args):
        self.head = None
        if args:
            self.head = LinkedNode(args[0])
            count = 0
            current = self.head
            while count < (len(args) - 1):
                current.next = LinkedNode(args[count+1])
                current = current.next
                count += 1
        
    
    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def add_head(self, *args):
        if not self.head:
            self.head = LinkedNode(args[-1])
        
            count = len(args) - 2
            while count >= 0:
                current = self.head
                self.head = LinkedNode(args[count])
                self.head.next = current
                count -= 1
        else:
            count = len(args) - 1
            while count >= 0:
                current = self.head
                self.head = LinkedNode(args[count])
                self.head.next = current
                count -= 1


    def append(self, *args):
        if not self.head:
            self.head = LinkedNode(args[0])

        current = self.head
        count = 0
        while current.next:
            current = current.next
        for _ in args:
            current.next = LinkedNode(args[count])
            current = current.next
            count += 1
    
    def get(self, index):
        current = self.head
        count = 0
        if index >= self.len():
            print("get: Out of index.")
            return
        if index < 0:
            index = self.len() + index
            if index < 0:
                print("get: Out of index.")
                return

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
        if index > self.len():
            print("insert: Out of index.")
            return
        if index < 0:
            index = self.len() + index
            if index < 0:
                print("insert: Out of index.")
                return
        if index == 0:
            self.head = LinkedNode(value)
            self.head.next = current
            return
        else:
            while current:
                if count == index-1:
                    original_next = current.next
                    current.next = LinkedNode(value)
                    current.next.next = original_next
                    return
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
    
    def delet_index(self, index):
        current = self.head
        count = 0
        if index >= self.len():
            print("delet: Out of index.")
            return
        if index < 0:
            index = self.len() + index
            if index < 0:
                print("delete: Out of index.")
                return
        if index == 0:
            self.head = current.next
        else:
            while current:
                if count == index - 1:
                    current.next = current.next.next
                    return
                current = current.next
                count += 1
    
    def delet_value(self, value):
        current = self.head
        while self.head.value == value:
            self.head = current.next
            current = self.head
        
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next

    def revert(self):
        current = self.head
        last = None
        while current:
            next = current.next
            current.next = last
            last = current
            current = next
        self.head = last
         
            




ll = LinkedList(10)
ll.add_head(20,30)
ll.show()
